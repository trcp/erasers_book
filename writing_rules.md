# 執筆ルール

本書の原稿（`book/`）を書くときのルールです。本の概要・章立て・ビルドの方法は [README.md](README.md) を、確認が必要な項目は [check_list.md](check_list.md) を見てください。

複数人で執筆するため、以下のルールに従ってください。迷ったときは `chapters/_template.tex` を参照してください。

## 作業の進め方（Git）

1. 担当する章を決めたら、Issue を立てて自分をアサインします（同じ章を複数人が同時に編集しないため）。
2. `master` から作業用ブランチを切ります。ブランチ名は `<章のファイル名>-<内容>` とします（例：`rclpy-publisher`, `cheatsheet-git`）。
3. `make` でエラーなくビルドできることを確認してからコミットします。
4. Pull Request を作成し、**最低 1 人のレビュー**を受けてから `master` にマージします。
5. コミットメッセージの先頭に対象の章を書きます（例：`rclpy: パブリッシャの節を執筆`）。

次のファイルは全員に影響するため、変更する場合は事前に Issue で相談してください。

- `preamble.tex`（パッケージ・環境・マクロの追加や変更）
- `main.tex`（章構成の変更）
- `.latexmkrc`, `Makefile`
- `.github/workflows/build-pdf.yml`（リポジトリ直下）

## ファイルの書き方

- **1 文ごとに改行**してください。差分が見やすくなり、レビューやコンフリクト解消が楽になります（LaTeX では空行を入れない限り段落は分かれません）。
- 段落を分けるときは空行を 1 行入れます。`\\` による改行は使いません。
- 各章の冒頭には `goalbox`（この章で学ぶこと）を、末尾には「この章のまとめ」を必ず書きます。
- 書きかけの箇所には `\todo{内容}` を残してください。PDF 上で赤字表示されるので未完成箇所がすぐわかります。
- 見出しは `\chapter` / `\section` / `\subsection` までとし、`\subsubsection` 以下はなるべく使いません。

## 使用する環境・マクロ

`preamble.tex` で定義している以下の環境・マクロを使い、独自の装飾（`\textcolor` や `\fbox` の直書きなど）は避けてください。

| 用途 | 書き方 |
| --- | --- |
| ターミナル操作例 | `\begin{terminal}[タイトル] ... \end{terminal}` |
| 表示例（読者が入力しない例） | `\begin{termexample}[タイトル] $ kill <PID> \end{termexample}`（紺色のタイトルバー・点線の枠で、タイトルの先頭に「例：」が付く） |
| ソースコード | `\begin{codelisting}[style=python]{キャプション}{lst:ラベル} ... \end{codelisting}`（ページをまたぐと「（次のページに続く）」「（前のページから続く）」が表示される） |
| 外部ファイルのコード | `\codefile[style=python]{キャプション}{lst:ラベル}{samples/rclpy/my_package/my_package/foo.py}`（`firstline=`・`lastline=` なども `[ ]` に書ける） |
| キャプションのない短いコード | `\begin{lstlisting}[style=python, numbers=none, xleftmargin=0pt, framexleftmargin=0pt] ... \end{lstlisting}`（コラムや注意などの囲みの中で使う） |
| この章で学ぶこと | `\begin{goalbox} ... \end{goalbox}` |
| ポイント | `\begin{point}[タイトル] ... \end{point}`（タイトル省略時は「ポイント」） |
| 注意 | `\begin{caution}[タイトル] ... \end{caution}`（タイトル省略時は「注意」） |
| コラム | `\begin{column}{タイトル} ... \end{column}` |
| TIPS | `\begin{tips}{タイトル} ... \end{tips}`（本筋とは別の、すぐに役立つ実践的なアドバイス。コラムは読み物・背景知識に使う） |
| 本文中の表 | `\begin{tablebox}[キャプション][tab:ラベル] \begin{tabular}{ll} ... \end{tabular} \end{tablebox}`（前後に余白が空き、表の上に「表 5.1 キャプション」が付く。キャプションと表は同じページに置かれる） |
| 練習問題 | `\begin{exercise} \begin{enumerate} \item ... \end{enumerate} \end{exercise}`（章ごとに「練習問題 18.1」と番号が付き、中の問題は (1), (2), ... になる。解答例は付録「Python の練習問題の解答例」（`appendix/python_answers.tex`）に章ごとの節としてまとめ、「練習問題 18.1 (2)」のように参照する） |
| 文中のコマンド・ファイル名 | `\cmd{ls -l}` |
| キー入力 | `\key{Ctrl}+\key{C}` |
| 未完成箇所 | `\todo{あとで図を追加}` |

