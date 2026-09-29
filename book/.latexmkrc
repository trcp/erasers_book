$pdf_mode = 4;  # lualatex
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 %O %S';
$max_repeat = 5;
$out_dir = 'build';

# \include したファイルの .aux を書けるよう build/ 以下にサブディレクトリを作る
use File::Path qw(make_path);
make_path(map { "$out_dir/$_" } qw(
  frontmatter appendix
  chapters/part1_linux chapters/part2_commandline
  chapters/part3_tools chapters/part4_ros2
));
