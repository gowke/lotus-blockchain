from setuptools import setup

dependencies = [
    "aiofiles==0.7.0",  # Async IO for files
    "blspy==1.0.11",  # Signature library
    "chiavdf==1.0.6",  # timelord and vdf verification
    "chiabip158==1.1",  # bip158-style wallet filters
    "chiapos==1.0.10",  # proof of space
    "clvm==0.9.7",
    "clvm_tools==0.4.4",  # Currying, Program.to, other conveniences
    "chia_rs==0.1.1",
    "clvm-tools-rs==0.1.7",  # Rust implementation of clvm_tools
    "aiohttp==3.8.1",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==6.6.0",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==36.0.2",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking, expected to be replaced by filelock
    "filelock==3.4.2",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.2.3",  # Gives the chia processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    # TODO: when moving to click 8 remove the pinning of black noted below
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.7",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.17",  # dns lib
    "typing-extensions==4.0.1",  # typing backports like Protocol and TypedDict
    "zstd==1.5.0.4",
    "packaging==21.0",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    "coverage",
    "pre-commit",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy",
    # TODO: black 22.1.0 requires click>=8, remove this pin after updating to click 8
    "black==21.12b0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.0",
    "types-aiofiles",
    "types-click",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

kwargs = dict(
    name="lotus-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@lotus.net",
    description="Chia blockchain full node, farmer, timelord, and wallet.",
    url="https://lotus.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="lotus blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "lotus",
        "lotus.cmds",
        "lotus.clvm",
        "lotus.consensus",
        "lotus.daemon",
        "lotus.full_node",
        "lotus.timelord",
        "lotus.farmer",
        "lotus.harvester",
        "lotus.introducer",
        "lotus.plot_sync",
        "lotus.plotters",
        "lotus.plotting",
        "lotus.pools",
        "lotus.protocols",
        "lotus.rpc",
        "lotus.seeder",
        "lotus.server",
        "lotus.simulator",
        "lotus.types.blockchain_format",
        "lotus.types",
        "lotus.util",
        "lotus.wallet",
        "lotus.wallet.puzzles",
        "lotus.wallet.rl_wallet",
        "lotus.wallet.cat_wallet",
        "lotus.wallet.did_wallet",
        "lotus.wallet.settings",
        "lotus.wallet.trading",
        "lotus.wallet.util",
        "lotus.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "lotus = lotus.cmds.lotus:main",
            "lotus_daemon = lotus.daemon.server:main",
            "lotus_wallet = lotus.server.start_wallet:main",
            "lotus_full_node = lotus.server.start_full_node:main",
            "lotus_harvester = lotus.server.start_harvester:main",
            "lotus_farmer = lotus.server.start_farmer:main",
            "lotus_introducer = lotus.server.start_introducer:main",
            "lotus_crawler = lotus.seeder.start_crawler:main",
            "lotus_seeder = lotus.seeder.dns_server:main",
            "lotus_timelord = lotus.server.start_timelord:main",
            "lotus_timelord_launcher = lotus.timelord.timelord_launcher:main",
            "lotus_full_node_simulator = lotus.simulator.start_simulator:main",
        ]
    },
    package_data={
        "lotus": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "lotus.util": ["initial-*.yaml", "english.txt"],
        "lotus.ssl": ["lotus_ca.crt", "lotus_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
