from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": (
        "lotus_harvester lotus_timelord_launcher lotus_timelord lotus_farmer "
        "lotus_full_node lotus_wallet lotus_data_layer lotus_data_layer_http"
    ).split(),
    # TODO: should this be `data_layer`?
    "data": "lotus_wallet lotus_data_layer".split(),
    "data_layer_http": "lotus_data_layer_http".split(),
    "node": "lotus_full_node".split(),
    "harvester": "lotus_harvester".split(),
    "farmer": "lotus_harvester lotus_farmer lotus_full_node lotus_wallet".split(),
    "farmer-no-wallet": "lotus_harvester lotus_farmer lotus_full_node".split(),
    "farmer-only": "lotus_farmer".split(),
    "timelord": "lotus_timelord_launcher lotus_timelord lotus_full_node".split(),
    "timelord-only": "lotus_timelord".split(),
    "timelord-launcher-only": "lotus_timelord_launcher".split(),
    "wallet": "lotus_wallet".split(),
    "introducer": "lotus_introducer".split(),
    "simulator": "lotus_full_node_simulator".split(),
    "crawler": "lotus_crawler".split(),
    "seeder": "lotus_crawler lotus_seeder".split(),
    "seeder-only": "lotus_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
