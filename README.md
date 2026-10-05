# これを読めばあなたもロボットを動かせるようになる！

**〜ロボット初学者のための Linux・コマンドライン・ROS 入門〜**

ロボット開発をこれから始める人に向けた入門書です。
Linux とは何かというところから始め、コマンドラインの基本操作、開発に必要な周辺ツール、
そして ROS 2 を使ったロボットソフトウェア開発の基礎までを、順を追って学べるように構成しています。

## 対象読者

- ロボット開発に興味があるが、Linux をほとんど触ったことがない人
- 研究室やロボットチームに配属され、ROS を使う必要が出てきた人
- Windows / macOS の GUI 操作には慣れているが、ターミナル操作に不安がある人

プログラミング経験は必須ではありません。ROS 2 のプログラムを書くのに必要な Python の基本は、第IV部で説明します。

## この本のゴール

この本を読み終えると、次のことができるようになります。

- Linux の仕組みを理解し、ターミナルで日常的な作業ができる
- シェルスクリプトやエディタ、Git を使って開発環境を整えられる
- ROS 2 の基本概念（ノード・トピック・サービス・アクション・パラメータ）を説明できる
- Python で簡単な ROS 2 ノードを書き、ビルド・実行・デバッグできる
- launch ファイル、RViz、Gazebo を使ってシミュレーション上のロボットを動かせる

## 動作環境

| 項目 | バージョン |
| --- | --- |
| 実行環境 | VirtualBox の仮想マシン（ホスト OS は Windows / macOS / Linux のいずれでもよい） |
| OS | Ubuntu 24.04 LTS |
| ROS | ROS 2 Jazzy Jalisco |
| 言語 | Python 3.12（一部 C++） |
| シミュレータ | Gazebo (Harmonic) |

> 本書では、VirtualBox の仮想マシンに Ubuntu 24.04 をインストールして使います。Windows・macOS・Linux のどれを使っていても、同じ手順で進められます（第2章で解説します）。

---

## サンプルコード

本書に出てくるプログラム（Python のプログラム、シェルスクリプト、ROS 2 のワークスペースなど）は、別のリポジトリで公開しています。

- https://github.com/trcp/erasers_book_code

## 章立て

### 第I部 Linux 入門

#### 第1章 コンピュータとは
- 1.1 コンピュータの構成要素（CPU・メモリ・ストレージ・GPU・入出力装置）
- 1.2 各部品が連携して動くしくみ
- 1.3 ハードウェアとソフトウェア（プログラム、アルゴリズム、順次・分岐・繰り返し、バグとデバッグ）
- 1.4 OS とは何か
- 1.5 ロボットに載っているコンピュータ

#### 第2章 Linux とは
- 2.1 Linux の歴史と UNIX 哲学
- 2.2 オープンソースソフトウェア（OSS）
- 2.3 ディストリビューション（Ubuntu, Debian, Fedora など）
- 2.4 なぜロボット開発で Linux が使われるのか
- 2.5 Ubuntu 環境の用意（VirtualBox で仮想マシンを作り、Ubuntu をインストールする。USB・ネットワークの設定）
- 2.6 デスクトップ環境の基本操作
- 2.7 最初の設定（ソフトウェアの更新、フォルダ名の英語化、Guest Additions）

#### 第3章 Linux の仕組み
- 3.1 カーネルとユーザ空間
- 3.2 ファイルシステムとディレクトリ構成（`/`, `/home`, `/etc`, `/usr`, `/opt` など）
- 3.3 ユーザとグループ、root 権限
- 3.4 プロセスとは
- 3.5 デバイスファイルと「すべてはファイル」という考え方

### 第II部 コマンドラインの基本

#### 第4章 ターミナルとシェル
- 4.1 GUI と CUI（CLI）
- 4.2 ターミナル・シェル・コマンドの関係
- 4.3 プロンプトの読み方
- 4.4 コマンドの構造（コマンド・オプション・引数）
- 4.5 ヘルプの調べ方（`--help`, `man`）
- 4.6 便利なキー操作（Tab 補完、履歴、`Ctrl+C` / `Ctrl+R` など）

