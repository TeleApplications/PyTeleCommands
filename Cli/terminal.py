import shlex

from Errors import errors
from Commands.register_command import CommandDictionary
from Cli.terminal_command import TerminalCommand


class Terminal:
    is_running: bool = True
    terminal_symbol: str = ">>"
    __bad_symbols: tuple = (" ",)

    def __init__(self):
        """init function"""

    def run_forever(self, print_error: bool = True):
        while self.is_running:
            self.run_once(print_error)

    def run_once(self, print_error: bool = True):
        user_input = input(f"{self.terminal_symbol} ")
        self.run_command(user_input, print_error)

    def run_command(self, command: str, print_output: bool = True):
        if len(command) > 0 and command not in self.__bad_symbols:
            val = self.__run_command(command)
            if print_output:
                print(val)
            return val

    def __run_command(self, command: str):
        _command = self.__command_serializer(command)
        if _command.name_error:
            error = errors.CommandDoesNotExistError(_command.name_error).to_string()
            _command.name_error = ""
            return error

        if _command.option_error:
            error = errors.OptionDoesNotExistError(_command.option_error).to_string()
            _command.option_error = ""
            return error

        if _command.name not in CommandDictionary.command_dict.keys():
            return errors.CommandDoesNotExistError(_command.name).to_string()

        for comm in CommandDictionary.command_dict:
            if _command.name == comm:
                class_instance = CommandDictionary.command_dict[comm]["class_instance"]
                for option in _command.options:
                    try:
                        return CommandDictionary.command_dict[comm][option](class_instance,
                                                                            *_command.options[option])
                    except KeyError:
                        return errors.OptionDoesNotExistError(option).to_string()
                    except TypeError as e:
                        return errors.BadNumberOfArgumentsError(str(e), option,
                                                                _command.options[option]).to_string()
                return class_instance.execute(class_instance)

    @staticmethod
    def __command_serializer(command: str) -> TerminalCommand:
        return TerminalCommand.from_list(shlex.split(command))

    @classmethod
    def set_terminal_symbol(cls, new_symbol: str):
        cls.terminal_symbol = new_symbol
