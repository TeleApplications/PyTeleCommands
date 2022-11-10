from prefixes.prefix import Prefix


class BaseErrorHandler(Exception):
    pass


class BadCommandStructure(BaseErrorHandler):
    def __init__(self, class_instance, super_class):
        super(BadCommandStructure, self).__init__(f"Class {class_instance} must derive from {super_class}")


class TerminalErrorHandler(BaseErrorHandler):
    def __init__(self, message: str):
        super(TerminalErrorHandler, self).__init__()
        print(Prefix.error + message)


class CommandDoesNotExistError(TerminalErrorHandler):
    def __init__(self, command_name: str):
        super(CommandDoesNotExistError, self).__init__(f"Command [{command_name}] does not exist")


class OptionDoesNotExistError(TerminalErrorHandler):
    def __init__(self, option):
        super(OptionDoesNotExistError, self).__init__(f"Option [{option}] does not exist")


class NoCommandOptionSetError(TerminalErrorHandler):
    def __init__(self):
        super(NoCommandOptionSetError, self).__init__(f"Command name should be followed by an option not an argument")


class BadCommandNameError(TerminalErrorHandler):
    def __init__(self):
        super(BadCommandNameError, self).__init__(f"Command should start from a-z")


class BadNumberOfArgumentsError(TerminalErrorHandler):
    def __init__(self, message, option, args: list):
        super(BadNumberOfArgumentsError, self).__init__(f"{message} [{option}] args: [{','.join(args)}]")
