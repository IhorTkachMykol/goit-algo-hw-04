def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:  # Ensure the line has all required fields
                    cat_info = {
                        'id': cat_data[0],
                        'name': cat_data[1],
                        'age': int(cat_data[2])
                    }
                    cats_list.append(cat_info)
                else:
                    print(f"Incomplete data for line: {line}")

    except FileNotFoundError:
        print(f"File not found: {path}")

    return cats_list

# Example function call:
cats_info = get_cats_info('cats_data.txt')

if cats_info:
    for cat in cats_info:
        print(cat)