def secure_archive(filename: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return True, file.read()
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"

        return False, "Unknown action"
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    test_content = ("[FRAGMENT 001] Digital preservation"
                    " protocols established 2087\n"
                    " [FRAGMENT 002] Knowledge must\n"
                    "survive the entropy wars\n"
                    " [FRAGMENT 003] Every byte saved"
                    " is a victory against oblivion\n")
    secure_archive("regular_file.txt", "write", test_content)

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("regular_file.txt", "read"))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", test_content))
