import pytest
@pytest.fixture
def sample_data():
    # La fixture fournit des données pour les tests
    return {'a': 3, 'b': 5}

