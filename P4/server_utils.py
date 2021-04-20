def print_colored(message, color):
    import termcolor
    import colorama

    colorama.init(strip="False")
    print(termcolor.colored(message, color))
