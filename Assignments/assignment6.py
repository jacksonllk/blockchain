# 1) Write a short Python script which queries the user for input 
#   (infinite loop with exit possibility) and writes the input to a file.

import json
import pickle


waiting_for_input = True
namelist = []

while waiting_for_input:
    print('1: Enter name')
    print('2: Output name')
    print('Q: Quit')
    user_choice = input('Your choice: ')

    if user_choice == '1':
        with open('assignment6.txt', mode = 'a') as q:
            name = input('Name: ')
            namelist.append(name)
            q.write(name)
            q.write('\n')
            # q.write(json.dumps(namelist))
            # q.write(pickle.dumps(namelist))

    elif user_choice == '2':
        with open('assignment6.txt', mode = 'r') as q:
            file_content = q.readlines()
            for line in file_content:
                print(line)
            # file_content = json.loads(q.read())
            # file_content = pickle.loads(q.read())
            # print(file_content)

    elif user_choice == 'q':
        namelist = []
        with open('assignment6.txt', mode = 'w') as q:
            q.write('')
            # q.write(json.dumps(namelist))
            # q.write(pickle.dumps(namelist))
        waiting_for_input = False
        print('User left!')

    else:
        print('Invalid response')

# 2) Add another option to your user interface: The user should be able to 
#   output the data stored in the file in the terminal.




# 3) Store user input in a list (instead of directly adding it to the file) 
#   and write that list to the file – both with pickle and json.




# 4) Adjust the logic to load the file content to work with pickled/ json data.