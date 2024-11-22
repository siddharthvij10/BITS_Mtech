import pytest
from hydra import initialize, compose
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig
import os
import rootutils

root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
from src.train import instantiate_loggers, instantiate_callbacks
import hydra
import lightning as L

@pytest.fixture(scope="module")
def cfg() -> DictConfig:
    with initialize(version_base="1.1", config_path="../configs"):
        # Basic configuration for testing
        cfg = compose(
            config_name="train",
            return_hydra_config=True,
            overrides=[
                "experiment=dog_ex",
                "trainer.fast_dev_run=True",
                # Set explicit paths for testing
                f"paths.root_dir={os.getcwd()}",
                "paths.log_dir=${paths.root_dir}/logs",
                "paths.data_dir=${paths.root_dir}/data",
                "paths.output_dir=${paths.root_dir}/outputs",
                "paths.work_dir=${paths.root_dir}",
            ]
        )
        return cfg

@pytest.fixture
def datamodule(cfg):
    """Fixture to instantiate the datamodule."""
    return hydra.utils.instantiate(cfg.data)