#### 第5章 ファイルとディレクトリの操作
- 5.1 現在地の確認と移動（`pwd`, `cd`, `ls`）
- 5.2 絶対パスと相対パス、`~` と `.` / `..`
- 5.3 作成・コピー・移動・削除（`mkdir`, `touch`, `cp`, `mv`, `rm`）
- 5.4 ファイルの中身を見る（`cat`, `less`, `head`, `tail`）
- 5.5 ファイルを編集する（Ubuntu 標準のテキストエディター）
- 5.6 ファイルを探す（`find`, `locate`）
- 5.7 ワイルドカードとブレース展開

#### 第6章 パーミッションとユーザ管理
- 6.1 パーミッションの読み方（`rwx`）
- 6.2 `chmod`, `chown` の使い方
- 6.3 `sudo` と安全な権限の扱い方
- 6.4 デバイスへのアクセス権（`dialout` グループなど、ロボットで頻出の例）

#### 第7章 テキスト処理とパイプ
- 7.1 標準入力・標準出力・標準エラー出力
- 7.2 リダイレクト（`>`, `>>`, `2>`, `<`）
- 7.3 パイプ（`|`）でコマンドをつなぐ
- 7.4 検索と加工（`grep`, `sort`, `uniq`, `wc`, `cut`）
- 7.5 `sed` と `awk` の入門

#### 第8章 プロセスとシステム管理
- 8.1 プロセスの確認（`ps`, `top`, `htop`）
- 8.2 フォアグラウンドとバックグラウンド（`&`, `jobs`, `fg`, `bg`）
- 8.3 プロセスの終了（`kill`, `pkill`）とシグナル
- 8.4 ディスク・メモリの確認（`df`, `du`, `free`）
- 8.5 ログの確認（`journalctl`, `dmesg`）

#### 第9章 環境変数とシェルの設定
- 9.1 環境変数とは（`PATH`, `HOME` など）
- 9.2 `export` と `source`
- 9.3 `.bashrc` のカスタマイズ
- 9.4 エイリアスと関数

#### 第10章 シェルスクリプト入門
- 10.1 はじめてのシェルスクリプト（shebang と実行権限）
- 10.2 変数・引数・クォート
- 10.3 条件分岐とループ
- 10.4 終了ステータスとエラー処理
- 10.5 実践：開発環境セットアップスクリプトを書く

### 第III部 開発のための周辺ツール

#### 第11章 パッケージ管理
- 11.1 `apt` によるソフトウェアのインストール・更新・削除
- 11.2 リポジトリと GPG 鍵
- 11.3 ソースからのビルド（`make`, `cmake` の基礎）

#### 第12章 エディタ
- 12.1 エディタの選び方（テキストエディター以外の選択肢、本書では VS Code を標準にする）
- 12.2 nano
- 12.3 Vim（モードと最低限の操作）
- 12.4 Emacs
- 12.5 VS Code（インストール・画面の構成・拡張機能・リモート開発）

#### 第13章 Git によるバージョン管理
- 13.1 バージョン管理とは
- 13.2 基本操作（`init`, `add`, `commit`, `status`, `log`, `diff`）
- 13.3 ブランチとマージ
- 13.4 GitHub との連携（`clone`, `push`, `pull`, Pull Request）
- 13.5 チーム開発のワークフロー

#### 第14章 ネットワークとリモート操作
- 14.1 IP アドレスとホスト名の基礎
- 14.2 ネットワークの確認（`ip`, `ping`, `ss`）
- 14.3 SSH によるリモートログインと鍵認証
- 14.4 ファイル転送（`scp`, `rsync`）
- 14.5 `tmux` で複数ターミナルを管理する

