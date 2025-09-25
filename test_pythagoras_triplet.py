from Squared_number import give_solutions
def test_pythagoras():

    assert give_solutions(0) == []

    with pytest.raises(TypeError)