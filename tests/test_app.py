from flask import Flask

import app as a
    

def test_index():
    failsOutOfContext = False
    try:
        a.index()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    
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
