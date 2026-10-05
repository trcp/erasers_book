$pdf_mode = 4;  # lualatex
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 %O %S';
$max_repeat = 5;
$out_dir = 'build';

# \include したファイルの .aux を書けるよう build/ 以下にサブディレクトリを作る
use File::Path qw(make_path);
make_path(map { "$out_dir/$_" } qw(
  frontmatter appendix supplement
  chapters/linux chapters/commandline
  chapters/tools chapters/python chapters/ros2
));

# 表紙と奥付に入れる版の情報を build/bookinfo.tex に書き出す
#   BOOK_VERSION: 環境変数があればそれを、なければ HEAD に付いたタグを使う（空なら「開発版」）
#                 タグがあれば、サンプルコードのリンクも erasers_book_code の同じタグを指す
#   BOOK_COMMIT : 環境変数があればそれを、なければ HEAD のコミットを使う（先頭 7 文字）
# 中身が変わったときだけ書き換えるので、版が変わると latexmk が再ビルドする
{
  my $version = $ENV{BOOK_VERSION} // `git describe --tags --exact-match 2>/dev/null`;
  my $commit  = $ENV{BOOK_COMMIT}  || `git rev-parse HEAD 2>/dev/null`;
  chomp($version, $commit);
  $commit = substr($commit, 0, 7);
  my $info = '';
  if ($version ne '') {
    $info .= "\\renewcommand{\\bookversion}{\\detokenize{$version}}\n";
    # サンプルコードのリポジトリも、同じ名前のタグを指すリンクにする
    $info .= "\\booktaggedtrue\n";
    $info .= "\\renewcommand{\\codeurl}{\\url{https://github.com/trcp/erasers_book_code/tree/$version}}\n";
  }
  $info .= "\\renewcommand{\\bookcommit}{\\detokenize{$commit}}\n"   if $commit  ne '';
  my $file = "$out_dir/bookinfo.tex";
  my $old = '';
  if (open(my $in, '<', $file)) { local $/; $old = <$in>; close $in; }
  if ($old ne $info) { open(my $outf, '>', $file) or die; print $outf $info; close $outf; }
}
