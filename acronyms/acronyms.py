def find_acronym():
    look_up = input('What acronyms are you looking for?\n')
    found = False
    try: 
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not fount')
        return
    
    if (not found):
        print('Acronym not found')

def add_acronym():
    acronym = input('What acronym do you want to create?\n')
    definition = input('What is the definition of your acronym?\n')
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition)

def main():
    choice = input('Do you want find (F) acronym or add (A) acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()
