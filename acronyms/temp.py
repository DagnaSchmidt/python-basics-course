acronym = input('What acronym do you want to create?\n')
definition = input('What is the definition of your acronym?\n')

with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition)