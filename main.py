import menu
import artwork_db


def main():
    """sets up tables if necessary and sets up menu to continue to pop up until user hits Q """
    artwork_db.create_tables()
    while True:
        menu.display_menu()


if __name__ == '__main__':
    main()
