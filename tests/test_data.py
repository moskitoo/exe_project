from torch.utils.data import Dataset

from exe_project.data import corrupt_mnist


# PULL FROM DVC NEEDED TO ACCESS DATA IN THE TEST -> THAT REQUIRES AUTHENTICATION FOR GITHUB

def test_my_dataset():
    """Test the MyDataset class."""
    train_set, _ = corrupt_mnist()
    assert isinstance(train_set, Dataset)
