from flask import Flask, render_template
from flask.ext.flatpages import FlatPages
import jinja2
from dateutil.parser import parse

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

jinja2.filters.FILTERS['datetimeformat'] = \
        lambda dstr : parse(dstr).strftime("%B %-d, %Y")

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

if __name__ == '__main__':
    app.run(port=8000)
