from typing import List
import os
from jinja2 import Environment, FileSystemLoader

from source.models import Page, Message

templates_dir = os.path.join('source/templates')
static_dir = 'static'
_css_dir = os.path.join(static_dir, 'css')
env = Environment( loader=FileSystemLoader(templates_dir) )

PAGES = [
    Page('Home', 'index.html'),
    Page('CV', 'cv.html'),
    Page('RunBot', 'projects/runbot.html'),
    Page('CompoundPye', 'projects/compoundpye.html',
         scripts=['../static/js/playAnimation.js']),
    Page('This', 'projects/this.html')
]

CSS_FILES = [
    'default.css',
    'fonts.css'
]


for p in PAGES:
    prefix = '/'.join(['..'] * p.url.count('/'))
    for c in CSS_FILES:
        path = os.path.join(prefix, _css_dir, c)
        p.render_kwargs.update({
            c.split('.')[0] + '_css': path
        })

MESSAGES = []

def render_pages():
    for p in PAGES:
        fname = os.path.join('html', p.url)
        _folder, _file = os.path.split(fname)
        if _folder:
            os.makedirs(_folder, exist_ok=True)
        template = env.get_template(p.url)
        with open(fname, 'w') as fh:
            fh.write(template.render(pages=PAGES,
                                     messages=get_messages_for_page(p.title,
                                                                    MESSAGES),
                                     current_page=p,
                                     **p.render_kwargs))
        print('rendered', fname)


def get_messages_for_page(pagetitle: str, messages: List[Message]) -> List[str]:
    filtered_messages = []
    for m in messages:
        if pagetitle in m.blacklist:
            continue
        filtered_messages.append(m.text)
    return filtered_messages


if __name__ == "__main__":
    render_pages()