#### 第15章 Docker 入門
- 15.1 コンテナとは
- 15.2 イメージとコンテナの操作
- 15.3 Dockerfile の書き方
- 15.4 GUI アプリやデバイスをコンテナで使う
- 15.5 Docker Compose と Dev Containers（ROS 2 をコンテナで使う方法は補章1）

### 第IV部 Python 入門

#### 第16章 Python とは
- 16.1 コンパイラ型とインタプリタ型
- 16.2 C 言語と比べてみる
- 16.3 Python の特徴
- 16.4 メリットとデメリット
- 16.5 Python のバージョン

#### 第17章 Python の開発環境
- 17.1 プログラムの実行方法
- 17.2 pip によるパッケージのインストール
- 17.3 Ubuntu 24.04 での注意点（PEP 668）
- 17.4 venv による仮想環境

#### 第18章 Python の基本
- 18.1 数値と計算（四則演算、コメント）
- 18.2 変数とデータ型（名前の付け方のコラム、文字列、型の変換、f 文字列、input）
- 18.3 リスト・タプル・辞書
- 18.4 条件分岐（if 文、比較演算子、論理演算子、None）
- 18.5 繰り返し（for 文、while 文、break / continue、リスト内包表記、乱数）
- 18.6 関数

#### 第19章 クラスとモジュール
- 19.1 クラスとオブジェクト
- 19.2 継承
- 19.3 関数を渡す（コールバック）
- 19.4 モジュールと import（`if __name__ == "__main__":`）
- 19.5 例外処理（try / except / finally、Ctrl+C）
- 19.6 読みやすいコードを書く（PEP 8・フォーマッタ・型ヒント）
- 19.7 デバッグの基本（練習問題の最終課題：自由製作）

### 第V部 ROS 2 入門

#### 第20章 ROS とは
- 20.1 ロボットソフトウェアの構成要素
- 20.2 ROS の歴史と ROS 1 / ROS 2 の違い
- 20.3 ROS 2 のアーキテクチャと DDS
- 20.4 ディストリビューションとサポート期間

#### 第21章 ROS 2 のインストールと環境構築
- 21.1 ROS 2 Jazzy のインストール
- 21.2 環境のセットアップ（`source /opt/ros/jazzy/setup.bash`）
- 21.3 turtlesim で動作確認
- 21.4 `ROS_DOMAIN_ID` とネットワーク設定

#### 第22章 ROS 2 の基本概念とコマンドラインツール
- 22.1 ノード（`ros2 node`）
- 22.2 トピック（`ros2 topic`）とメッセージ型（`ros2 interface`）
- 22.3 サービス（`ros2 service`）
- 22.4 アクション（`ros2 action`）
- 22.5 パラメータ（`ros2 param`）
- 22.6 `rqt` と `rqt_graph` による可視化

#### 第23章 ワークスペースとパッケージ
- 23.1 ワークスペースの構成（`src`, `build`, `install`, `log`）
- 23.2 `colcon` によるビルド
- 23.3 パッケージの作成（`ros2 pkg create`）
- 23.4 `package.xml` と `setup.py` / `CMakeLists.txt`
- 23.5 依存関係の解決（`rosdep`）
- 23.6 オーバーレイとアンダーレイ

#### 第24章 Python でノードを書く
- 24.1 はじめてのノード（`rclpy` の基本）
- 24.2 パブリッシャとサブスクライバ
- 24.3 タイマとコールバック
- 24.4 サービスサーバとクライアント
- 24.5 アクションサーバとクライアント
- 24.6 パラメータの宣言と利用
- 24.7 カスタムメッセージ・サービスの定義
- 24.8 （コラム）C++ で書く場合（`rclcpp`）（詳しくは補章2）

#### 第25章 launch と設定ファイル
- 25.1 launch ファイルとは
- 25.2 Python launch ファイルの書き方
- 25.3 YAML によるパラメータ設定
- 25.4 名前空間とリマップ
- 25.5 複数ノードをまとめて起動する（launch 引数、インクルード）
- 25.6 （コラム）XML の launch ファイル（詳しくは補章3）

