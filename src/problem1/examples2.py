from src.problem1 import service
from src.problem1.status import STATUS


def run_examples():
    run_example_1()
    run_example_2()
    run_example_3()


def run_example_1():
    print_message(1)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [1], 'outbounds': [0]},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [0], 'outbounds': [1]}
    ]

    service.create_product(modules=modules)


def run_example_2():
    print_message(2)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': [1]},
        {'id': 1, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [0], 'outbounds': [3]},
        {'id': 2, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': []},
        {'id': 3, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [1], 'outbounds': [0, 4]},
        {'id': 4, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': []}
    ]

    service.create_product(modules=modules)


def run_example_3():
    print_message(3)

    modules = [
        {'id': 0, 'stage': 0, 'status': STATUS.NOT_STARTED, 'inbounds': [], 'outbounds': [2]},
        {'id': 1, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [2], 'outbounds': [3]},
        {'id': 2, 'stage': 1, 'status': STATUS.NOT_STARTED, 'inbounds': [0, 4], 'outbounds': [3]},
        {'id': 3, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [1, 2], 'outbounds': [5]},
        {'id': 4, 'stage': 2, 'status': STATUS.NOT_STARTED, 'inbounds': [5], 'outbounds': [2]},
        {'id': 5, 'stage': 3, 'status': STATUS.NOT_STARTED, 'inbounds': [3], 'outbounds': [4]}
    ]

    service.create_product(modules=modules)


def print_message(num):
    print("========================================================")
    print(f"##### RUN EXAMPLE {num} #####\n")
    print("========================================================\n")


run_examples()
