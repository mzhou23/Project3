from app import Priority


def test_init():
    m = Priority("medium")
    assert m.priority == "medium"
    assert m.priority_list == ["medium", "low", "high"]
    assert m.color == "orange"

    l = Priority("low")
    assert l.priority == "low"
    assert l.priority_list == ["low", "medium", "high"]
    assert l.color == "green"

    h = Priority("high")
    assert h.priority == "high"
    assert h.priority_list == ["high", "low", "medium"]
    assert h.color == "red"


def test_cpl():
    p = Priority("medium")
    prior_list = p.create_priority_list("medium")
    assert prior_list == ["medium", "low", "high"]

    prior_list = p.create_priority_list("high")
    assert prior_list == ["high", "low", "medium"]

    prior_list = p.create_priority_list("low")
    assert prior_list == ["low", "medium", "high"]

    prior_list = p.create_priority_list("other")
    assert prior_list == ["low", "medium", "high"]


def test_gpc():
    p = Priority("high")

    assert p.get_priority_color("low") == "green"

    assert p.get_priority_color("medium") == "orange"

    assert p.get_priority_color("high") == "red"


def test_gp():
    p = Priority("low")
    assert p.get_priority() == "low"

    p = Priority("other")
    assert p.get_priority() == "medium"


def test_sp():
    p = Priority("low")
    assert p.get_priority() == "low"
    assert p.color == "green"
    assert p.priority_list == ["low", "medium", "high"]
    
    p.set_priority("medium")
    assert p.get_priority() == "medium"
    assert p.color == "orange"
    assert p.priority_list == ["medium", "low", "high"]