`codelisting`・`\codefile`・`lstlisting` の `style` には `python`, `bash`, `cpp`, `xml` が使えます。
本文のソースコードは、キャプションとラベルを付けて `codelisting` か `\codefile` で書きます。`\end{codelisting}` は行の先頭に書いてください。
ソースコードの枠・TIPS・練習問題は、ページの残りが少ないときは自動で次のページに送られ、ページをまたいだときは「続く」の表示が付きます。

> **注意：見出しの直後の表**
> `\section` や `\subsection` の直後に、文章を挟まずに表（`tabular`）を置くとビルドエラーになります。見出しと表の間には、必ず 1 文以上の本文を入れてください。

> **注意：`terminal` 環境のタイトル**
> タイトルを省略した `terminal` 環境で、1 行目に日本語が含まれているとビルドエラーになります。
> 1 行目に日本語を書くときは、`\begin{terminal}[コマンドの基本形]` のように必ずタイトルを付けてください。
> また、タイトルが長すぎると右上のボタンと重なります。タイトルは全角 20 文字程度までにしてください。
> タイトルの中の `_` `&` `%` `#` などの記号は、`\cmd{}` と同じようにエスケープしてください（例：`[ROS\_DOMAIN\_ID を設定する]`）。

> **注意：`\cmd{}` 内の特殊文字**
> `\cmd{}` の中では `_ # $ % & { } ~` をエスケープする必要があります（例：`\cmd{ros2\_ws}`）。
> 本文中でエスケープが面倒な場合は `\lstinline|ros2_ws|` を使えます。ただし `\lstinline` は見出し（`\section` など）の中では使えないので、見出しでは `\cmd{}` とエスケープを使ってください。

## コマンド例の書き方

- 本文の流れどおりに読者が入力して、同じ結果になるコマンドは `terminal` で書きます。そのために必要なファイルやディレクトリは、先に作る手順も書いておきます（第5章以降の練習は `~/practice` の中で行う）。
- 次のようなものは `termexample`（表示例）で書きます。
  - まだ作っていないファイルや、つながっていない機器（`/dev/ttyUSB0` など）、ほかのコンピュータ（ロボットの PC など）を使う例
  - 実行すると困ることがある例（`kill` で動いているプログラムを止めるなど）
  - `<PID>` のような書式を説明するための例、後の章で実行する手順の先取り
- ROS 2 は第21章でインストールします。それより前の章では、ROS 2 のコマンドやファイル（`ros2`、`/opt/ros/...`、`~/ros2_ws`）を `terminal` で実行させないでください。ROS 2 での使い方を紹介したいときは、本文の説明か `termexample` にします。
- 実行結果のユーザ名は `user`、ホスト名は `robot` にそろえます（「はじめに」で読み替えを説明しています）。
- `cd` でディレクトリを移動した後のコマンドは、プロンプトの `$` の前に今いるディレクトリを書きます（`~/practice$ ls` のように。ホームディレクトリは `~`）。同じ章の中では、前の枠で `cd` した場所が続いているものとして書きます。`cd` していない（ターミナルを開いたまま）のコマンドは `$` だけにします。
- 別のターミナル（2 つ目のターミナルなど）で実行するコマンドや、表示例（`termexample`）、TIPS などの囲みの中の枠には、パスを付けません。

