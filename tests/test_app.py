from flask import Flask

from app import *
    

def test_index():
    failsOutOfContext = False
    try:
        index()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    
def test_remove():
    failsOutOfContext = False
    try:
        remove(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_add():
    failsOutOfContext = False
    try:
        add()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_prioritize():
    failsOutOfContext = False
    try:
        prioritize(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_check():
    failsOutOfContext = False
    try:
        check(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_addTag():
    failsOutOfContext = False
    try:
        addTag()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_removeTag():
    failsOutOfContext = False
    try:
        removeTag("some_tag")
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
def test_tagItem():
    failsOutOfContext = False
    try:
        tagItem(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
