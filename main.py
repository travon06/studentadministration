from Student import Student

def get_input_from_options(options: list):
    while True:
        for index, option in enumerate(options):
            print(f'{option}: {index + 1}')
            
        try:
            user_input: int  = int(input('Input: '))
        except ValueError:
            continue
        
        if(user_input > len(options) or user_input <= 0 ):
            continue
        
        return user_input
        

def main():
    user_input = get_input_from_options([
        'option 1',
        'second option',
        'third option'
    ])
    
    print(user_input)
    
if __name__ == '__main__':
    main()