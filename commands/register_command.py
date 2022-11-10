from functools import wraps

import errors.errors
from commands.command_base import CommandBase


class CommandDictionary:
    command_dict: dict = dict()
    command_name: str

    @classmethod
    def update_dictionary(cls, key, value) -> None:
        cls.command_dict.setdefault(cls.command_name, {}).update({key: value})

    @classmethod
    def set_command_name(cls, command_name: str) -> None:
        cls.command_name = command_name


class RegisterCommand:
    def __init__(self, command_name: str) -> None:
        CommandDictionary.set_command_name(command_name)

    def __call__(self, class_instance):
        if not issubclass(class_instance, CommandBase):
            raise errors.errors.BadCommandStructure(class_instance, CommandBase)
        CommandDictionary.update_dictionary("class_instance", class_instance)
        return class_instance


class RegisterOption:
    _option_name: str

    def __init__(self, option_name: str) -> None:
        self.option_name = option_name

    @property
    def option_name(self) -> str:
        return self._option_name

    @option_name.setter
    def option_name(self, value: str) -> None:
        if not value.startswith("-"):
            self._option_name = "-" + value
        else:
            self._option_name = value

    def __call__(self, method_instance):
        CommandDictionary.update_dictionary(self._option_name, method_instance)

        @wraps(method_instance)
        def wrapper(*args, **kwargs):
            return method_instance(*args, **kwargs)

        return wrapper
