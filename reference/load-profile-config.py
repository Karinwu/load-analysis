import os
from omegaconf import OmegaConf

current_directory = os.path.dirname(os.path.realpath(__file__))
filename = "project_config.yaml"
config_path = os.path.join(current_directory, filename)
conf = OmegaConf.load(config_path)
