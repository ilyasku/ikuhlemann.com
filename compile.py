from typing import List
import os
from jinja2 import Environment, FileSystemLoader

from source.models import Page, Message

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'source/templates')
env = Environment( loader=FileSystemLoader(templates_dir) )

PAGES = [Page('Home', 'index.html'),
         Page('Research', 'research.html', scripts=["static/js/slideshow.js"])]

MESSAGES = []

def render_pages():
    for p in PAGES:
        fname = os.path.join(root, 'html', p.url)
        template = env.get_template(p.url)
        with open(fname, 'w') as fh:
            fh.write(template.render(pages=PAGES,
                                     messages=get_messages_for_page(p.title,
                                                                    MESSAGES),
                                     **p.render_kwargs))


def get_messages_for_page(pagetitle: str, messages: List['_Message']) -> List[str]:
    filtered_messages = []
    for m in messages:
        if pagetitle in m.blacklist:
            continue
        filtered_messages.append(m.text)
    return filtered_messages


if __name__ == "__main__":
    render_pages()
