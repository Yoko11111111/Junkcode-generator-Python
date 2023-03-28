import random
import string

def generate_junk_code():
    # Generate a random number of functions and classes to create
    num_functions = random.randint(300, 500)
    num_classes = random.randint(300, 500)

    # Define a list of valid Python function argument names
    arg_names = ['arg{}'.format(i) for i in range(10)]

    # Define a list of valid Python variable names
    var_names = [c for c in string.ascii_lowercase]

    # Generate the code
    code = ''
    for i in range(num_functions):
        # Choose a random function name and argument list
        func_name = ''.join(random.choices(var_names, k=random.randint(1, 10)))
        arg_list = ', '.join(random.choices(arg_names, k=random.randint(0, 5)))
        arg_names_used = set()
        if arg_list:
            arg_names_used.update(arg_list.split(', '))
        arg_names_unused = arg_names_used.symmetric_difference(arg_names)
        arg_list_unused = ', '.join(random.sample(arg_names_unused, k=random.randint(0, len(arg_names_unused))))
        code += 'def {}({}): pass\n\n'.format(func_name, arg_list_unused)

    for i in range(num_classes):
        # Choose a random class name
        class_name = ''.join(random.choices(var_names, k=random.randint(1, 10)))
        code += 'class {}:\n'.format(class_name)
        # Add random variables to the class
        for j in range(random.randint(1, 10)):
            var_name = ''.join(random.choices(var_names, k=random.randint(1, 10)))
            var_value = ''
            var_type = random.choice(['int', 'bool', 'str', 'float'])
            if var_type == 'int':
                var_value = str(random.randint(0, 100))
            elif var_type == 'bool':
                var_value = str(random.choice([True, False]))
            elif var_type == 'str':
                var_value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
                var_value = "'" + var_value + "'"
            elif var_type == 'float':
                var_value = str(random.uniform(0, 100))
            code += '    {} = {}\n'.format(var_name, var_value)
        code += '\n'

    return code

if __name__ == '__main__':
    with open('junk.txt', 'a') as f:
        code = generate_junk_code()
        f.write(code)
        print('Code saved to junk.txt')
        print(code)
