
import re
from pathlib import Path




def templete_apply(text: str) -> str:
    t = Path('test', 'test_file', 'templete.html').read_text(encoding='utf-8')
    pattern_sub = re.compile(r'\[\[SUB MARK\]\]')
    return pattern_sub.sub(text, t)