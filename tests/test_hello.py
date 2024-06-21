from rye_template import hello


def test_hello():
    assert isinstance(hello(), str)
