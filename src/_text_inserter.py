""" text_insert.py
touch: 10/29 加入样式隔离

elif!!!!!!!

尾随空格绝对不影响输出

不能将lastOpenTag清空移动到右括号, 在到达下一个左括号之前都是要可取值的
"""




def text_insterer(text: str, pos: int, insert: str, debug: bool=False) -> str:
    """不受HTML标签影响, 将文本插入指定的位置
    ### param
    - text: 被插入文本
    - pos: 插入的位置
    - insert: 插入的文本
    - debug: 带颜色打印输出结果
    ### note
    - 插入文本最好不要是空字符串, 会导致产生多余的样式隔离标签
    - 产生样式隔离标签的条件
        - 光标经过了一个开标签, 并且没有遇到闭标签(即last_open_tag为真), 且光标不在标签的边缘
    """

    _e_counter = 0

    cursorPos = -1      # 初始还没有完成第一次检测, 所以光标位置为-1
    realPos = -1        # 初始还没有完成第一次检测, 所以光标位置为-1
    lastOpenTag = ''    # 用于产生样式隔离标签

    flag_cursorInOpenTag = False
    flag_cursorInTag = False
    flag_inOut = False

    while True:

        realPos += 1

        try:
            # 都是离散的, 只会进入其中一个, 不用进行多次判断, 要尽快跳出

            if text[realPos] == '<':
                flag_cursorInTag = True
                if text[realPos + 1] != '/':
                    flag_cursorInOpenTag = True
                    lastOpenTag = ''

            elif text[realPos] == '>':
                flag_cursorInTag = False
                flag_cursorInOpenTag = False

            elif not flag_cursorInTag:
                if text[realPos:realPos+3] == '&gt' or text[realPos:realPos+3] == '&lt':
                    cursorPos -= 2
                cursorPos += 1 # 当检测不在标签内时, cursorPos和realPos同步

            elif flag_cursorInOpenTag:
                lastOpenTag += text[realPos]

        except IndexError:
            _e_counter += 1
            if _e_counter >= 100:
                import sys
                import _ansi_fun
                print(f'{_ansi_fun.cursor_pos_y=}')
                print(f'{_ansi_fun.cursor_pos_x=}')
                print(f'{text=}')
                print('text_insterer()错误')
                sys.exit(1)

            placeholder = '.' if debug else ' '

            text += placeholder
            cursorPos += 1
            flag_inOut = True

        if cursorPos == pos:

            if not flag_inOut:

                # 左边缘检测, 只会出现左边缘, 因为
                if text[realPos - 1] == '>':
                    while True:
                        realPos -= 1
                        if text[realPos] == '<':
                            # 在光标的左侧插入
                            if debug: insert = f'\033[31m{insert}\033[0m'
                            return f'{text[:realPos]}{insert}{text[realPos:]}'
                else:
                    print('样式隔离start')
                    # 在光标的左侧插入
                    insert = f'</span>{insert}<{lastOpenTag}>'
                    if debug: insert = f'\033[31m{insert}\033[0m'
                    return f'{text[:realPos]}{insert}{text[realPos:]}'

            else:
                if debug: insert = f'\033[31m{insert}\033[0m'
                return f'{text[:realPos]}{insert}{text[realPos:]}'.rstrip(placeholder)




if __name__ =='__main__':
    test_text = '<span style="background-color: rgb(255, 111, 0);">5678</span><span style="background-color: rgb(255, 111, 0.0);">901234</span>'


    for i in range(20 + 1):
        print(text_insterer(test_text, i, '[===]', debug=True))

    # insert empty string test
    for i in range(20 + 1):
        print(text_insterer(test_text, i, '', debug=True))

    # insert empty string to shrot string # 不会发生
    for i in range(20 + 1):
        print(text_insterer('1', i, '', debug=True))

    # insert empty string to empty string
    for i in range(20 + 1):
        print(text_insterer('', i, '', debug=True))

    # insert string to empty string
    for i in range(20 + 1):
        print(text_insterer('', i, '123', debug=True))




