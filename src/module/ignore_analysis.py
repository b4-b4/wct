def get_ignore_params():
    params = []  # table that will contain the parameters
    with open('.ignore', 'r') as ignore_file:
        for line in ignore_file.readlines():
            if line[0] == "#":
                pass
            else:
                params.append(line)

    return params
