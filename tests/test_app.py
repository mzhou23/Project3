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
    url = "/add"
    data = {"item_name": "new item"}
    response = client.post(url, data=data)
    
    assert response.status_code == 302 # code for redirect
    
def test_remove():
    failsOutOfContext = False
    try:
        remove(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    response = client.get("/remove/0")
    assert response.status_code == 302 # redirect
    

def test_prioritize():
    failsOutOfContext = False
    try:
        prioritize(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    data = {"priority_selection": "medium"}
    response = client.post("/prioritize/0", data=data)
    assert response.status_code == 302 # redirect
    
    
def test_check():
    failsOutOfContext = False
    try:
        check(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    url = "/add"
    data = {"item_name": "new item"}
    response = client.post(url, data=data)
    
    response = client.get("/check/0")
    assert response.status_code == 302 # redirect
    
    
def test_addTag():
    failsOutOfContext = False
    try:
        addTag()
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    url = "/addTag"
    data = {"tag_name": "tag name  "}
    response = client.post(url, data=data)
    
    assert response.status_code == 302 # code for redirect
    
    
def test_removeTag():
    failsOutOfContext = False
    try:
        removeTag("some_tag")
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    #client = app.test_client()
    #response = client.get("/removeTag/tag1")
    #assert response.status_code == 302 # code for redirect
    
    
def test_tagItem():
    failsOutOfContext = False
    try:
        tagItem(0)
    except:
        failsOutOfContext = True
    assert failsOutOfContext
    
    client = app.test_client()
    data = {"tag_selection": "none"}
    response = client.post("/tagItem/0", data=data)
    assert response.status_code == 302 # code for redirect
