
def addition(a, b):
    return a + b

def test_addition(sample_data):
    # Utilisez sample_data comme paramètre de test
    result = addition(sample_data['a'], sample_data['b'])
    assert result == 8

def op(a):
    return a + 5
 
def test_op():
    assert op(2) == 7