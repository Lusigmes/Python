import textwrap


def menu():
    menu = """\n
    **************** MENU ****************

    [q]\tSair
    **************************************
    => """
    return input(textwrap.dedent(menu))