def get_input(user_input):
    IRAN_PREFIX = '+98'

    stripted_user_input = str(user_input.strip())
    
    if 7 < len(stripted_user_input) < 14:
        
        if len(stripted_user_input) == 8:
            print('City number')
            return 1
    
        if stripted_user_input.startswith(IRAN_PREFIX) and len(stripted_user_input) == 13:
            new_format = stripted_user_input[3:]

            if new_format.startswith('9', 0, 1):
                print('Mobile number')
                return 2
            else:
                print('City number')
                return 1

        elif stripted_user_input.startswith('98') and len(stripted_user_input) == 12:
            new_format2 = stripted_user_input[2:]

            if new_format2.startswith('9', 0, 1):
                print('Mobile number')
                return 2
            else:
                print('City number')
                return 1

        elif stripted_user_input.startswith('09'):
            print('Mobile number')
            return 2

        elif stripted_user_input.startswith('9'):
            print('Mobile number')
            return 2
        else:
            print('City number')
            return 1
    else:
        print('Bad type!')
        return 0
