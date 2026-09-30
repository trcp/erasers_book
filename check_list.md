# 確認事項リスト

執筆・レビューの過程で出てきた「あとで確認・判断が必要なこと」をまとめたリストです。
対応したらチェックを入れ、不要になった項目は削除してください。
ファイルのパスは `book/` からの相対パスです。

---

## 1. 動作確認（Ubuntu 24.04 + ROS 2 Jazzy の実機で）

執筆ルールでは、掲載するコマンドと結果は実際の環境で確認することになっています。
以下は執筆時に 24.04 で実行できておらず、想定で書いている箇所です。

### 第4章 ターミナルとシェル（`chapters/commandline/terminal_shell.tex`）

- [ ] Ubuntu 24.04 の標準のターミナルアプリが GNOME Terminal であること、日本語環境でのアプリ名が「端末」であること
- [ ] `head -n 3 /etc/os-release` の出力（`PRETTY_NAME` のポイントリリース番号 `24.04.1` など）
- [ ] `ls --help` の出力の冒頭部分
- [ ] `sudo apt install tldr` でインストールできること、`tldr --update` が必要かどうか、`tldr tar` の出力の形式
- [ ] `help cd` の出力
- [ ] `type date` / `type cd` / `which date` の出力（`/usr/bin/date` など）
- [ ] 存在しないコマンドを入力したときのメッセージ（`LS: command not found`）
- [ ] `ping localhost` の出力の形式
- [ ] `Ctrl+R` の表示（`(reverse-i-search)`）

### 第5章 ファイルとディレクトリの操作（`chapters/commandline/files.tex`）

- [ ] 新しくインストールした直後のホームディレクトリの `ls` / `ls -a` / `ls -lh` の出力（`snap` ディレクトリの有無など）
- [ ] `ls /` の出力
- [ ] `cp` / `mkdir` / `rm` のエラーメッセージの文言
- [ ] `LANG=C xdg-user-dirs-gtk-update` でディレクトリ名を英語に変えられること（ダイアログのボタン名「Update Names」）
- [ ] `find /opt/ros/jazzy -name "*.launch.py"` の出力例のパス
- [ ] `sudo apt install plocate` で `locate` が使えるようになること、`locate turtlesim_node` の出力のパス
- [ ] `tail -f ~/.ros/log/latest/launch.log` のパスが実在すること
- [ ] `head -n 2` / `tail -n 2 /etc/os-release` の出力

### 第3章 Linux の仕組み（`chapters/linux/linux_internals.tex`）

- [ ] `uname -r` の出力例（`6.8.0-45-generic`）と、「Ubuntu 24.04 では 6.8 系のカーネル」という記述（HWE カーネルで新しい版になる場合がある）
- [ ] `id` の出力例で、インストール時に作ったユーザが所属するグループ（`adm`, `cdrom`, `sudo`, `dip`, `plugdev`, `users`, `lpadmin`）
- [ ] `sudo` のパスワード入力時の表示（`[sudo] password for user:`）
- [ ] `head -n 3 /proc/meminfo` の出力の形式
- [ ] Ubuntu 24.04 で `/bin` が `/usr/bin` へのシンボリックリンクになっていること、`/tmp` が再起動で消えること

### 第15章 Docker 入門（`chapters/tools/docker.tex`）

- [ ] Docker のインストール手順が、出版時点の公式ドキュメント（https://docs.docker.com/engine/install/ubuntu/）と合っているか（リポジトリの設定ファイルの形式が変わることがある）
- [ ] `docker run hello-world`、`docker images`、`docker ps -a`、`docker build` の出力の形式
- [ ] ROS 2 の公式イメージのタグ（`ros:jazzy-ros-core`、`ros:jazzy`、`osrf/ros:jazzy-desktop`）と、`osrf/ros:jazzy-desktop` に `demo_nodes_cpp` が含まれていること
- [ ] `xhost +local:` と `DISPLAY` の受け渡しで、Ubuntu 24.04（Wayland）の上で turtlesim のウィンドウが表示されること
- [ ] `--network host --ipc host` で、2 つのコンテナの talker / listener が通信できること
- [ ] Dev Containers の `devcontainer.json` の例で、実際にコンテナの中に接続できること
- [ ] Docker Desktop の有料ライセンスの条件

