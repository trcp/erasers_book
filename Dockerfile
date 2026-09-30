# 本書の執筆用のイメージ
#   - PDF のビルド（TeX Live）
#   - 原稿の編集（Emacs）、Claude Code、tmux、Git（SSH で push）
# GitHub Actions（.github/workflows/build-pdf.yml）と同じ TeX Live のイメージを元にする
ARG TEXLIVE_TAG=latest
FROM texlive/texlive:${TEXLIVE_TAG}

# 作業用ユーザは、元のイメージにいる texlive ユーザ（UID / GID 1000）を使う
# ホストの UID / GID が 1000 でない場合は、texlive ユーザの UID / GID をホストに合わせる（ファイルの所有者をそろえるため）
ARG USER_NAME=texlive
ARG USER_UID=1000
ARG USER_GID=1000

ENV LANG=C.UTF-8 \
    TZ=Asia/Tokyo \
    TERM=xterm-256color \
    # Claude Code はイメージを作り直して更新する（root の場所に入れているため自動更新は使わない）
    DISABLE_AUTOUPDATER=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        make git openssh-client ca-certificates curl \
        emacs-nox tmux ripgrep less tzdata \
        nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Claude Code（npm のパッケージは、インストール時にネイティブのバイナリを取得するスクリプトを明示的に実行する）
RUN npm install -g @anthropic-ai/claude-code \
    && node "$(npm root -g)/@anthropic-ai/claude-code/install.cjs" \
    && npm cache clean --force

# 作業用ユーザ（texlive）の UID / GID をホストに合わせる
RUN set -eux; \
    if [ "$(id -g ${USER_NAME})" != "${USER_GID}" ]; then groupmod -g ${USER_GID} ${USER_NAME}; fi; \
    if [ "$(id -u ${USER_NAME})" != "${USER_UID}" ]; then usermod -u ${USER_UID} -g ${USER_GID} ${USER_NAME}; fi; \
    chown -R ${USER_UID}:${USER_GID} /home/${USER_NAME}

# LuaTeX のフォントキャッシュ（compose のボリュームで残す）
ENV TEXMFVAR=/tmp/texmf-var
RUN mkdir -p /tmp/texmf-var && chmod 1777 /tmp/texmf-var

USER ${USER_NAME}
WORKDIR /workspace/book

CMD ["make"]
