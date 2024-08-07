def clear_out(name, system):
    if name == "nt":
        return system("cls")
    return system("clear")
