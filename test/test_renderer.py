
from pathlib import Path
from colorsys import hsv_to_rgb

from src._text_renderer import text_renderer
from src._text_renderer import _ansi_fun
from templete_apply import templete_apply




ansi = Path('test', 'test_file', 'test1.txt').read_text(encoding='utf-8')


# test font

_ansi_fun.m(0)
html = text_renderer('111\n')
_ansi_fun.m(1)
html += text_renderer('222\n')
_ansi_fun.m(3)
html += text_renderer('333\n')
_ansi_fun.m(92)
_ansi_fun.m(4)
html += text_renderer('444\n')
html += 'no apply style\n'


# color test

_ansi_fun.m(0)


# 4bit color

for i in range(8):
    _ansi_fun.m(40 + i)
    html += text_renderer('   ')
html += '\n'
for i in range(8):
    _ansi_fun.m(100 + i)
    html += text_renderer('   ')
html += '\n'


# xterm 8bit color

for i in range(16):
    if not i % 8:
        html += '\n'
    _ansi_fun.m(48, 5, i)
    html += text_renderer('   ')
html += '\n'


for i in range(16, 256):
    if not (i - 16) % 36:
        html += '\n'
    _ansi_fun.m(48, 5, i)
    html += text_renderer(' ')
html += '\n'


# RGB 24bit color

for i in range(600):
    if not i % 40:
        html += '\n'
    i = i * (1 / 600)
    _ansi_fun.m(48, 2, *(f * 255 for f in hsv_to_rgb(i, 1, 1)))
    html += text_renderer(' ')


html = templete_apply(html)
Path('test', 'test_file', 'renderer.html').write_text(html, encoding='utf-8')
