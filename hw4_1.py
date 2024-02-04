def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()

        total_salary = 0
        num_developers = len(lines)

        for line in lines:
            try:
                salary = float(line.strip().split(',')[1])
                total_salary += salary
            except (IndexError, ValueError):
                # Пропустити рядки, які не містять коректні дані
                continue

        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            print("Incщккусе input data")
        return total_salary, average_salary

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

# Приклад виклику функції:
result = total_salary('developers_salary.txt')

if result is not None:
    total, average = result
    print(f'Total Salary: {total}')
    print(f'Average Salary: {average}')