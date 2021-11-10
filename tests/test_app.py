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
    
def test_add():
    failsOutOfContext = False
    try:
        add()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    
    # home initially does not include "new item"
    response = client.get("/")
    home_txt = response.get_data()
    assert b"new item" not in response.data
    
    url = "/add"
    data = "new item"
    response = client.post(url, data=data)
    
    assert response.status_code = 302 # code for redirect
    
    # home now includes "new item"
    response = client.get("/")
    home_txt = response.get_data()
    assert b"new item" in response.data
    
def test_remove():
    failsOutOfContext = False
    try:
        remove(0)
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
