import controller
def display_menu():
    """sets up UI menu"""
    print('\n')
    print('Enter 1 to register a new artist ')
    print('Enter 2 to display portfolio of an artist ')
    print('Enter 3 to display available work by an artist ')
    print('Enter 4 to enter a new artwork (artist must be registered) ')
    print('Enter 5 to delete an artwork')
    print('Enter 6 to change an artwork\'s availability to "sold" ')
    print('Enter Q to quit ')
    new_choice = input('Please enter your choice here: ')
    choice_valid(new_choice)


def choice_valid(new_choice):
    """determines if user response is valid, if found to be valid it converts to int to
    be compared one last time to ensure the choice is one of the options"""
    if new_choice.isalnum():
        if new_choice.isalpha() and new_choice.upper() == 'Q':
            quit()
        elif new_choice.isalpha():
            print('Please enter a valid choice ')
        else:
            choice = int(new_choice)
            if not choice < 1 or choice > 5:
                choice_made(int(choice))
    else:
        print('invalid choice: ')


def choice_made(choice):
    """once choice has been validated, calls the appropriate function"""
    if choice == 1:
        artist_name = controller.get_artist_name()
        controller.add_new_artist(artist_name)
    elif choice == 2:
        artist_name = controller.get_artist_name()
        controller.display_artist_complete_portfolio(artist_name)
    elif choice == 3:
        artist_name = controller.get_artist_name()
        controller.display_artist_available_portfolio(artist_name)
    elif choice == 4:
        controller.add_new_artwork()
    elif choice == 5:
        controller.get_artwork_to_delete()
    elif choice == 6:
        return 6
