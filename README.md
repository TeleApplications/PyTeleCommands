# PyTeleCommands
Command interface in python
```python

# Test command
@RegisterCommand("ping")  # command name in terminal
class Ping(CommandBase):
    def __init__(self):
        """ your code..."""

    @RegisterOption("-ttl")  # command option without in terminal
    def option_ttl(self): # no arguments
        """ your code..."""
    
    @RegisterOption("-ip")  # command option in terminal
    def option_ip(self, ip_address): # multiple arguments
        """ your code..."""

    def execute(self):  # method executed as the latest
        """ your code..."""
   
```
![](https://github.com/TeleApplications/PyTeleCommands/blob/main/assets/command.gif)
