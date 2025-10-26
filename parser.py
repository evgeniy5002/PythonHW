import os


def test_remove_comments(s: str) -> None:
    print(f"[{s}] -> [{remove_comments(s)}]")


def test_get_pair(s: str) -> None:
    pair = get_pair(s)
    if pair is None:
        print("Symbol  <:>  is not in the line")
        return

    print(f"{pair[0]}: {pair[1]}")


def remove_comments(line: str) -> str:
    for char in ("#", ";"):
        index = line.find(char)
        if index != -1:
            line = line[:index]
    return line.strip()


def get_pair(line: str) -> tuple[str, str] | None:
    if ":" not in line:
        return None

    key, value = line.split(":", 1)
    return key.strip(), value.strip()


def parse_ini(path: str) -> dict | None:
    if not os.path.isfile(path):
        print(f"File  <{path}>  does not exist")
        return None

    try:
        with open(path, 'r', encoding='utf-8') as file:
            pairs = []
            filtered_lines = filter(None, (remove_comments(line) for line in file))

            for line in filtered_lines:
                pair = get_pair(line)

                if pair is None:
                    print(f"Invalid line in INI file:  <{line}>")
                    return None

                pairs.append(pair)

            return {k: v for k, v in pairs}
    except OSError as err:
        print(f"OSError: {err}")
        return None


def main() -> None:
    ini = parse_ini("file.ini")

    if ini is not None:
        [print(f"{k}: {v}", sep="\n") for k, v in ini.items()]

    print("═══════════════════════════════════")
    test_remove_comments("qwe # rty")
    test_remove_comments("qwe ; rty")
    test_remove_comments("qwe #; rty")
    test_remove_comments("qwe #; rty")
    test_remove_comments("#qwerty")
    test_remove_comments(";qwerty")

    print("═══════════════════════════════════")
    test_get_pair("Key: Value")
    test_get_pair("Key; Value")
    test_get_pair("Key Value")


if __name__ == "__main__":
    main()
