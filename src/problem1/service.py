from status import STATUS

CACHE = {}


def validate_product(modules):
    """
    As you've been noticed by now, our product is shaped as a graph. In order to validate the
    product you have to check if the graph has any cycles.

    :param modules: list of modules
    :return bool: True - if product is valid, False - otherwise
    """

    has_cycle = False

    # TODO: 4. VALIDATE PRODUCT

    return not has_cycle


def check_all_modules_completed():
    done = True
    for id in CACHE:
        if CACHE[id]['status'] is not STATUS.COMPLETED:
            done = False
            break

    if done:
        print("==> PRODUCT COMPLETED")


def print_validation(has_cycle):
    print("========================================================")
    res = "has" if has_cycle else "doesn't have"
    print(f"0. VALIDATION: The product {res} cycles!")
    print("========================================================\n")


def print_results(msg):
    print("========================================================")
    print(msg)
    print("--------------------------------------------------------")
    print_product()
    print("========================================================\n")


def print_product():
    print("MODULE ID: stage, inbounds, outbounds .......... STATUS")
    for id in CACHE:
        module = CACHE[id]
        print(
            f"MODULE {id}: ({module['stage']}), {module['inbounds']}, {module['outbounds']} .......... {module['status']}")


def create_product(modules):
    """
    Using the list of modules you need to create the "product" by saving those modules to the CACHE,
    but only if the "product" is valid.

    :param modules: list of modules
    :return bool: True - if product is valid, False - otherwise
    """

    valid_product = validate_product(modules)

    # TODO: 1. CREATE PRODUCT

    print_results("1. CREATE PRODUCT")

    return valid_product


def enable_product():
    """
    Enabling a product means that a user can start working on a product and complete modules.

    A module can be completed only when its status is IN_PROGRESS and the first module that can be
    completed should be the very first module (id = 0).

    All the standalone modules from the very same stage should also be ready for completion.

    :return dict: the cache
    """

    # TODO: 2. ENABLE PRODUCT

    print_results("2. ENABLE PRODUCT")

    return CACHE


def complete_module(id):
    """
    Completing a module means that a module has moved from IN_PROGRESS state to COMPLETED state.

    You might notice that some modules are not in IN_PROGRESS yet. We should make sure that, in the
    background, whenever all inbounds modules are completed for a specific module, that module will
    be automatically moved to IN_PROGRESS.

    :param id: the id of a module
    :return dict: the cache
    """

    # TODO: 3. COMPLETE MODULE

    print_results(f"3. COMPLETE MODULE {id}")
    check_all_modules_completed()

    return CACHE
