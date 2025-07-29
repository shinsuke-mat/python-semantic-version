import pytest
from semantic_version.version import Version


def test_constructor_valid01():
    v = Version('1.2.3')
    assert v.major == 1
    assert v.minor == 2
    assert v.patch == 3

def test_constructor_valid02():
    v = Version('1.20.30')
    assert v.major == 1
    assert v.minor == 20
    assert v.patch == 30

@pytest.mark.parametrize('semver', [
    '1.2.3', '1.2.99', '1.2.0', '0.0.0', '10.20.30'
])
def test_constructor_parameterized(semver):
    Version(semver)

@pytest.mark.parametrize('semver', [
    '1', '1.2', '1.2.', '1.2.3.', '1..3', 'aaa',
    '1.01.1', '1. 2.3', '1.-2.3'
])
def test_constructor_invalid(semver):
    try:
        Version(semver)
        pytest.fail()
    except ValueError:
        pass
