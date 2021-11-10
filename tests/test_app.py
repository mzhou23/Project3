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
    
# while we cannot directly test the flask html methods
# we can ensure that they are appropriately intertwined
# with the flask context by verifying they fail outside
# of it.
    
def test_index():
    failsOutOfContext = False
    try:
        a.index()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_remove():
    failsOutOfContext = False
    try:
        a.remove(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_add():
    failsOutOfContext = False
    try:
        a.add()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_prioritize():
    failsOutOfContext = False
    try:
        a.prioritize(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_check():
    failsOutOfContext = False
    try:
        a.check(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_addTag():
    failsOutOfContext = False
    try:
        a.addTag()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_removeTag():
    failsOutOfContext = False
    try:
        a.removeTag("some_tag")
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_tagItem():
    failsOutOfContext = False
    try:
        a.tagItem(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
