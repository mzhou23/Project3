from app import index
from app import Tag

<<<<<<< HEAD

def test_tag():
    tags = ["none"]
    tag1 = Tag(tags)
    assert len(tag1.tag_list) == 1
    tags.append("cat")
    tag1.set_tag("cat",tags)
    assert tag1.get_tag() == "cat"
    assert tag1.tag_list[0] == "cat"
=======
def test_index():
    assert True
>>>>>>> 529c3ff86a4b4e937c6d5a69ce90e8c5727a8eea