- `terminal` 環境の中では、一般ユーザで実行するコマンドの先頭に `$ `、root 権限で実行するコマンドの先頭に `# ` を付けます。
- `terminal` 環境は Ubuntu のターミナル風の枠で表示され、`$` から行末まで（入力するコマンド）が自動で太字になります。実行結果の行に `$` が含まれると、そこから行末までも太字になるので注意してください。
- 実行結果は `$` を付けずにそのまま書きます。長い出力は途中を `...` で省略して構いません。
- 読者が自分の環境に合わせて置き換える部分は `<ファイル名>` のように山括弧で囲みます。
- コマンドに説明を添えるときは、行末に `# 説明` の形でコメントを書きます（例：`$ cd ~/Documents     # ホームの Documents に移動`）。
- 実行結果とエラーメッセージは英語の表示で掲載します（日本語環境では日本語で表示されることを、第4章で断っています）。
- プロンプトを含めて書く必要があるときは、ユーザ名を `user`、ホスト名を `robot` とします（例：`user@robot:~$`）。
- 掲載するコマンドとコードは、必ず**動作環境（Ubuntu 24.04 + ROS 2 Jazzy）で実際に実行して確認**してください。

## ラベルと相互参照

ラベルには種類を表す接頭辞を付け、`\ref` で参照します。「上の図」「次のリスト」のような位置に依存した書き方は避けてください。

| 対象 | 接頭辞 | 例 |
| --- | --- | --- |
| 章 | `chap:` | `\label{chap:rclpy}` |
| 節 | `sec:` | `\label{sec:rclpy-publisher}` |
| 図 | `fig:` | `\label{fig:rqt-graph}` |
| 表 | `tab:` | `\label{tab:apt-commands}` |
| コード | `lst:` | `\label{lst:minimal-node}` |
| 補章 | `sup:` | `\label{sup:launch-xml}` |
| 付録 | `app:` | `\label{app:cheatsheet}` |

補章は `main.tex` の `\hoshou` の後に `\include` します（補章と付録は、第V部の中に入らないように、それぞれ番号なしの部「補章」「付録」の後に置いています）。見出しは「補章1」、節・図・表・コードの番号は「補1.1」のようになり、本文からは `補章\ref{sup:launch-xml}` のように参照します。

ラベルは本全体で一意になるよう、節以下のラベルには章を表す語を含めてください（例：`sec:rclpy-publisher`）。

## 図版

- 画像は、章のファイル名と同じ名前のディレクトリ `images/<章のファイル名>/` に置きます（例：`ros2_concepts.tex` の図なら `images/ros2_concepts/rqt_graph.png`）。`\includegraphics{ros2_concepts/rqt_graph.png}` のように `images/` を省略して参照できます。
- ファイル名は半角英数字・ハイフン・アンダースコアのみとし、日本語や空白は使いません。
- スクリーンショットは PNG を使います。
- 図（ブロック図・流れ図・状態遷移図・木構造など）は、なるべく TikZ で描きます（次の「TikZ で描く図」を参照）。TikZ で描きにくい図は、PDF か、SVG から変換した PDF を使います。
- 図には必ず `\caption` と `\label` を付け、本文から `\ref` で参照します。
- 外部から引用する図は出典とライセンスを確認し、キャプションに出典を明記してください。

### TikZ で描く図

TikZ で描く図は、図ごとに `images/<章のファイル名>/<図の名前>.tex` というファイルに `tikzpicture` 環境だけを書き、本文からは `\input` で読み込みます。
図の中身を別ファイルにすることで、本文の差分が読みやすくなり、図だけを修正・レビューしやすくなります。

```latex
\begin{figure}[tb]
  \centering
  \input{images/terminal_shell/terminal_shell_command}
  \caption{ターミナル・シェル・コマンドの関係}
  \label{fig:terminal-shell-command}
\end{figure}
```

