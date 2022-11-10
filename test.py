from commands.command_base import CommandBase
from commands.register_command import RegisterCommand, RegisterOption
from cli.terminal import Terminal


@RegisterCommand("ping")  # command name in terminal
class Ping(CommandBase):
    def __init__(self):
        """ your code..."""

    @RegisterOption("-ip")  # command option in terminal
    def option_ip(self, ip_address):
        """ your code..."""

    def execute(self):  # method executed as the latest
        """ your code..."""


@RegisterCommand("ipconfig")  # command name in terminal
class IPConfig(CommandBase):
    def __init__(self):
        """ your code..."""

    @RegisterOption("-all")  # command option in terminal
    def option_all(self):
        """ your code..."""

    def execute(self):  # method executed as the latest
        """ your code..."""


if __name__ == '__main__':
    t = Terminal()
    t.run()
