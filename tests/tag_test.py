import app as a

def test_tag():
    tags = []
    tag1 = a.Tag(tags)
    assert len(tag1.tag_list) == 1
    tags.append("cat")
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list[0] == "cat"
    
def test_get_tag():
    tags = ["dog"]
    tag1 = a.Tag(tags)
    assert tag1.get_tag() == tag1.tag
    assert tag1.tag == "none"
    
def test_get_with_set():
    tags = ["mouse"]
    tag1 = a.Tag(tags)
    assert tag1.get_tag() == "none"
    tag1.set_tag("mouse",tags)
    assert tag1.get_tag() == "mouse"

def test_set_with_update():
    tags = ["cat","mouse"]
    tag1 = a.Tag(tags)
    assert tag1.get_tag() == "none"
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list == ["cat","mouse","none"]
    tag1.set_tag("mouse",tags)
    assert tag1.get_tag() == "mouse"
    assert tag1.tag_list == ["mouse","cat","none"]
    
def test_update():
    tags = ["cat","mouse"]
    tag1 = a.Tag(tags)
    assert tag1.get_tag() == "none"
    tag1.set_tag("cat",tags)
    tag1.update_tag_list(["cat","dog"])
    assert tag1.tag_list == ["cat","dog","none"]
    tag1.update_tag_list(["dog","cat"])
    assert tag1.tag_list == ["cat","dog","none"]
    
