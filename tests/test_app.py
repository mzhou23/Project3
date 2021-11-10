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
    
def test_remove():
    failsOutOfContext = False
    try:
        a.remove(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