### 第16章 Python とは（`chapters/python/what_is_python.tex`）

- [ ] `gcc hello.c -o hello` の例：Ubuntu 24.04 のデスクトップ版には `gcc` が標準で入っていない可能性がある（`sudo apt install build-essential` が必要か）。本文で断るか
- [ ] `python3 --version` の出力（`Python 3.12.3`）

### 第17章 Python の開発環境（`chapters/python/python_env.tex`）

- [ ] Ubuntu 24.04 で `python` コマンドが標準で存在しないこと、`python-is-python3` で使えるようになること
- [ ] 対話モードの起動時の表示（`Python 3.12.3 (main, ...) [GCC 13.2.0] on linux`）
- [ ] `pip` と `venv` が標準で入っておらず、`sudo apt install python3-pip python3-venv` が必要なこと
- [ ] 仮想環境の外で `pip install` したときのエラーメッセージ（`error: externally-managed-environment`）
- [ ] `pip install numpy` の出力と、例に使った NumPy のバージョン（`2.1.1`）
- [ ] `pipx` が `sudo apt install pipx` で入ること
- [ ] ROS 2 と仮想環境を組み合わせる方法（`--system-site-packages`）の記述が、ROS 2 Jazzy の公式ドキュメントの推奨と合っているか
- [ ] コラム「venv 以外の開発ツール」：uv の速さ（開発元の公称で pip の 10〜100 倍）、pixi と RoboStack で ROS 2 の環境を作れること、Anaconda の有料ライセンスの条件が、出版時点の情報と合っているか

### 第2章 Linux とは：Ubuntu 環境の用意・デスクトップ（`chapters/linux/what_is_linux.tex`）

- [ ] インストール手順の流れ（Ubuntu 24.04 のインストーラの画面の順番と文言）
- [ ] `wsl --install -d Ubuntu-24.04` のディストリビューション名
- [ ] 日本語でインストールしたときに Mozc が使える状態になっているか、`半角/全角` キーで切り替えられるか
- [ ] GNOME のショートカットキー（`Super`+矢印、`Print` など）と、「App Center」「ソフトウェアとアップデート」「追加のドライバー」の名称
- [ ] 推奨する PC の性能の目安（CPU 4 コア以上、メモリ 8 GB 以上、ストレージ 50 GB 以上）が妥当か

### 第6章 パーミッションとユーザ管理（`chapters/commandline/permission.tex`）

- [ ] `ls -l /dev/ttyUSB0` の表示（`crw-rw---- 1 root dialout 188, 0 ...`）
- [ ] `groups` の出力（インストール時に作ったユーザの所属グループ）
- [ ] `sudo` のパスワードの有効時間（標準で 15 分）
- [ ] udev のルールの例（CP210x の ID `10c4:ea60`）と、`udevadm` の手順で `/dev/lidar` が作られること

### 第7章 テキスト処理とパイプ（`chapters/commandline/text_pipe.tex`）

- [x] 例のコマンドを実際に `robot.log` と `data.csv` で実行し、出力が本文と一致すること（執筆環境の GNU coreutils で確認済み。Ubuntu 24.04 でも同じ結果になるはずだが、念のため確認するとよい）

### 第8章 プロセスとシステム管理（`chapters/commandline/process.tex`）

- [ ] `ps`, `ps aux`, `top`, `df -h`, `free -h`, `systemctl status ssh` の出力の形式
- [ ] Ubuntu 24.04 で `dmesg` に `sudo` が必要なこと、CP210x を差し込んだときのメッセージ
- [ ] `journalctl -u ssh` のサービス名（`ssh`）

### 第9章 環境変数とシェルの設定（`chapters/commandline/env.tex`）

- [ ] Ubuntu 24.04 の標準の `PATH` の値
- [ ] Ubuntu の `.bashrc` に最初から書かれているエイリアス（`ll`, `la`, `l`）と `PS1` の値

