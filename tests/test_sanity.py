def test_sanity():
    assert True == True

    try:
        assert True == False
    except AssertionError as e:
        assert isinstance(e, AssertionError)
