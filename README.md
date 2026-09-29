# これを読めばあなたもロボットを動かせるようになる！

**〜ロボット初学者のための Linux・コマンドライン・ROS 入門〜**

ロボット開発をこれから始める人に向けた入門書です。
Linux とは何かというところから始め、コマンドラインの基本操作、開発に必要な周辺ツール、
そして ROS 2 を使ったロボットソフトウェア開発の基礎までを、順を追って学べるように構成しています。

## 対象読者

- ロボット開発に興味があるが、Linux をほとんど触ったことがない人
- 研究室やロボットチームに配属され、ROS を使う必要が出てきた人
- Windows / macOS の GUI 操作には慣れているが、ターミナル操作に不安がある人

プログラミング経験は必須ではありませんが、Python の基本文法（変数・条件分岐・関数・クラス）を知っていると後半の ROS の章がスムーズに読めます。

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
| OS | Ubuntu 24.04 LTS |
| ROS | ROS 2 Jazzy Jalisco |
| 言語 | Python 3.12（一部 C++） |
| シミュレータ | Gazebo (Harmonic) |

> Windows / macOS を使っている場合は、デュアルブート・仮想マシン・WSL2・Docker のいずれかで Ubuntu 環境を用意してください（第1章で解説します）。

---

## 章立て

### 第I部 Linux 入門

#### 第1章 Linux とは
- 1.1 OS とは何か
- 1.2 Linux の歴史と UNIX 哲学
- 1.3 オープンソースソフトウェア（OSS）
- 1.4 ディストリビューション（Ubuntu, Debian, Fedora など）
- 1.5 なぜロボット開発で Linux が使われるのか
- 1.6 Ubuntu 環境の用意（インストール / 仮想マシン / WSL2 / Docker）
- 1.7 デスクトップ環境の基本操作

#### 第2章 Linux の仕組み
- 2.1 カーネルとユーザ空間
- 2.2 ファイルシステムとディレクトリ構成（`/`, `/home`, `/etc`, `/usr`, `/opt` など）
- 2.3 ユーザとグループ、root 権限
- 2.4 プロセスとは
- 2.5 デバイスファイルと「すべてはファイル」という考え方

### 第II部 コマンドラインの基本

#### 第3章 ターミナルとシェル
- 3.1 GUI と CUI（CLI）
- 3.2 ターミナル・シェル・コマンドの関係
- 3.3 プロンプトの読み方
- 3.4 コマンドの構造（コマンド・オプション・引数）
- 3.5 ヘルプの調べ方（`--help`, `man`, `tldr`）
- 3.6 便利なキー操作（Tab 補完、履歴、`Ctrl+C` / `Ctrl+R` など）

#### 第4章 ファイルとディレクトリの操作
- 4.1 現在地の確認と移動（`pwd`, `cd`, `ls`）
- 4.2 絶対パスと相対パス、`~` と `.` / `..`
- 4.3 作成・コピー・移動・削除（`mkdir`, `touch`, `cp`, `mv`, `rm`）
- 4.4 ファイルの中身を見る（`cat`, `less`, `head`, `tail`）
- 4.5 ファイルを探す（`find`, `locate`）
- 4.6 ワイルドカードとブレース展開

#### 第5章 パーミッションとユーザ管理
- 5.1 パーミッションの読み方（`rwx`）
- 5.2 `chmod`, `chown` の使い方
- 5.3 `sudo` と安全な権限の扱い方
- 5.4 デバイスへのアクセス権（`dialout` グループなど、ロボットで頻出の例）

#### 第6章 テキスト処理とパイプ
- 6.1 標準入力・標準出力・標準エラー出力
- 6.2 リダイレクト（`>`, `>>`, `2>`, `<`）
- 6.3 パイプ（`|`）でコマンドをつなぐ
- 6.4 検索と加工（`grep`, `sort`, `uniq`, `wc`, `cut`）
- 6.5 `sed` と `awk` の入門

