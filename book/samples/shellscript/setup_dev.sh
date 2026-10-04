#!/usr/bin/env bash
# 開発環境のセットアップスクリプト
#   使い方: ./setup_dev.sh [作業用のディレクトリ]
set -euo pipefail

# 作業用のディレクトリ（引数がなければ ~/dev）
WORK_DIR="${1:-$HOME/dev}"
PATH_LINE='export PATH="$HOME/bin:$PATH"'

info() {
    echo "[INFO] $*"
}

warn() {
    echo "[WARN] $*" >&2
}

# 1. 開発に使うパッケージをインストールする
for pkg in git tree htop tmux; do
    if dpkg -s "$pkg" > /dev/null 2>&1; then
        info "$pkg はインストール済みです"
    else
        info "$pkg をインストールします"
        sudo apt-get install -y "$pkg"
    fi
done

# 2. 作業用のディレクトリを作る
for dir in "$WORK_DIR" "$HOME/bin"; do
    if [ -d "$dir" ]; then
        info "$dir はすでにあります"
    else
        mkdir -p "$dir"
        info "$dir を作りました"
    fi
done

# 3. ~/bin を PATH に追加する設定を .bashrc に書く（まだ書かれていなければ）
if grep -qF "$PATH_LINE" "$HOME/.bashrc"; then
    info ".bashrc にはすでに PATH の設定があります"
else
    echo "$PATH_LINE" >> "$HOME/.bashrc"
    info ".bashrc に PATH の設定を追加しました"
fi

# 4. dialout グループに入っているか確認する
if id -nG | grep -qw dialout; then
    info "dialout グループに入っています"
else
    warn "dialout グループに入っていません"
    warn "USB の機器を使う前に、sudo usermod -aG dialout \$USER を実行して、ログインし直してください"
fi

info "セットアップが完了しました"