#### 第26章 座標変換と可視化
- 26.1 ロボットにおける座標系
- 26.2 tf2 の仕組み（`static_transform_publisher`, `tf2_ros`）
- 26.3 URDF によるロボットモデルの記述
- 26.4 `robot_state_publisher` と `joint_state_publisher`
- 26.5 RViz2 の使い方

#### 第27章 シミュレーション
- 27.1 Gazebo の概要
- 27.2 Gazebo と ROS 2 の連携（`ros_gz_bridge`）
- 27.3 移動ロボットをシミュレーションで動かす
- 27.4 センサ（LiDAR・カメラ・IMU）のシミュレーション

#### 第28章 データの記録とデバッグ
- 28.1 rosbag2 による記録と再生
- 28.2 ログ出力とログレベル
- 28.3 よくあるトラブルと対処法（ノードが見えない、トピックが届かない等）
- 28.4 QoS 設定の基礎

#### 第29章 実践：移動ロボットを動かす
- 29.1 キーボードでロボットを操作する（`teleop_twist_keyboard`）
- 29.2 センサデータを読んで障害物を避けるノードを作る
- 29.3 SLAM による地図作成の体験（`slam_toolbox`）
- 29.4 Navigation2 による自律移動の体験
- 29.5 次のステップへ

#### 第30章 実践：カチャカを動かす
- 30.1 カチャカとは（Preferred Robotics 社の家庭用ロボット、kachaka API、erasers_kachaka）
- 30.2 パソコンとつなぐ（ネットワーク、IP アドレス、`ping`）
- 30.3 erasers_kachaka を用意する（ビルド、環境変数）
- 30.4 起動して RViz2 で見る
- 30.5 カチャカを動かす（`ros2 topic pub`、teleop_twist_keyboard）
- 30.6 カチャカに話させる
- 30.7 カメラの画像を見る（cv_bridge、OpenCV）
- 30.8 LiDAR のデータを読む（カチャカの LiDAR の向き）
- 30.9 障害物を避けて走らせる（第29章のノードを実機で動かす）

### 補章

本編の章の内容を、別の書き方などで補う章です（付録は早見表・用語集などの資料）。

- 補章1 Docker で ROS 2 の開発環境を作る（第15章の Docker と第21章以降の ROS 2 を組み合わせる）
- 補章2 C++ でノードを書く（rclcpp）（第24章のノードを C++ で書き直す）
- 補章3 XML による launch ファイルの書き方（第25章の launch ファイルを XML で書き直す）

### 付録

- 付録A コマンド早見表（Linux / Git / ROS 2）
- 付録B よく使うキーボードショートカット
- 付録C Python の練習問題の解答例（第18章・第19章）
- 付録D トラブルシューティング集
- 付録E 用語集
- 付録F 参考文献・オンラインリソース

---

## リポジトリ構成

