
def get_input():
    user_input = input('Please enter your number: ')
    IRAN_PREFIX = '+98'

    stripted_user_input = user_input.strip()
    
    if 7 < len(stripted_user_input) < 14:
        
        if len(stripted_user_input) == 8:
            print('City number')
    
        if stripted_user_input.startswith(IRAN_PREFIX):
            new_format = stripted_user_input[3:]

            if new_format.startswith('9', 0, 1):
                print('Mobile number')
            else:
                print('City number')

        elif stripted_user_input.startswith('98'):
            new_format2 = stripted_user_input[2:]

            if new_format2.startswith('9', 0, 1):
                print('Mobile number')
            else:
                print('City number')
                
        elif stripted_user_input.startswith('09'):
            print('Mobile number')
            
        else:
            print('City number')

    else:
        print('Bad type!')