### 第10章 シェルスクリプト入門（`chapters/commandline/shellscript.tex`、`samples/shellscript/setup_dev.sh`）

- [ ] `samples/shellscript/setup_dev.sh` を Ubuntu 24.04 の実機で実行し、本文の出力例と一致すること（執筆時は `sudo` と `dpkg` を差し替えた環境でだけ確認）

### 第11章 パッケージ管理（`chapters/tools/package.tex`）

- [ ] `apt update` / `apt install tree` / `apt show htop` の出力（バージョン番号、サイズなど）
- [ ] `/etc/apt/sources.list.d/ubuntu.sources` の内容（deb822 形式）
- [ ] リポジトリを追加する手順の例（`/etc/apt/keyrings` に鍵を置き `signed-by` で指定する方法）が、Docker や ROS 2 の現在の公式手順と矛盾しないか
- [ ] VS Code の `.deb` ファイル名の例（`code_1.93.1_amd64.deb`）
- [ ] CMake の例の出力（`The C compiler identification is GNU 13.2.0` など）と、`cmake_minimum_required(VERSION 3.10)` の値

### 第12章 エディタ（`chapters/tools/editor.tex`）

- [ ] Ubuntu 24.04 に最初から入っている Vim（`vi` コマンド）の範囲と、`vimtutor` が `sudo apt install vim` で使えるようになること
- [ ] Ubuntu の標準のエディタ（`git commit` などで開くもの）が nano であること
- [ ] VS Code の `.deb` ファイルでインストールすると公式リポジトリが自動で登録されること、ファイル名の例（`code_1.93.1_amd64.deb`）
- [ ] 紹介する拡張機能の名前（Japanese Language Pack、Python、C/C++、YAML・XML）と、ROS 2 向けの拡張機能を具体的に紹介するか
- [ ] コラム「エディタ戦争」：開発者向けの調査で VS Code が最も多く使われているという記述（出典を示すか）

### 第13章 Git によるバージョン管理（`chapters/tools/git.tex`）

- [ ] `git --version` の出力（`2.43.0`）、`git init` / `git status` / `git commit` / `git merge` の出力の文言
- [ ] `sudo apt install gh` で GitHub CLI が入ること、`gh auth login` の質問の文言
- [ ] 本文の「本書の原稿も GitHub で管理されている」という記述を残すか（リポジトリを公開するかどうかによる）

### 第14章 ネットワークとリモート操作（`chapters/tools/network.tex`）

- [ ] `ip a` の出力の形式と、ネットワークの名前の例（`wlp2s0`, `enp0s31f6`）
- [ ] `ss -tln` の出力の形式
- [ ] Ubuntu 24.04 のデスクトップ版に `openssh-server` が入っていないこと、インストール後に自動で起動すること
- [ ] 初回接続時のメッセージ、`ssh-keygen -t ed25519`、`ssh-copy-id` の出力
- [ ] `ホスト名.local`（mDNS）が Ubuntu 24.04 の標準で使えること
- [ ] `rsync -av` の出力の形式、`tmux ls` の出力の形式
- [ ] コラム「ターミナルマルチプレクサのいろいろ」：herdr と cmux の説明（各リポジトリの README をもとに執筆。herdr は状態の表示・複数マシンの管理・Linux 対応、cmux は macOS 専用の GUI アプリで通知が特徴）が、出版時点の情報と合っているか

### 第2章 Linux とは（`chapters/linux/what_is_linux.tex`）

- [ ] Ubuntu と ROS 2 の対応表（Foxy / Humble / Jazzy）が最新の情報と合っていること

---

## 2. 内容・事実関係の確認

