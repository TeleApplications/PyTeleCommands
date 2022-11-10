from errors import errors


class TerminalCommand:
    name: str
    options: dict

    @classmethod
    def __set_command_name(cls, array: list[str]):
        command_name = array.pop(0).lower()
        if 97 <= ord(command_name[0]) <= 122:
            cls.name = command_name
        else:
            raise errors.BadCommandNameError()

    @classmethod
    def __set_command_options(cls, array: list[str]):
        cls.options = dict()
        option_identifier = ""
        for item in array:
            try:
                if item.startswith("-"):
                    option_identifier = item
                    cls.options[option_identifier] = ""
                else:
                    cls.options[option_identifier] = [*cls.options[option_identifier], item]
            except KeyError:
                raise errors.NoCommandOptionSetError()

    @classmethod
    def from_list(cls, array: list[str]):
        try:
            cls.__set_command_name(array)
            cls.__set_command_options(array)
        except (errors.BadCommandNameError, errors.NoCommandOptionSetError):
            return None
        return cls