#### 第7章 プロセスとシステム管理
- 7.1 プロセスの確認（`ps`, `top`, `htop`）
- 7.2 フォアグラウンドとバックグラウンド（`&`, `jobs`, `fg`, `bg`）
- 7.3 プロセスの終了（`kill`, `pkill`）とシグナル
- 7.4 ディスク・メモリの確認（`df`, `du`, `free`）
- 7.5 ログの確認（`journalctl`, `dmesg`）

#### 第8章 パッケージ管理
- 8.1 `apt` によるソフトウェアのインストール・更新・削除
- 8.2 リポジトリと GPG 鍵
- 8.3 `pip` と Python 仮想環境（`venv`）
- 8.4 ソースからのビルド（`make`, `cmake` の基礎）

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

#### 第11章 エディタ
- 11.1 ターミナルエディタ（`nano`, `vim` の最低限の操作）
- 11.2 VS Code のセットアップと拡張機能
- 11.3 リモート開発（Remote-SSH / Dev Containers）

#### 第12章 Git によるバージョン管理
- 12.1 バージョン管理とは
- 12.2 基本操作（`init`, `add`, `commit`, `status`, `log`, `diff`）
- 12.3 ブランチとマージ
- 12.4 GitHub との連携（`clone`, `push`, `pull`, Pull Request）
- 12.5 チーム開発のワークフロー

#### 第13章 ネットワークとリモート操作
- 13.1 IP アドレスとホスト名の基礎
- 13.2 ネットワークの確認（`ip`, `ping`, `ss`）
- 13.3 SSH によるリモートログインと鍵認証
- 13.4 ファイル転送（`scp`, `rsync`）
- 13.5 `tmux` で複数ターミナルを管理する

#### 第14章 Docker 入門
- 14.1 コンテナとは
- 14.2 イメージとコンテナの操作
- 14.3 Dockerfile の書き方
- 14.4 GUI アプリやデバイスをコンテナで使う
- 14.5 ROS 開発環境をコンテナで構築する

### 第IV部 ROS 2 入門

#### 第15章 ROS とは
- 15.1 ロボットソフトウェアの構成要素
- 15.2 ROS の歴史と ROS 1 / ROS 2 の違い
- 15.3 ROS 2 のアーキテクチャと DDS
- 15.4 ディストリビューションとサポート期間

#### 第16章 ROS 2 のインストールと環境構築
- 16.1 ROS 2 Jazzy のインストール
- 16.2 環境のセットアップ（`source /opt/ros/jazzy/setup.bash`）
- 16.3 turtlesim で動作確認
- 16.4 `ROS_DOMAIN_ID` とネットワーク設定

#### 第17章 ROS 2 の基本概念とコマンドラインツール
- 17.1 ノード（`ros2 node`）
- 17.2 トピック（`ros2 topic`）とメッセージ型（`ros2 interface`）
- 17.3 サービス（`ros2 service`）
- 17.4 アクション（`ros2 action`）
- 17.5 パラメータ（`ros2 param`）
- 17.6 `rqt` と `rqt_graph` による可視化

#### 第18章 ワークスペースとパッケージ
- 18.1 ワークスペースの構成（`src`, `build`, `install`, `log`）
- 18.2 `colcon` によるビルド
- 18.3 パッケージの作成（`ros2 pkg create`）
- 18.4 `package.xml` と `setup.py` / `CMakeLists.txt`
- 18.5 依存関係の解決（`rosdep`）
- 18.6 オーバーレイとアンダーレイ

#### 第19章 Python でノードを書く
- 19.1 はじめてのノード（`rclpy` の基本）
- 19.2 パブリッシャとサブスクライバ
- 19.3 タイマとコールバック
- 19.4 サービスサーバとクライアント
- 19.5 アクションサーバとクライアント
- 19.6 パラメータの宣言と利用
- 19.7 カスタムメッセージ・サービスの定義
- 19.8 （コラム）C++ で書く場合（`rclcpp`）

