from torch.utils.data import Dataset

from exe_project.data import corrupt_mnist

from tests import _PATH_DATA


def test_my_dataset():
    """Test the MyDataset class."""
    train_set, _ = corrupt_mnist(_PATH_DATA)
    assert isinstance(train_set, Dataset)