- [ ] **第1章 コンピュータとは**（`chapters/linux/computer.tex`）：メモリ容量やストレージ容量の目安、GPU のコア数（「数千個」）などの数値が現状に合っていること
- [ ] **第1章**：コラム「パソコンのスペック表の読み方」の、ROS 2 開発に必要な性能についての記述が妥当か
- [ ] **第2章**：歴史の年号・人名（UNIX 1969 年、GNU 1983 年、Linux 1991 年、GPL 化 1992 年、Ubuntu 2004 年、「オープンソース」1998 年）
- [ ] **第2章**：ライセンスの比較表（GPL / MIT / BSD / Apache 2.0）の説明は簡略化しているので、誤解を招かないか
- [ ] **第2章**：Ubuntu のサポート期間（LTS 版は 5 年、それ以外は 9 か月、Ubuntu Pro で延長）
- [ ] **第2章**：「リアルタイム性のための機能も用意されている」という記述の粒度（PREEMPT_RT などに具体的に触れるか）
- [ ] **第2章**：2.1 節（歴史）と 2.2 節（OSS）で「1991 年に Linus Torvalds が公開」という内容が重複している。2.2 節側を `\ref{sec:linux-history}` を使った書き方に変えるか
- [ ] **第3章**：プロセスの状態を「実行可能・実行中・待機中・終了」の 4 つに簡略化している（ゾンビや停止状態などは省略）。入門書として十分か
- [x] **第3章**：`dialout` グループや udev の話をどこで詳しく扱うか → 第6章 6.4 節で詳しく扱った（付録C からは参照する形にする）
- [ ] **第16章**：「Python は C 言語に比べて数十倍以上遅くなることがある」という記述の妥当性（処理内容によって差が大きい）
- [ ] **第16章**：Python の公開年（1991 年）、Python 2 のサポート終了（2020 年）、名前の由来のコラム
- [ ] **第4章**：実行結果とエラーメッセージを英語表示で掲載する方針でよいか（日本語環境では日本語で表示される旨を 4.3 節で断っている）

---

## 3. 未執筆・書き残し

- [ ] 後の章で OSS の話を振り返る（第2章 2.2 節からの流れ）
  - [x] 第11章 パッケージ管理：`apt` で入れるソフトウェアの多くは OSS で、ディストリビューションが配布している（11.1 節に記載済み）
  - [x] 第13章 Git：GitHub が OSS 開発の中心の場であること、Issue / Pull Request での貢献（13.4 節に記載済み）
  - [ ] 第20章 ROS とは：ROS 2 自体が Apache 2.0 ライセンスの OSS であること
  - [ ] 第23章 ワークスペースとパッケージ：`package.xml` の `<license>` タグ
  - [ ] 第29章 次のステップへ：使う側から貢献する側へ
