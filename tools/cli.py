from tools.chats import chats_menu


def main():

    while True:

        print()
        print("=" * 60)
        print("CNBridge AI ADMIN")
        print("=" * 60)
        print()
        print("1. Управление чатами")
        print("2. Менеджеры (скоро)")
        print("3. Настройки (скоро)")
        print("0. Выход")
        print()

        cmd = input("> ").strip()

        if cmd == "1":
            chats_menu()

        elif cmd == "0":
            break


if __name__ == "__main__":
    main()