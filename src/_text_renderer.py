'''
满满的设计因素
全靠CSS
'''

from pathlib import Path

from . import _ansi_fun




def text_renderer(s: str, debug: bool=False) -> str:
    if debug: print('text_renderer() start.')

    tag_s = '<span style="'

    if _ansi_fun.bold_enable:
        tag_s += 'font-weight: bold; '
    if _ansi_fun.italic_enable:
        tag_s += 'font-style: italic; '
    if _ansi_fun.underline_enable:
        tag_s += 'text-decoration: underline; '
    if _ansi_fun.color_active_foreground != 'inherit':
        tag_s += f'color: rgb({_ansi_fun.color_active_foreground[0]}, {_ansi_fun.color_active_foreground[1]}, {_ansi_fun.color_active_foreground[2]}); '
    else:
        tag_s += 'color: inherit; ' # empty style
    if _ansi_fun.color_active_background != 'inherit':
        tag_s += f'background-color: rgb({_ansi_fun.color_active_background[0]}, {_ansi_fun.color_active_background[1]}, {_ansi_fun.color_active_background[2]}); '

    if debug: print('text_renderer() done.')

    return tag_s + f'">{s}</span>'
