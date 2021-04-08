def print_colored(message, color):
    import termcolor
    import colorama

    colorama.init(strip="False")
    print("To server:", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING command", "green")
