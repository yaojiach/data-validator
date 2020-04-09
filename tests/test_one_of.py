import pytest


@pytest.fixture
def one_of_tester():
    from data_validator.validators import OneOf
    
    class Tester:
        tester = OneOf('python', 'rust')

    return Tester()


def test_one_of_fail(one_of_tester):
    with pytest.raises(ValueError) as excinfo:
        one_of_tester.tester = 'java'
    assert 'java' in str(excinfo.value)


def test_one_of_success(one_of_tester):
    one_of_tester.tester = 'python'
    assert one_of_tester.tester == 'python'