```
.
├── README.md              # このファイル
├── check_list.md          # 確認事項リスト（動作確認・事実確認・未執筆箇所など）
├── Dockerfile             # 執筆用の Docker イメージ（TeX Live・Emacs・Claude Code・tmux）
├── compose.yaml           # 執筆用コンテナの設定
├── docker/                # 執筆用の tmux セッションの起動スクリプト
├── .github/
│   └── workflows/
│       └── build-pdf.yml  # PDF の自動ビルドと Releases への公開
│   ├── python/            # 第IV部の Python のプログラムと練習問題の解答例
│   ├── shellscript/       # シェルスクリプト
│   ├── cmake_hello/       # CMake の例
│   ├── docker/            # Docker の例
│   └── ros2_ws/           # ROS 2 のワークスペース（src/ に my_package・my_interfaces・my_cpp_package）
└── book/                  # 原稿一式
    ├── main.tex           # 本全体の構成（部・章の読み込み順）
    ├── preamble.tex       # パッケージ読み込み・囲み環境・共通マクロ
    ├── .latexmkrc         # latexmk の設定（LuaLaTeX, 出力先 build/）
    ├── Makefile
    ├── frontmatter/       # はじめに・おわりに・執筆者一覧
    ├── chapters/          # 各章の原稿
    │   ├── _template.tex  # 執筆用サンプル（環境・マクロの使用例）
    │   ├── linux/         # 第I部 Linux 入門
    │   ├── commandline/   # 第II部 コマンドラインの基本
    │   ├── tools/         # 第III部 開発のための周辺ツール
    │   ├── python/        # 第IV部 Python 入門
    │   └── ros2/          # 第V部 ROS 2 入門
    ├── supplement/        # 補章
    ├── appendix/          # 付録
    ├── samples/           # \codefile で読み込むサンプル（ROS 2 のパッケージ・スクリプト）
    └── images/            # 図版（章ごとにサブディレクトリ）
```

以降の説明に出てくる原稿のパス（`main.tex`, `chapters/...`, `images/...` など）は、すべて `book/` からの相対パスです。

## ビルド方法

LuaLaTeX（jlreq クラス）でビルドします。TeX Live が必要です。
`book/` ディレクトリに移動してから `make` を実行してください（`.latexmkrc` が `book/` にあるため、他のディレクトリから `latexmk` を実行すると設定が読み込まれません）。

```bash
cd book
make          # build/main.pdf を生成
make watch    # ファイルの変更を監視して自動で再ビルド
make clean    # 生成物を削除
```

特定の章だけを確認したいときは、`main.tex` の先頭に `\includeonly{chapters/ros2/rclpy}` のように書くと、その章だけを組版できます。

### Docker の中で執筆する

TeX Live・Emacs・Claude Code・tmux・Git が入った執筆用の Docker イメージを用意しています。
Docker（Docker Compose）があれば、手元に TeX Live などをインストールしなくても、コンテナの中で原稿の編集からビルド、`git push` まで行えます。
TeX Live は GitHub Actions と同じイメージを使うので、手元と CI で組版結果がそろいます。
リポジトリの一番上のディレクトリで、次のコマンドを実行します。

```bash
docker compose up -d dev            # 執筆用のコンテナを起動する（初回はイメージを作るので時間がかかる）
docker compose exec dev dev-tmux    # tmux のセッションに入る
docker compose down                 # コンテナを止めて削除する
```

`dev-tmux` を実行すると、次の 3 つのウィンドウを持つ tmux のセッション `book` に入ります。
セッションから離れる（プレフィックスキー → `d`）と、コンテナの中でセッションが動き続け、次に `dev-tmux` を実行したときに続きから作業できます。

| ウィンドウ | 内容 |
| --- | --- |
| 1: emacs | `book/` を開いた Emacs |
| 2: claude | リポジトリの一番上で起動した Claude Code |
| 3: build | 原稿を保存するたびに自動でビルドし直す `latexmk -pvc`（PDF は `book/build/main.pdf`） |

ウィンドウはプレフィックスキー → 数字キーで切り替えられます（プレフィックスキーは、下のとおりホストの `~/.tmux.conf` の設定に従います。標準では `Ctrl+B`）。
PDF は、ホストの PDF ビューアで `book/build/main.pdf` を開いておくと、ビルドのたびに再読み込みされます。

ホストの次のファイルを、コンテナの中から使えるようにしています（`compose.yaml` の `dev` を参照）。

| ホスト | 用途 |
| --- | --- |
| SSH エージェント（`$SSH_AUTH_SOCK`） | `git push` のときの SSH の認証（パスフレーズ付きの鍵もそのまま使える） |
| `~/.ssh`（読み取り専用） | SSH の鍵・`known_hosts`・設定 |
| `~/.gitconfig`（読み取り専用） | コミットに記録する名前やメールアドレス |
| `~/.tmux.conf`（読み取り専用） | tmux の設定（プレフィックスキーなど） |
| `~/.claude`, `~/.claude.json` | Claude Code の認証情報と設定（ホストでログイン済みなら、コンテナの中でログインし直す必要はない） |

