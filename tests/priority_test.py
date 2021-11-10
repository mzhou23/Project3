from app import Priority


def test_init():
    m = Priority("medium")
    assert m.priority == "medium"
    assert m.priority_list is ["medium", "low", "high"]
    assert m.color == "orange"

    l = Priority("low")
    assert l.priority == "low"
    assert l.priority_list is ["low", "medium", "high"]
    assert l.color == "green"

    h = Priority("medium")
    assert h.priority == "medium"
    assert h.priority_list is ["high", "low", "medium"]
    assert h.color == "orange"


def test_cpl():
    p = Priority("medium")
    prior_list = p.create_priority_list("medium")
    assert prior_list is ["medium", "low", "high"]

    prior_list = p.create_priority_list("high")
    assert prior_list is ["high", "low", "medium"]

    prior_list = p.create_priority_list("low")
    assert prior_list is ["low", "medium", "high"]

    prior_list = p.create_priority_list("other")
    assert prior_list is ["other", "low", "medium", "high"]


def test_gpc():
    p = Priority("low")
    assert p.get_priority_color() == "green"

    p = Priority("medium")
    assert p.get_priority_color() == "orange"

    p = Priority("high")
    assert p.get_priority_color() == "red"


def test_gp():
    p = Priority("low")
    assert p.get_priority() == "low"

    p = Priority("other")
    assert p.get_priority() == "other"


def test_sp():
    p = Priority("low")
    assert p.get_priority() == "low"
    assert p.get_priority_color == "green"
    assert p.priority_list is ["low", "medium", "high"]
    
    p.set_priority("medium")
    assert p.get_priority == "medium"
    assert p.get_priority_color == "orange"
    assert p.priority_list is ["medium", "low", "high"]
