
import re

from . import _ansi_fun
from ._text_inserter import *
from ._text_renderer import *
from ._html_tools import *




def ansi_to_html(text: str, style: bool=True, debug=False) -> str:
    '''translate ansi code to html code'''

    # init
    _ansi_fun.screen_buffer = []
    _ansi_fun.cursor_pos_x = 0
    _ansi_fun.cursor_pos_y = 0

    text = html_mark_escape(text)

    # print(text)
    for row in text.split('\n'):
        _ansi_fun.screen_buffer.append('')
        for i, cstp in enumerate(row.split('^[[')):
            # 给行首文字接续style
            if i == 0 : # first must have not CS, so directly writo to file
                if cstp != '':
                    t = cstp
                else:
                    t = ''
            else:
                pattern_cs = re.compile(r'^.*?[ABCDEFGHJKSTlmsu]')
                if pfp := pattern_cs.search(cstp):
                    pfp: str = pfp.group(0)

                    f = pfp[-1]

                    p = pfp[:-1].split(';')

                    if p == ['']:
                        eval(f'_ansi_fun.{f}()')

                    else:
                        lbd = lambda s: int(s) if s != '' else 0
                        p = [lbd(s.strip('?')) for s in p]          # TODO Some 临时性处理 直接忽略带?的属性

                        if debug:
                            if f in 'EFGHJKSTlsu':
                                print(p, f)

                        eval(f'_ansi_fun.{f}(*p)')

                pattern_t = re.compile(r'(?<=[lmABCD]).*$')
                if t := pattern_t.search(cstp):
                    t = t.group(0)
                else:
                    t = ''

            if t != '': # 空文字不做动
                _ansi_fun.screen_buffer[_ansi_fun.cursor_pos_y] = text_insterer(_ansi_fun.screen_buffer[_ansi_fun.cursor_pos_y], _ansi_fun.cursor_pos_x, text_renderer(t))
                pattern_tag = re.compile(r'&lt|&gt')
                _, tag_num = pattern_tag.subn('', t)
                _ansi_fun.cursor_pos_x += len(t) - tag_num * 2

        # line break(CRLF)
        _ansi_fun.cursor_pos_x = 0
        _ansi_fun.cursor_pos_y += 1

    text = '\n'.join(_ansi_fun.screen_buffer).strip('\n')

    if not style:
        pattern_elements = re.compile(r'<.*?>')
        text = pattern_elements.sub('', text)
        pattern_lg = re.compile(r'&lt')
        pattern_gt = re.compile(r'&gt')
        text = pattern_lg.sub('<', text)
        text = pattern_gt.sub('>', text)

    return text