- 生成されるファイルの所有者がホストのユーザになるよう、コンテナの中の作業用ユーザ（元のイメージにいる `texlive`）の UID と GID をホストに合わせています。自分の UID（`id -u` で確認できます）が 1000 でない場合は、`export UID GID=$(id -g)` を実行してから `docker compose up -d dev` を実行してください。
- マウントするファイル（`~/.claude.json`, `~/.gitconfig`, `~/.tmux.conf`）がホストにないと、Docker が同じ名前のディレクトリを作ってしまいます。`~/.claude.json` は先にホストで Claude Code にログインしておけば作られます。ほかのファイルは、使っていなければ `touch ~/.tmux.conf` のように空のファイルを作っておいてください。
- Claude Code の会話の履歴やメモリは、作業しているディレクトリのパスごとに分かれて保存されます。コンテナの中のパス（`/workspace`）はホストのパスと違うので、ホストの Claude Code とは別のプロジェクトとして扱われます。
- Emacs の設定（`~/.emacs.d`）もホストと共有したい場合は、`compose.yaml` のコメントを外してください。ホストとコンテナで Emacs のバージョンが違うと、パッケージが動かないことがあります。
- Claude Code と Emacs は、イメージを作ったときの最新版が入ります。更新するときは `docker compose build --no-cache dev` でイメージを作り直します。

PDF をビルドするだけなら、Emacs などを起動せずに次のコマンドでも実行できます。

```bash
docker compose run --rm pdf         # 1 回だけビルドする
docker compose up watch             # 原稿を保存するたびに自動でビルドし直す（Ctrl+C で終了）
```

### 最新版 PDF

`master` ブランチに push されると、GitHub Actions が自動で PDF をビルドし、Releases の `latest` に置きます。
最新の PDF は次の URL からダウンロードできます。

<https://github.com/trcp/erasers_book/releases/download/latest/erasers_book.pdf>

### バージョンを付けた PDF

`v` から始まるタグ（例：`v1.0.0`）を push すると、そのタグのコミットから PDF をビルドし、タグと同じ名前の Release に `erasers_book-v1.0.0.pdf` として置きます。

```bash
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0
```

表紙と奥付の「版」には、タグ名（例：`v1.0.0`）が入ります。
タグの付いていないコミットからビルドした PDF では「開発版」と表示され、奥付にはビルドしたコミットの番号が入ります。
版の情報は `.latexmkrc` がビルドのたびに `build/bookinfo.tex` に書き出します（環境変数 `BOOK_VERSION`、`BOOK_COMMIT` で上書きできます）。

同じタグで作り直したいときは、タグを付け直して `git push -f origin v1.0.0` で push すると、Release も作り直されます。

`draft` ブランチへの push と Pull Request では、PDF のビルドだけを行い、Releases には置きません。
ビルドに失敗した PR はマージしないでください。
生成された PDF は、リポジトリの Actions タブで該当する実行結果を開き、Artifacts の `pdf` からダウンロードできます（zip 形式、GitHub へのログインが必要、保存期間は最長 90 日）。

## 章とファイルの対応

