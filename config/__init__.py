# project requirements and inclusions
from config import Config

# initialize version
__version__ = "0.0.1"
VERSION = tuple(map(int, __version__.split('.')))

# all elements here are loaded
__all__ = [

	Config
]