#### 第20章 launch と設定ファイル
- 20.1 launch ファイルとは
- 20.2 Python launch ファイルの書き方
- 20.3 YAML によるパラメータ設定
- 20.4 名前空間とリマップ
- 20.5 複数ノードをまとめて起動する

#### 第21章 座標変換と可視化
- 21.1 ロボットにおける座標系
- 21.2 tf2 の仕組み（`static_transform_publisher`, `tf2_ros`）
- 21.3 URDF によるロボットモデルの記述
- 21.4 `robot_state_publisher` と `joint_state_publisher`
- 21.5 RViz2 の使い方

#### 第22章 シミュレーション
- 22.1 Gazebo の概要
- 22.2 Gazebo と ROS 2 の連携（`ros_gz_bridge`）
- 22.3 移動ロボットをシミュレーションで動かす
- 22.4 センサ（LiDAR・カメラ・IMU）のシミュレーション

#### 第23章 データの記録とデバッグ
- 23.1 rosbag2 による記録と再生
- 23.2 ログ出力とログレベル
- 23.3 よくあるトラブルと対処法（ノードが見えない、トピックが届かない等）
- 23.4 QoS 設定の基礎

#### 第24章 実践：移動ロボットを動かす
- 24.1 キーボードでロボットを操作する（`teleop_twist_keyboard`）
- 24.2 センサデータを読んで障害物を避けるノードを作る
- 24.3 SLAM による地図作成の体験（`slam_toolbox`）
- 24.4 Navigation2 による自律移動の体験
- 24.5 次のステップへ

### 付録

- 付録A コマンド早見表（Linux / Git / ROS 2）
- 付録B よく使うキーボードショートカット
- 付録C トラブルシューティング集
- 付録D 用語集
- 付録E 参考文献・オンラインリソース

---

## リポジトリ構成

