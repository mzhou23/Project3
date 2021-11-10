from flask import Flask

import app

def test_tag():
    tags = []
    tag1 = app.Tag(tags)
    assert len(tag1.tag_list) == 1
    tags.append("cat")
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list[0] == "cat"

def test_index():
    assert app.index() is not None
    # assert type(index()) == str
    
def test_remove():
    app = Flask(__name__)

    items = []
    tags = []
    assert app.remove(0) == "/"
