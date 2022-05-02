import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("LOTUS_ROOT", "~/.lotus/mainnet"))).resolve()
STANDALONE_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("LOTUS_STANDALONE_WALLET_ROOT", "~/.lotus/standalone_wallet"))
).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("LOTUS_KEYS_ROOT", "~/.lotus_keys"))).resolve()
