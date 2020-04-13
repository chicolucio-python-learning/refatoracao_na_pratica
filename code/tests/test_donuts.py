from donuts import donuts, Quantity


def test_quantity():
    assert Quantity(9)
    assert str(Quantity(9)) == '9'
    assert str(Quantity(10)) == 'many'


def test_donuts():
    assert donuts(4), 'Number of donuts: 4'
    assert donuts(9), 'Number of donuts: 9'
    assert donuts(10), 'Number of donuts: many'
    assert donuts(99), 'Number of donuts: many'
