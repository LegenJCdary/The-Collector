def input_mode():
    pass


def output_mode():
    pass


def sync_mode():
    pass


def player_mode():
    pass


def main(mode: int) -> None:
    input_mode()
    output_mode()
    sync_mode()
    player_mode()


def collector():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    collector()
