'''
bold和bright，历史
是由于单色终端和8bit伪色终端并存导致的
bright方式在mobaxterm以256色显示竟然无效!!!

---

还有 充满魔法和空白 2呢
5-29

38 5
38 2

现在还没有校验值是否有效

上下 右 左 为什么 右 左

几乎 only for fetch了
网页不是终端 终端现在几乎我只输出fetch彩色最多了 一些TUI应用的输出可以捕捉吗

或者 网页加入光标 真正会闪烁的光标 成为终端 但远不是编辑器
终端可以接收编辑器的行为
'''

import sys
from enum import Enum, auto

from info_print import info_print

from ._palette_4bit import palette_4bit
from ._palette_8bit import palette_8bit
from ._palette_default import palette_default


class Bold(Enum):
    NONE = auto()
    BOLD = auto()
    BRIGHT = auto()
    BOTH = auto()


# manual config
config_bold_method = Bold.BOTH
config_color_active_foreground_default = palette_default[0]
config_color_active_background_default = palette_default[0]
config_palette_4bit_replace_8bit = True


# m default apply DO NOT EDIT
bold_enable = False
italic_enable = False
underline_enable = False
color_active_foreground = config_color_active_foreground_default
color_active_background = config_color_active_background_default


# A, B, C, D apply DO NOT EDIT
screen_buffer = []  # screen_buffer
cursor_pos_x = 0
cursor_pos_y = 0
last_cursor_pos_x = 0
last_cursor_pos_y = 0


if config_palette_4bit_replace_8bit:
    for i in range(16):
        palette_8bit[i] = palette_4bit[i]


def m(p1: int = None, p2: int = None, p3=None, p4=None, p5=None):

    global bold_enable
    global italic_enable
    global underline_enable
    global color_active_foreground
    global color_active_background

    if p1 == 0 or p1 is None:
        bold_enable = False
        italic_enable = False
        underline_enable = False
        color_active_foreground = config_color_active_foreground_default
        color_active_background = config_color_active_background_default
    elif p1 == 1:
        match config_bold_method:
            case Bold.NONE:
                pass
            case Bold.BOLD:
                bold_enable = True
            case Bold.BRIGHT:
                # When enable [palette_4bit_replace_8bit], the coloer could be
                # any color in the palette_4bit, so need limited the range.
                if color_active_foreground in palette_4bit[:8]:
                    color_active_foreground = palette_4bit[
                        palette_4bit.index(color_active_foreground) + 8
                    ]
                else:
                    pass  # TODO initial bright 8bit bright
            case Bold.BOTH:
                bold_enable = True
                if color_active_foreground in palette_4bit[:8]:
                    color_active_foreground = palette_4bit[
                        palette_4bit.index(color_active_foreground) + 8
                    ]
                else:
                    pass # TODO initial bright 8bit bright
    elif p1 == 3:
        italic_enable = True
    elif p1 == 4:
        underline_enable = True
    elif 30 <= p1 <= 37:
        color_active_foreground = palette_4bit[p1 - 30]
    elif p1 == 38:
        if p2 == 5:
            color_active_foreground = palette_8bit[p3]
        elif p2 == 2:
            color_active_foreground = (p3, p4, p5)
        else:
            info_print('e', f'Invalid parameter p2 --> {p2}.')
            sys.exit()
    elif 40 <= p1 <= 47:
            color_active_background = palette_4bit[p1 - 40]
    elif p1 == 48:
        if p2 == 5:
            color_active_background = palette_8bit[p3]
        elif p2 == 2:
            color_active_background = (p3, p4, p5)
        else:
            info_print('e', f'Invalid parameter p2 --> {p2}.')
            sys.exit()
    elif 90 <= p1 <= 97:
        color_active_foreground = palette_4bit[p1 - 90 + 8]
    elif 100 <= p1 <= 107:
        color_active_background = palette_4bit[p1 - 100 + 8]
    else:
        info_print('e', f'Invalid parameter p2 --> {p1}.')
        sys.exit()




def A(p1: int=1):
    global cursor_pos_y
    cursor_pos_y -= p1
    if cursor_pos_y < 0:
        cursor_pos_y = 0
    # print(f'{cursor_pos_y=}')




def B(p1: int=1):
    global cursor_pos_y
    cursor_pos_y += p1
    # print(f'{cursor_pos_y=}')




def C(p1: int=1):
    global cursor_pos_x
    cursor_pos_x += p1
    # print(f'{cursor_pos_x=}')




def D(p1: int=1):
    global cursor_pos_x
    cursor_pos_x -= p1
    if cursor_pos_x < 0:
        cursor_pos_x = 0
    # print(f'{cursor_pos_x=}')




def E(p1: int=1):
    global cursor_pos_y
    global cursor_pos_x
    cursor_pos_y += p1
    cursor_pos_x = 0




def F(p1: int=1):
    global cursor_pos_y
    global cursor_pos_x
    cursor_pos_y -= p1
    if cursor_pos_y < 0:
        cursor_pos_y = 0
    cursor_pos_x = 0




def G(p1: int=1):
    global cursor_pos_x
    cursor_pos_x = p1 - 1




def H(p1: int=1, p2: int=1):
    global cursor_pos_y
    global cursor_pos_x
    cursor_pos_y = p1 - 1
    cursor_pos_x = p2 - 1




def J(p1: int=0):
    global cursor_pos_y
    global cursor_pos_x

    match p1:
        case 0:
            screen_buffer[cursor_pos_y:-1] = ''
        case 1:
            screen_buffer[:cursor_pos_y] = ''
        case 2:
            screen_buffer[:cursor_pos_y] = ['']




def K(p1: int=0):
    global cursor_pos_y
    global cursor_pos_x

    match p1:
        case 0:
            screen_buffer[cursor_pos_y][cursor_pos_x:-1] = '</span>'
        case 1:
            realPos = cursor_pos_x
            flag_remove = True
            for c in screen_buffer[cursor_pos_y]:
                if c == '>':
                    flag_remove = False
                if c == '<':
                    flag_remove = True
                elif flag_remove:
                    screen_buffer[cursor_pos_y] = screen_buffer[cursor_pos_y][:realPos] + screen_buffer[cursor_pos_y][realPos + 1:]
                realPos -= 1
        case 2:
            screen_buffer[cursor_pos_y] = ['']




def S(p1: int=1):
    global cursor_pos_y
    global cursor_pos_x

    for _ in range(p1):
        screen_buffer.append([''])





def T(p1: int=1):
    global cursor_pos_y
    global cursor_pos_x

    for _ in range(p1):
        screen_buffer.insert(0, [''])




def s():
    global cursor_pos_y
    global cursor_pos_x
    global last_cursor_pos_y
    global last_cursor_pos_x

    last_cursor_pos_y = cursor_pos_y
    last_cursor_pos_x = cursor_pos_x




def u():
    global cursor_pos_y
    global cursor_pos_x
    global last_cursor_pos_y
    global last_cursor_pos_x

    cursor_pos_y = last_cursor_pos_y
    cursor_pos_x = last_cursor_pos_x




def l(*p):
    pass

