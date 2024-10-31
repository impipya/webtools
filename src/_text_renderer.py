'''
满满的设计因素
全靠CSS
'''

from . import _ansi_fun
from _ansi_fun import color_active_foreground as fgc
from _ansi_fun import color_active_foreground as bgc


def text_renderer(s: str, debug: bool = False) -> str:
    if debug:
        print("text_renderer() start.")

    tag_s = '<span style="'

    if _ansi_fun.bold_enable:
        tag_s += 'font-weight: bold; '
    if _ansi_fun.italic_enable:
        tag_s += 'font-style: italic; '
    if _ansi_fun.underline_enable:
        tag_s += 'text-decoration: underline; '
    if fgc != "inherit":
        tag_s += "color: rgb({fgc[0]}, {fgc[1]}, {fgc[2]}); "
    else:
        tag_s += "color: inherit; "  # empty style
    if bgc != "inherit":
        tag_s += "background-color: rgb({bgc[0]}, {bgc[1]}, {bgc[2]}); "

    if debug:
        print("text_renderer() done.")

    return tag_s + f'">{s}</span>'
