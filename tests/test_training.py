import os
from pathlib import Path

import hydra
import torch
from omegaconf import DictConfig, OmegaConf
from sklearn.metrics import RocCurveDisplay, accuracy_score, f1_score, precision_score, recall_score

from exe_project.model import MyAwesomeModel

# from exe_project.src.exe_project import train
from tests import _PROJECT_ROOT


# ... previous code remains the same
def test_training():
    # loss value should be scalar and non negative

    # training_cfg = OmegaConf.load(Path(_PROJECT_ROOT) / "configs" / "model_conf.yaml")
    loss_fn = torch.nn.CrossEntropyLoss()

    # Mock data
    batch_size = 4
    num_classes = 10
    logits = torch.randn(batch_size, num_classes, requires_grad=True)  # Random predictions (logits)
    targets = torch.randint(0, num_classes, (batch_size,))  # Random valid class indices

    # Compute loss
    loss = loss_fn(logits, targets)

    # Assertions
    assert isinstance(loss.item(), float), "Loss is not a scalar."
    assert loss.item() >= 0, "Loss is negative."
