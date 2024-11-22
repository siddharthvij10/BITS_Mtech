import pytest
from hydra import initialize, compose
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig
import os

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