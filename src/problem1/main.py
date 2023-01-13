import service
from status import STATUS

MODULES = [
    {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [3]},
    {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [3]},
    {'id': 2, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []},
    {'id': 3, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [0, 1], 'outbounds': [4]},
    {'id': 4, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': []}
]


def call_service():
    valid_product = service.create_product(modules=MODULES)

    if valid_product:
        service.enable_product()
        service.complete_module(0)
        service.complete_module(1)
        service.complete_module(3)
        service.complete_module(4)
        service.complete_module(2)


call_service()
