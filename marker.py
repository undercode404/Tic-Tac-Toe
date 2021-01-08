def marker():
    user_marker_choice = " "
    while not (user_marker_choice == 'X' or user_marker_choice == 'O'):
        user_marker_choice = input("Please select either 'X' or 'O' as your marker : ").upper()


    if user_marker_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')