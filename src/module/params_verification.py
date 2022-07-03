def verification(argv_list):

    if type(argv_list) != list:
        print('The parameter of the verification() function is not an array as expected.')
        quit()

    if len(argv_list) == 3:
        print('All the parameters did not pass, ' 
              'try again with all the parameters this time.\n'
              'Refer to the README for more information about the parameters.'
              )
        quit()
    
    params_list = {
        '-s': [
            '--root',
            '--session',
            '--anywhere'
        ]
    }

    for key, suffixes in params_list.items():
        if key == argv_list[1]:
            for suffix in suffixes:
                if suffix == argv_list[2]:
                    return
            print(f'"{argv_list[1]}" has not attribute "{" ".join(argv_list[2:])}".')
            quit()

        print(f'"{argv_list[1]}" is not recognized.')  # "a b c d" is not recognized.
        quit()