- [ ] 第IV部 Python 入門の第18章・第19章の本文を書く（第16章・第17章は執筆済み）。内容は ROS 2 のノードを書くのに必要な範囲（特にクラスと継承、コールバック）に絞る
- [x] 第10章 シェルスクリプト入門の「実践：開発環境セットアップスクリプトを書く」は、`apt` を扱う第11章より前にある → 題材はそのままで、`apt-get` について断り書きを入れた
- [ ] 付録D 用語集（`appendix/glossary.tex`）に、これまでの章で導入した用語を追加する
  - 第1章：CPU、コア、クロック周波数、メモリ（RAM）、ストレージ、GPU、VRAM、入出力装置、ハードウェア、ソフトウェア、機械語、OS、デバイスドライバ、マイコン
  - 第2章：カーネル、UNIX、GNU、UNIX 哲学、OSS、フリーソフトウェア、ライセンス、コピーレフト、パーミッシブ、ディストリビューション、LTS
  - 第3章：ユーザ空間、カーネル空間、システムコール、ファイルシステム、ルートディレクトリ、マウント、FHS、ユーザ、UID、グループ、GID、root、sudo、プロセス、PID、親プロセス・子プロセス、systemd、スケジューラ、デバイスファイル
  - 第15章：コンテナ、Docker、仮想マシン、ハイパーバイザ、イメージ、タグ、レジストリ、Docker Hub、Dockerfile、ボリューム（`-v`）、Docker Compose、Dev Containers、Docker Desktop
  - 第16章：インタプリタ、コンパイラ、コンパイル、ソースコード、静的型付け、動的型付け、ガベージコレクション、ライブラリ
  - 第17章：対話モード、スクリプト、shebang、標準ライブラリ、パッケージ、PyPI、pip、仮想環境、venv、PEP 668、pipx
  - 第2章（追加）：デュアルブート、仮想マシン、WSL2、ISO ファイル、GNOME、デスクトップ環境、Dock、ワークスペース、Super キー、Mozc
  - 第6章：パーミッション、所有者、chmod、chown、sudoers、tee、dialout、udev、ルールファイル、ベンダ ID、プロダクト ID
  - 第7章：標準入力、標準出力、標準エラー出力、リダイレクト、/dev/null、パイプ、CSV、grep、正規表現、wc、cut、sort、uniq、sed、awk
  - 第8章：ps、top、htop、load average、フォアグラウンド、バックグラウンド、ジョブ、シグナル、SIGINT、SIGTERM、SIGKILL、kill、pkill、df、du、free、スワップ、サービス、journalctl、systemctl、dmesg
  - 第9章：変数、シェル変数、環境変数、PATH、export、source、.bashrc、エイリアス、関数、PS1
  - 第10章：シェルスクリプト、コメント、コマンド置換、引数、クォート、if 文、for 文、while 文、終了ステータス、set -euo pipefail
  - 第11章：パッケージ、依存関係、パッケージ管理システム、apt、リポジトリ、GPG 鍵、電子署名、.deb、snap、PPA、ビルド、make、Makefile、CMake
  - 第12章：テキストエディタ、テキストファイル、シンタックスハイライト、補完、ターミナルエディタ、GUI エディタ、nano、Vim、vi、モード、Emacs、VS Code、拡張機能、統合ターミナル、コマンドパレット、Remote - SSH、Dev Containers
  - 第13章：README、Markdown、バージョン管理システム、Git、リポジトリ、作業ディレクトリ、ステージングエリア、コミット、コミットハッシュ、差分、.gitignore、ブランチ、マージ、コンフリクト、GitHub、リモートリポジトリ、push、pull、clone、Pull Request、レビュー、Issue、GitHub Flow
  - 第14章：IP アドレス、プライベートアドレス、localhost、DHCP、ホスト名、mDNS、ポート番号、SSH、公開鍵認証、秘密鍵、公開鍵、パスフレーズ、scp、rsync、tmux、セッション、デタッチ、アタッチ、ターミナルマルチプレクサ、screen、zellij、コーディングエージェント
  - 第4章：GUI、CUI、CLI、ターミナル、シェル、bash、プロンプト、ビルトインコマンド、man ページ、Tab 補完
  - 第5章：カレントディレクトリ、ホームディレクトリ、隠しファイル、パス、絶対パス、相対パス、ワイルドカード、ブレース展開
- [ ] 付録A コマンド早見表に、第4章・第5章のコマンドを追加する

---

## 4. 図版

図は TikZ で描いて `images/<章のファイル名>/` に置いています（31 点）。
残りの 5 か所はスクリーンショットが必要なため、プレースホルダのままです。
残っている箇所は `grep -rn '入れる画像' book/` で一覧できます。

| 章 | ラベル | 内容 | 状態 |
| --- | --- | --- | --- |
| 第12章 | `fig:editor-vscode` | VS Code の画面 | 要スクリーンショット |
| 第2章 | `fig:linux-desktop` | Ubuntu 24.04 のデスクトップ | 要スクリーンショット |
| 第4章 | `fig:terminal-gui-cli` | 同じディレクトリを GUI と CLI で表示した例 | 要スクリーンショット |
| 第4章 | `fig:terminal-window` | Ubuntu のターミナル | 要スクリーンショット |
| 第4章 | `fig:terminal-man` | `man ls` の表示画面 | 要スクリーンショット |

