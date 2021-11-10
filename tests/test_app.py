from flask import Flask

import app as a

def test_tag():
    tags = []
    tag1 = a.Tag(tags)
    assert len(tag1.tag_list) == 1
    tags.append("cat")
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list[0] == "cat"

def test_index():
    assert a.index() is not None
    # assert type(index()) == str
    
def test_remove():
    app = Flask(__name__)

    items = []
    tags = []
    assert a.remove(0) == "/"
