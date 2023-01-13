import service
from status import STATUS


def run_examples():
    run_example_1()
    run_example_2()
    run_example_3()
    run_example_4()


def run_example_1():
    print_message(1)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [3]},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [3]},
        {'id': 2, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []},
        {'id': 3, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [0, 1], 'outbounds': [4]},
        {'id': 4, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': []}
    ]

    valid_product = service.create_product(modules=modules)

    if valid_product:
        service.enable_product()
        service.complete_module(0)
        service.complete_module(1)
        service.complete_module(3)
        service.complete_module(4)
        service.complete_module(2)


def run_example_2():
    print_message(2)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [4]},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [2]},
        {'id': 2, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [1], 'outbounds': [4]},
        {'id': 3, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [5]},
        {'id': 4, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [0, 2], 'outbounds': [5]},
        {'id': 5, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3, 4], 'outbounds': []}
    ]

    valid_product = service.create_product(modules=modules)

    if valid_product:
        service.enable_product()
        service.complete_module(0)
        service.complete_module(1)
        service.complete_module(2)
        service.complete_module(4)
        service.complete_module(3)
        service.complete_module(5)


def run_example_3():
    print_message(3)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []},
    ]

    valid_product = service.create_product(modules=modules)

    if valid_product:
        service.enable_product()
        service.complete_module(0)
        service.complete_module(1)


def run_example_4():
    print_message(4)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [2]},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [2]},
        {'id': 2, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [0, 1], 'outbounds': [3]},
        {'id': 3, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [2], 'outbounds': [5, 6]},
        {'id': 4, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [6]},
        {'id': 5, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': [7]},
        {'id': 6, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3, 4], 'outbounds': [7]},
        {'id': 7, 'stage': 3, 'status': STATUS.NOT_STARTED, 'inbounds': [5, 6], 'outbounds': []},
        {'id': 8, 'stage': 3, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []}
    ]

    valid_product = service.create_product(modules=modules)

    if valid_product:
        service.enable_product()
        service.complete_module(0)
        service.complete_module(1)
        service.complete_module(2)
        service.complete_module(4)
        service.complete_module(3)
        service.complete_module(6)
        service.complete_module(5)
        service.complete_module(7)
        service.complete_module(8)


def print_message(num):
    print("========================================================")
    print(f"##### RUN EXAMPLE {num} #####\n")
    print("========================================================\n")


run_examples()
