from torch.utils.data import Dataset

from exe_project.data import corrupt_mnist


def test_my_dataset():
    """Test the MyDataset class."""
    train_set, _ = corrupt_mnist()
    assert isinstance(train_set, Dataset)