| 章 | タイトル | ファイル |
| --- | --- | --- |
| 1 | コンピュータとは | `chapters/linux/computer.tex` |
| 2 | Linux とは | `chapters/linux/what_is_linux.tex` |
| 3 | Linux の仕組み | `chapters/linux/linux_internals.tex` |
| 4 | ターミナルとシェル | `chapters/commandline/terminal_shell.tex` |
| 5 | ファイルとディレクトリの操作 | `chapters/commandline/files.tex` |
| 6 | パーミッションとユーザ管理 | `chapters/commandline/permission.tex` |
| 7 | テキスト処理とパイプ | `chapters/commandline/text_pipe.tex` |
| 8 | プロセスとシステム管理 | `chapters/commandline/process.tex` |
| 9 | 環境変数とシェルの設定 | `chapters/commandline/env.tex` |
| 10 | シェルスクリプト入門 | `chapters/commandline/shellscript.tex` |
| 11 | パッケージ管理 | `chapters/tools/package.tex` |
| 12 | エディタ | `chapters/tools/editor.tex` |
| 13 | Git によるバージョン管理 | `chapters/tools/git.tex` |
| 14 | ネットワークとリモート操作 | `chapters/tools/network.tex` |
| 15 | Docker 入門 | `chapters/tools/docker.tex` |
| 16 | Python とは | `chapters/python/what_is_python.tex` |
| 17 | Python の開発環境 | `chapters/python/python_env.tex` |
| 18 | Python の基本 | `chapters/python/python_basics.tex` |
| 19 | クラスとモジュール | `chapters/python/python_class.tex` |
| 20 | ROS とは | `chapters/ros2/what_is_ros.tex` |
| 21 | ROS 2 のインストールと環境構築 | `chapters/ros2/ros2_install.tex` |
| 22 | ROS 2 の基本概念とコマンドラインツール | `chapters/ros2/ros2_concepts.tex` |
| 23 | ワークスペースとパッケージ | `chapters/ros2/workspace.tex` |
| 24 | Python でノードを書く | `chapters/ros2/rclpy.tex` |
| 25 | launch と設定ファイル | `chapters/ros2/launch.tex` |
| 26 | 座標変換と可視化 | `chapters/ros2/tf_viz.tex` |
| 27 | シミュレーション | `chapters/ros2/simulation.tex` |
| 28 | データの記録とデバッグ | `chapters/ros2/debug.tex` |
| 29 | 実践：移動ロボットを動かす | `chapters/ros2/practice.tex` |
| 30 | 実践：カチャカを動かす | `chapters/ros2/kachaka.tex` |
| 補章1 | Docker で ROS 2 の開発環境を作る | `supplement/docker_ros.tex` |
| 補章2 | C++ でノードを書く（rclcpp） | `supplement/rclcpp.tex` |
| 補章3 | XML による launch ファイルの書き方 | `supplement/launch_xml.tex` |
| 付録A | コマンド早見表 | `appendix/cheatsheet.tex` |
| 付録B | よく使うキーボードショートカット | `appendix/shortcuts.tex` |
| 付録C | Python の練習問題の解答例 | `appendix/python_answers.tex` |
| 付録D | トラブルシューティング集 | `appendix/troubleshooting.tex` |
| 付録E | 用語集 | `appendix/glossary.tex` |
| 付録F | 参考文献・オンラインリソース | `appendix/references.tex` |
| — | はじめに / おわりに | `frontmatter/preface.tex` / `frontmatter/afterword.tex` |
| — | 執筆者一覧 | `frontmatter/contributors.tex` |
| — | 奥付 | `frontmatter/colophon.tex` |

章の追加・削除・順番の入れ替えは `main.tex` の `\include` を編集して行います。
章番号は LaTeX が自動で振るので、ファイル名やディレクトリ名（`images/` のサブディレクトリを含む）には章番号を付けず、章の内容を表す名前を使ってください。
こうしておけば、章の順番を入れ替えてもファイル名を変更する必要がありません。
本文中で章や図を参照するときも、番号を直接書かずに `\ref` を使います。

---

## 執筆ルール

複数人で執筆するためのルール（作業の進め方、使用する環境・マクロ、図版、ラベル、文体と用語など）は [writing_rules.md](writing_rules.md) にまとめています。執筆を始める前に必ず読んでください。

## 誤りの報告

誤字脱字・内容の誤り・わかりにくい箇所などがあれば、Issue または Pull Request でお知らせください。
