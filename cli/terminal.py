import shlex

from errors import errors
from commands.register_command import CommandDictionary
from cli.terminal_command import TerminalCommand


class Terminal:
    is_running: bool = True
    terminal_symbol: str = ">> "
    __bad_symbols: tuple = (" ", )

    def __init__(self):
        ...

    @staticmethod
    def command_serializer(command: str) -> TerminalCommand:
        return TerminalCommand.from_list(shlex.split(command))

    @staticmethod
    def run_command(command: TerminalCommand):
        if not command:
            return None

        if command.name not in CommandDictionary.command_dict.keys():
            return errors.CommandDoesNotExistError(command.name)

        for c in CommandDictionary.command_dict:
            if command.name == c:
                class_instance = CommandDictionary.command_dict[c]["class_instance"]
                for option in command.options:
                    try:
                        CommandDictionary.command_dict[c][option](class_instance, *command.options[option])
                    except KeyError:
                        return errors.OptionDoesNotExistError(option)
                    except TypeError as e:
                        return errors.BadNumberOfArgumentsError(str(e), option, command.options[option])
                return class_instance.execute(class_instance)

    def run(self):
        while self.is_running:
            user_input = input(self.terminal_symbol)
            if len(user_input) > 0 and user_input not in self.__bad_symbols:
                self.run_command(self.command_serializer(user_input))

    @classmethod
    def set_terminal_symbol(cls, new_symbol: str):
        cls.terminal_symbol = new_symbol
