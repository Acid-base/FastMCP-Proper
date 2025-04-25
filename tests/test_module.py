import pytest
from my_package.module import DataProcessor, add, greet


def test_add() -> None:
    assert add(2, 3) == 5


def test_add_type() -> None:
    with pytest.raises(TypeError):
        add("a", 1)  # type: ignore
    with pytest.raises(TypeError):
        add(1, "a")  # type: ignore


def test_greet() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_type() -> None:
    with pytest.raises(TypeError):
        greet(10)  # type: ignore


class TestDataProcessor:
    def test_init(self) -> None:
        # Test valid list initialization
        processor = DataProcessor([1, 2, 3])
        assert processor.data == [1, 2, 3]

    def test_init_type_error(self) -> None:
        # Test for invalid type in DataProcessor constructor
        with pytest.raises(TypeError):
            DataProcessor("not a list")  # type: ignore
        with pytest.raises(TypeError):
            DataProcessor([1, "not an int", 3])  # type: ignore

    def test_calculate_average(self) -> None:
        processor = DataProcessor([1, 2, 3, 4, 5])
        assert processor.calculate_average() == 3.0

    def test_calculate_average_empty_list(self) -> None:
        processor = DataProcessor([])
        assert processor.calculate_average() == 0

    def test_find_max(self) -> None:
        processor = DataProcessor([1, 5, 2, 8, 3])
        assert processor.find_max() == 8

    def test_find_max_empty_list(self) -> None:
        processor = DataProcessor([])
        with pytest.raises(ValueError):
            processor.find_max()
