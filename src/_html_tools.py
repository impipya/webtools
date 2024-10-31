
import re


def html_mark_escape(text: str) -> str:
    return re.sub(r'\<', '&lt', re.sub(r'\>', '&gt', text))




def div_mark(text: str, type: str) -> str:
    return f'<div class="{type}">\n{text}\n</div>'




def span_mark(text: str, type: str) -> str:
    return f'<span class="{type}">{text}</span>'