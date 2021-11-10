from app import index
from app import remove
from app import Tag

def test_tag():
    tags = []
    tag1 = Tag(tags)
    assert len(tag1.tag_list) == 1
    tags.append("cat")
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list[0] == "cat"

def test_index():
    assert index() is not None
    # assert type(index()) == str
    
def test_remove():
    assert remove(0) == "/"
