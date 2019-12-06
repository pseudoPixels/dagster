from dagster.core.types.marshal import PickleFileBasedSerializationStrategy
from dagster.utils import safe_tempfile_path


def test_serialization_strategy():
    serialization_strategy = PickleFileBasedSerializationStrategy()
    with safe_tempfile_path() as tempfile_path:
        serialization_strategy.serialize('foo', tempfile_path)
        assert serialization_strategy.deserialize(tempfile_path) == 'foo'