```
.
├── README.md              # このファイル
├── .github/
│   └── workflows/
│       └── build-pdf.yml  # PDF の自動ビルドと Releases への公開
└── book/                  # 原稿一式
    ├── main.tex           # 本全体の構成（部・章の読み込み順）
    ├── preamble.tex       # パッケージ読み込み・囲み環境・共通マクロ
    ├── .latexmkrc         # latexmk の設定（LuaLaTeX, 出力先 build/）
    ├── Makefile
    ├── frontmatter/       # はじめに・おわりに
    ├── chapters/          # 各章の原稿
    │   ├── _template.tex  # 執筆用サンプル（環境・マクロの使用例）
    │   ├── part1_linux/
    │   ├── part2_commandline/
    │   ├── part3_tools/
    │   └── part4_ros2/
    ├── appendix/          # 付録
    ├── samples/           # 各章のサンプルコード・ROS 2 パッケージ
    └── images/            # 図版
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

特定の章だけを確認したいときは、`main.tex` の先頭に `\includeonly{chapters/part4_ros2/ch19_rclpy}` のように書くと、その章だけを組版できます。

### 最新版 PDF

`master` ブランチに push されると、GitHub Actions が自動で PDF をビルドし、Releases の `latest` に置きます。
最新の PDF は次の URL からダウンロードできます。

<https://github.com/trcp/erasers_book/releases/download/latest/erasers_book.pdf>

Pull Request では PDF のビルドだけを行います。
ビルドに失敗した PR はマージしないでください。
生成された PDF は、その PR の Actions の実行結果ページ（Artifacts の `pdf`）からダウンロードできます。

## 章とファイルの対応

| 章 | タイトル | ファイル |
| --- | --- | --- |
| 1 | Linux とは | `chapters/part1_linux/ch01_what_is_linux.tex` |
| 2 | Linux の仕組み | `chapters/part1_linux/ch02_linux_internals.tex` |
| 3 | ターミナルとシェル | `chapters/part2_commandline/ch03_terminal_shell.tex` |
| 4 | ファイルとディレクトリの操作 | `chapters/part2_commandline/ch04_files.tex` |
| 5 | パーミッションとユーザ管理 | `chapters/part2_commandline/ch05_permission.tex` |
| 6 | テキスト処理とパイプ | `chapters/part2_commandline/ch06_text_pipe.tex` |
| 7 | プロセスとシステム管理 | `chapters/part2_commandline/ch07_process.tex` |
| 8 | パッケージ管理 | `chapters/part2_commandline/ch08_package.tex` |
| 9 | 環境変数とシェルの設定 | `chapters/part2_commandline/ch09_env.tex` |
| 10 | シェルスクリプト入門 | `chapters/part2_commandline/ch10_shellscript.tex` |
| 11 | エディタ | `chapters/part3_tools/ch11_editor.tex` |
| 12 | Git によるバージョン管理 | `chapters/part3_tools/ch12_git.tex` |
| 13 | ネットワークとリモート操作 | `chapters/part3_tools/ch13_network.tex` |
| 14 | Docker 入門 | `chapters/part3_tools/ch14_docker.tex` |
| 15 | ROS とは | `chapters/part4_ros2/ch15_what_is_ros.tex` |
| 16 | ROS 2 のインストールと環境構築 | `chapters/part4_ros2/ch16_ros2_install.tex` |
| 17 | ROS 2 の基本概念とコマンドラインツール | `chapters/part4_ros2/ch17_ros2_concepts.tex` |
| 18 | ワークスペースとパッケージ | `chapters/part4_ros2/ch18_workspace.tex` |
| 19 | Python でノードを書く | `chapters/part4_ros2/ch19_rclpy.tex` |
| 20 | launch と設定ファイル | `chapters/part4_ros2/ch20_launch.tex` |
| 21 | 座標変換と可視化 | `chapters/part4_ros2/ch21_tf_viz.tex` |
| 22 | シミュレーション | `chapters/part4_ros2/ch22_simulation.tex` |
| 23 | データの記録とデバッグ | `chapters/part4_ros2/ch23_debug.tex` |
| 24 | 実践：移動ロボットを動かす | `chapters/part4_ros2/ch24_practice.tex` |
| 付録A | コマンド早見表 | `appendix/appA_cheatsheet.tex` |
| 付録B | よく使うキーボードショートカット | `appendix/appB_shortcuts.tex` |
| 付録C | トラブルシューティング集 | `appendix/appC_troubleshooting.tex` |
| 付録D | 用語集 | `appendix/appD_glossary.tex` |
| 付録E | 参考文献・オンラインリソース | `appendix/appE_references.tex` |
| — | はじめに / おわりに | `frontmatter/preface.tex` / `frontmatter/afterword.tex` |

章の追加・削除・順番の入れ替えは `main.tex` の `\include` を編集して行います。

---

## 執筆ルール

複数人で執筆するため、以下のルールに従ってください。迷ったときは `chapters/_template.tex` を参照してください。

### 作業の進め方（Git）

1. 担当する章を決めたら、Issue を立てて自分をアサインします（同じ章を複数人が同時に編集しないため）。
2. `master` から作業用ブランチを切ります。ブランチ名は `chXX-<内容>` とします（例：`ch19-publisher`, `appA-cheatsheet`）。
3. `make` でエラーなくビルドできることを確認してからコミットします。
4. Pull Request を作成し、**最低 1 人のレビュー**を受けてから `master` にマージします。
5. コミットメッセージの先頭に対象の章を書きます（例：`ch19: パブリッシャの節を執筆`）。

次のファイルは全員に影響するため、変更する場合は事前に Issue で相談してください。

- `preamble.tex`（パッケージ・環境・マクロの追加や変更）
- `main.tex`（章構成の変更）
- `.latexmkrc`, `Makefile`
- `.github/workflows/build-pdf.yml`（リポジトリ直下）

### ファイルの書き方

- **1 文ごとに改行**してください。差分が見やすくなり、レビューやコンフリクト解消が楽になります（LaTeX では空行を入れない限り段落は分かれません）。
- 段落を分けるときは空行を 1 行入れます。`\\` による改行は使いません。
- 各章の冒頭には `goalbox`（この章で学ぶこと）を、末尾には「この章のまとめ」を必ず書きます。
- 書きかけの箇所には `\todo{内容}` を残してください。PDF 上で赤字表示されるので未完成箇所がすぐわかります。
- 見出しは `\chapter` / `\section` / `\subsection` までとし、`\subsubsection` 以下はなるべく使いません。

### 使用する環境・マクロ

`preamble.tex` で定義している以下の環境・マクロを使い、独自の装飾（`\textcolor` や `\fbox` の直書きなど）は避けてください。

| 用途 | 書き方 |
| --- | --- |
| ターミナル操作例 | `\begin{terminal}[タイトル] ... \end{terminal}` |
| ソースコード | `\begin{lstlisting}[style=python, caption={...}, label={lst:...}] ... \end{lstlisting}` |
| 外部ファイルのコード | `\lstinputlisting[style=python]{samples/chXX/foo.py}` |
| この章で学ぶこと | `\begin{goalbox} ... \end{goalbox}` |
| ポイント | `\begin{point}[タイトル] ... \end{point}`（タイトル省略時は「ポイント」） |
| 注意 | `\begin{caution}[タイトル] ... \end{caution}`（タイトル省略時は「注意」） |
| コラム | `\begin{column}{タイトル} ... \end{column}` |
| 文中のコマンド・ファイル名 | `\cmd{ls -l}` |
| キー入力 | `\key{Ctrl}+\key{C}` |
| 未完成箇所 | `\todo{あとで図を追加}` |

`lstlisting` の `style` には `python`, `bash`, `cpp`, `xml` が使えます。

> **注意：`terminal` 環境のタイトル**
> タイトルを省略した `terminal` 環境で、1 行目に日本語が含まれているとビルドエラーになります。
> 1 行目に日本語を書くときは、`\begin{terminal}[コマンドの基本形]` のように必ずタイトルを付けてください。

> **注意：`\cmd{}` 内の特殊文字**
> `\cmd{}` の中では `_ # $ % & { } ~` をエスケープする必要があります（例：`\cmd{ros2\_ws}`）。
> 本文中でエスケープが面倒な場合は `\lstinline|ros2_ws|` を使えます。ただし `\lstinline` は見出し（`\section` など）の中では使えないので、見出しでは `\cmd{}` とエスケープを使ってください。