- [ ] 上の 5 点のスクリーンショットを Ubuntu 24.04 で撮影する
- [ ] TikZ で描いた 31 点の図の内容・見た目を確認する（第1章 5 点、第2章 3 点、第3章 3 点、第4章 2 点、第5章 2 点、第6章 1 点、第7章 2 点、第8章 1 点、第9章 1 点、第11章 1 点、第12章 1 点、第13章 2 点、第14章 3 点、第15章 2 点、第16章 1 点、第17章 1 点）
- [ ] 第5章のコラム「ホームディレクトリの中のディレクトリ名」に `xdg-user-dirs-gtk-update` のダイアログの画像を入れるか（コラムの囲みの中には `figure` を置けないため、入れる場合はコラムの外に出すか、囲みの中に `\includegraphics` を直接書く）

---

## 5. 組版・体裁

- [ ] 第I部の名前：「Linux 入門」のままでよいか（第1章「コンピュータとは」が入ったので、「コンピュータと Linux の基礎」などにするか）
- [ ] ソースコードのキャプションが「Listing 16.1」と英語で表示される。`preamble.tex` に `\renewcommand{\lstlistingname}{リスト}` を追加して「リスト 16.1」にするか（要相談）
- [ ] 第16章の比較表のページが、わずかに版面の下にはみ出している（Overfull \vbox 3pt 程度）。本文が固まったら改ページ位置を確認する
- [ ] 用紙サイズが A5 から A4 に変わった。図は A5（本文の幅 約 109 mm）を想定して横幅 10 cm 程度で描いているので、A4 では小さく見える。A4 のままにするなら、図を拡大するか（`\resizebox` やフォントサイズの調整）検討する
- [ ] 表紙の日付が `\date{\today}`（ビルドした日）になっている。発行日などに固定するか
- [ ] 第4章のキー操作一覧表は列幅が狭く、説明が折り返している。見た目を調整するか
- [ ] `chapters/ros2/tf_viz.tex` の見出し「robot\_state\_publisher と joint\_state\_publisher」が版面から少しはみ出している（Overfull \hbox）
- [ ] ローカル（TeX Live 2019）と CI（最新の TeX Live）で組版結果に差が出ないか、CI の PDF を一度確認する

---

## 6. `preamble.tex` の変更・不具合（要 Issue での相談）

- [ ] `\section` / `\subsection` の直後に文章を挟まずに表を置くとビルドエラーになる（jlreq と `tabular` の組み合わせで発生）。原因を調べて直すか、README の注意書きのままにするか
- [ ] `column` 環境（コラム）はページをまたげないため、長いコラムは版面からはみ出す。`preamble.tex` の `column` の定義に `breakable` を付けて、ページをまたげるようにするか
- [ ] 図のために `\usepackage{tikz}`、`\usetikzlibrary{...}`、共通スタイル（`figbox` など）を追加した。共同執筆者に共有する
- [ ] `terminal` 環境の見た目を Ubuntu のターミナル風（濃い灰色のタイトルバー、右上にウィンドウのボタン、明るい本文、入力行を太字）に変更した。共同執筆者に共有する
- [ ] タイトルを省略した `terminal` 環境で、1 行目に日本語があるとビルドエラーになる。現在は README に注意書きを入れ、タイトルを付けて回避している。環境の定義を直すか検討する

---

## 7. リポジトリ・CI

- [ ] GitHub Actions のワークフロー（`.github/workflows/build-pdf.yml`）が実際に動くことを確認する（`master` への push で Releases の `latest` が更新される / `draft` への push と PR で Artifacts に PDF が置かれる）
- [ ] Settings → Actions → General → Workflow permissions で書き込みが許可されていること（Releases の作成に必要）
- [ ] GitHub のデフォルトブランチが `master` になっていること
- [ ] 以前のワークフローで `draft-pdf` ブランチが作られていたら削除する（`git push origin --delete draft-pdf`）
- [ ] 章ファイルの名前と置き場所を全面的に変更した（番号付きの名前 → 内容を表す名前）。作業中のブランチがある共同執筆者に連絡する
- [ ] 今後の運用（`draft` で書きためて `master` に反映するのか、章ごとのブランチから `master` に PR するのか）を決め、README の「作業の進め方」に反映する
- [ ] README に追加した「ビルドに失敗した PR はマージしないでください」というルールを残すか
