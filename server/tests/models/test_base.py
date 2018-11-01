import pytest

from awesome_applejuice_backend.models import SimpleSerializer


def test_simple_serializer_methods():
    with pytest.raises(TypeError):
        serializer = SimpleSerializer()
