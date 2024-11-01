import os
import sys
from pathlib import Path

from src.webansi import ansi_to_html
from templete_apply import templete_apply

print(f"{'-' * os.get_terminal_size().columns}")
for i in sys.path:
    print(i)
print(f"{'-' * os.get_terminal_size().columns}")

ansi = Path('test', 'test_file', 'test1.txt').read_text(encoding='utf-8')
html = templete_apply(ansi_to_html(ansi, style=True, debug=True))
Path("test", "test_file", "test1.html").write_text(html, encoding="utf-8")


ansi = Path('test', 'test_file', 'test2.txt').read_text(encoding='utf-8')
html = templete_apply(ansi_to_html(ansi, style=True, debug=True))
Path("test", "test_file", "test2.html").write_text(html, encoding="utf-8")
