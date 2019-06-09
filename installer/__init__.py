import questions
from . import install_agent as agent
from . import install_cli as cli
from . import install_server as server


def show():
    # initial initialization
    module, answer = questions.list('installer_menu', clear_console=True)

    while True:
        if module == "server":
            server.install()

        if module == "cli":
            cli.install()

        if module == "agent":
            agent.install()

        if module == "exit":
            exit(0)

        module, answer = questions.list('installer_menu', clear_console=True)