- `\input` では `\includegraphics` と違って `images/` を省略できないので、`images/` から書きます。
- 図の幅は本文の幅（A4 で約 155 mm）に収めます。これまでの図は横幅 10 cm 程度で描いているので、それに合わせると見た目がそろいます。
- 見た目をそろえるため、`preamble.tex` で定義している次のスタイルを使います。

| スタイル | 用途 |
| --- | --- |
| `figbox` | 枠付きの箱（白地） |
| `figpart` | 主役となる箱（薄い青地） |
| `figarrow` | 矢印 |
| `figlabel` | 矢印や箱に添える小さな説明文 |
| `fignum` | 丸囲みの番号（`\tikz\node[fignum]{1};` のように使う） |

- 状態遷移図には `automata` ライブラリ、配置には `positioning` ライブラリなどが使えます（`preamble.tex` で読み込み済み）。
- 既存の図（`images/computer/flow.tex` など）を参考にしてください。

### 画像がまだないときのプレースホルダ

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
  % \includegraphics[width=0.8\linewidth]{terminal_shell/terminal_window.png}
  \caption{Ubuntu のターミナル}
  \label{fig:terminal-window}
\end{figure}
```

- `%% 入れる画像：` の行に、どのような画像が必要かを具体的に書きます。
- `\includegraphics` の行には、置く予定のファイル名を書いておきます。
- プレースホルダの段階でも `\caption` と `\label` を付け、本文から `\ref` で参照しておきます。
- 画像ができたら `images/<章のファイル名>/` に置き、`tikzpicture` 環境を削除して `\includegraphics` の行のコメントを外します。
- TikZ で描く場合は、プレースホルダの `tikzpicture` 環境とコメントを消して、`\input{images/<章のファイル名>/<図の名前>}` に置き換えます。

プレースホルダが残っている箇所は、`grep -rn '入れる画像' book/` で一覧できます。

## サンプルコード

- 本文で扱う ROS 2 パッケージやスクリプトは `book/samples/` に置き（ROS 2 のパッケージは `samples/rclpy/`・`samples/rclcpp/`）、実際にビルド・実行できる状態に保ちます。
- 長いコードは本文に直接書かず、`\codefile` で `samples/` から読み込みます。これにより本文とサンプルコードの食い違いを防ぎます。本のリポジトリだけでビルドできるように、`book/` の外のファイルは読み込まないでください。
- 読者向けのサンプルコードは、別のリポジトリ https://github.com/trcp/erasers_book_code で公開しています（ROS 2 のパッケージは `ros2_ws/src/`、本文に直接書いた短いプログラムは `python/` など）。`book/samples/` や本文のプログラムを直したときは、そちらのリポジトリも合わせて直してください。
- Python コードは PEP 8 に従ってください。

## 文体と用語

- 文体は「です・ます」調で統一します。
- 句読点は「、」「。」を使います（「，」「．」は使いません）。
- 和文と半角英数字の間には半角スペースを入れます（例：「Linux の仕組み」「ROS 2 を使う」）。
- 数字・英字・記号は半角を使います。
- カタカナ語の語末の長音は省略します（例：ユーザ、サーバ、コンピュータ、パブリッシャ、サブスクライバ）。
- 用語は以下のように統一します。新しい用語を導入したら付録E（用語集）にも追加してください。

| 使う表記 | 使わない表記 |
| --- | --- |
| ディレクトリ | フォルダ |
| ターミナル | 端末、コンソール（Ubuntu のアプリ名「端末」を指す場合を除く） |
| CLI | CUI（第4章で両者を紹介する箇所を除く） |
| ROS 2 | ROS2、ros2（コマンド名を除く） |
| ノード / トピック / サービス / アクション | node / topic などの英語表記 |
| パッケージ | pkg |
| Ubuntu 24.04 | Ubuntu24.04、ubuntu |