### コマンド例の書き方

- `terminal` 環境の中では、一般ユーザで実行するコマンドの先頭に `$ `、root 権限で実行するコマンドの先頭に `# ` を付けます。
- 実行結果は `$` を付けずにそのまま書きます。長い出力は途中を `...` で省略して構いません。
- 読者が自分の環境に合わせて置き換える部分は `<ファイル名>` のように山括弧で囲みます。
- コマンドに説明を添えるときは、行末に `# 説明` の形でコメントを書きます（例：`$ cd ~/Documents     # ホームの Documents に移動`）。
- 実行結果とエラーメッセージは英語の表示で掲載します（日本語環境では日本語で表示されることを、第3章で断っています）。
- プロンプトを含めて書く必要があるときは、ユーザ名を `user`、ホスト名を `robot` とします（例：`user@robot:~$`）。
- 掲載するコマンドとコードは、必ず**動作環境（Ubuntu 24.04 + ROS 2 Jazzy）で実際に実行して確認**してください。

### ラベルと相互参照

ラベルには種類を表す接頭辞を付け、`\ref` で参照します。「上の図」「次のリスト」のような位置に依存した書き方は避けてください。

| 対象 | 接頭辞 | 例 |
| --- | --- | --- |
| 章 | `chap:` | `\label{chap:rclpy}` |
| 節 | `sec:` | `\label{sec:rclpy-publisher}` |
| 図 | `fig:` | `\label{fig:rqt-graph}` |
| 表 | `tab:` | `\label{tab:apt-commands}` |
| コード | `lst:` | `\label{lst:minimal-node}` |
| 付録 | `app:` | `\label{app:cheatsheet}` |

