import os
import pytest
from utils import organize_by_type, organize_by_date


@pytest.fixture
def setup_test_dir(tmp_path):
    """Create a temporary test directory with dummy files."""
    file1 = tmp_path / "test1.txt"
    file1.write_text("dummy text")
    file2 = tmp_path / "test2.jpg"
    file2.write_text("dummy image")
    return tmp_path


def test_organize_by_type(setup_test_dir):
    moved = organize_by_type(str(setup_test_dir))
    assert moved == 2
    assert (setup_test_dir / "txt" / "test1.txt").exists()
    assert (setup_test_dir / "jpg" / "test2.jpg").exists()


def test_organize_by_date(setup_test_dir):
    moved = organize_by_date(str(setup_test_dir))
    # Expect files moved into some date folder
    assert moved == 2
    assert any(folder.is_dir() for folder in setup_test_dir.iterdir())
