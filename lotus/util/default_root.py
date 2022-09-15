import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("LOTUS_ROOT", "~/.lotus/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("LOTUS_KEYS_ROOT", "~/.lotus_keys"))).resolve()
