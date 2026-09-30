#!/usr/bin/env bash
# 開発環境のセットアップスクリプト
#   使い方: ./setup_dev.sh [ワークスペースのディレクトリ]
set -euo pipefail

# ワークスペースのディレクトリ（引数がなければ ~/ros2_ws）
WS_DIR="${1:-$HOME/ros2_ws}"
ROS_SETUP="/opt/ros/jazzy/setup.bash"

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

# 2. ワークスペースのディレクトリを作る
if [ -d "$WS_DIR/src" ]; then
    info "$WS_DIR/src はすでにあります"
else
    mkdir -p "$WS_DIR/src"
    info "$WS_DIR/src を作りました"
fi

# 3. .bashrc に ROS 2 の設定を追加する（ROS 2 が入っていて、まだ書かれていなければ）
if [ ! -f "$ROS_SETUP" ]; then
    warn "ROS 2 がインストールされていないので、.bashrc の設定は飛ばします"
elif grep -qF "source $ROS_SETUP" "$HOME/.bashrc"; then
    info ".bashrc にはすでに ROS 2 の設定があります"
else
    echo "source $ROS_SETUP" >> "$HOME/.bashrc"
    info ".bashrc に ROS 2 の設定を追加しました"
fi

# 4. dialout グループに入っているか確認する
if id -nG | grep -qw dialout; then
    info "dialout グループに入っています"
else
    warn "dialout グループに入っていません"
    warn "sudo usermod -aG dialout \$USER を実行して、ログインし直してください"
    exit 1
fi

info "セットアップが完了しました"