ラベルは本全体で一意になるよう、節以下のラベルには章を表す語を含めてください（例：`sec:rclpy-publisher`）。

### 図版

- 画像は `images/chXX/` に置きます（例：`images/ch17/rqt_graph.png`）。`\includegraphics{ch17/rqt_graph.png}` のように `images/` を省略して参照できます。
- ファイル名は半角英数字・ハイフン・アンダースコアのみとし、日本語や空白は使いません。
- スクリーンショットは PNG、図は可能な限り PDF か SVG から変換した PDF を使います。
- 図には必ず `\caption` と `\label` を付け、本文から `\ref` で参照します。
- 外部から引用する図は出典とライセンスを確認し、キャプションに出典を明記してください。

#### 画像がまだないときのプレースホルダ

画像を入れたい場所が決まっていても、まだ画像が用意できていないときは、次の形式でプレースホルダを入れておきます。
PDF 上には「Sample」と書かれた枠が表示されます（TikZ は `preamble.tex` で読み込み済みです）。

```latex
\begin{figure}[tb]
  \centering
  \large
  \begin{tikzpicture}
    \draw rectangle++(4.5,3);
    \clip rectangle++(4.5,3);
    \foreach\x in{0,1,2,3,4}{
      \foreach\y in{0,1,2,3,4,5,6}{
        \path(\x*1.5-\y*0.5,\y*0.6)node[rotate=10,text=gray]{\sffamily\bfseries\itshape Sample };
      }
    }
  \end{tikzpicture}
  %% 入れる画像：ターミナルを起動した直後のウィンドウのスクリーンショット
  % eps 画像を貼る場合は includegraphics をお使いください。
  % \includegraphics[width=0.8\linewidth]{ch03/terminal_window.png}
  \caption{Ubuntu のターミナル}
  \label{fig:terminal-window}
\end{figure}
```

- `%% 入れる画像：` の行に、どのような画像が必要かを具体的に書きます。
- `\includegraphics` の行には、置く予定のファイル名を書いておきます。
- プレースホルダの段階でも `\caption` と `\label` を付け、本文から `\ref` で参照しておきます。
- 画像ができたら `images/chXX/` に置き、`tikzpicture` 環境を削除して `\includegraphics` の行のコメントを外します。

プレースホルダが残っている箇所は、`grep -rn '入れる画像' book/` で一覧できます。

### サンプルコード

- 本文で扱う ROS 2 パッケージやスクリプトは `samples/chXX/` に置き、実際にビルド・実行できる状態に保ちます。
- 長いコードは本文に直接書かず、`\lstinputlisting` で `samples/` から読み込みます。これにより本文とサンプルコードの食い違いを防ぎます。
- Python コードは PEP 8 に従ってください。

### 文体と用語

- 文体は「です・ます」調で統一します。
- 句読点は「、」「。」を使います（「，」「．」は使いません）。
- 和文と半角英数字の間には半角スペースを入れます（例：「Linux の仕組み」「ROS 2 を使う」）。
- 数字・英字・記号は半角を使います。
- カタカナ語の語末の長音は省略します（例：ユーザ、サーバ、コンピュータ、パブリッシャ、サブスクライバ）。
- 用語は以下のように統一します。新しい用語を導入したら付録D（用語集）にも追加してください。

| 使う表記 | 使わない表記 |
| --- | --- |
| ディレクトリ | フォルダ |
| ターミナル | 端末、コンソール（Ubuntu のアプリ名「端末」を指す場合を除く） |
| CLI | CUI（第3章で両者を紹介する箇所を除く） |
| ROS 2 | ROS2、ros2（コマンド名を除く） |
| ノード / トピック / サービス / アクション | node / topic などの英語表記 |
| パッケージ | pkg |
| Ubuntu 24.04 | Ubuntu24.04、ubuntu |

## 誤りの報告

誤字脱字・内容の誤り・わかりにくい箇所などがあれば、Issue または Pull Request でお知らせください。
