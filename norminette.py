import sys
import os
import re


class Norminette():

    def __init__(self, *args, **kwargs):
        self.current_folder = args[0]
        self.c_file_list = []
        self.error = 0
        self.red_color = '\033[31m'
        self.green_color = '\033[32m'
        self.end = '\033[0m'

    # Get all c files
    def get_c_files(self):

        for root, directory, files in os.walk(self.current_folder):
            for get_file in files:

                is_c_file = re.match('.*\.c', get_file)
                is_h_file = re.match('.*\.h', get_file)

                if is_c_file or is_h_file:
                    self.c_file_list.append(root + "/" + get_file)
                else:
                    self.error += 1
                    print(self.red_color + root + "/" + get_file + ":" + self.end +
                          "Folder must contains only compilable c file (.c or .h)")

    # Check max function
    def check_max_function(self):

        for path in self.c_file_list:
            # Read file
            opened_file = open(path, 'r')
            content = opened_file.read()
            # Get line
            lines = content.split("\n")
            # Function index
            function_index = 0

            for line in lines:
                is_declaration = re.match(
                    'void|int|char|short|long|float|double\s\(*\)', line)
                is_contain_string = re.match('.*["]+', line)
                is_variable = re.match('.*[=]+', line)
                is_object_like = re.match('.*[:]+', line)

                if is_declaration and not is_contain_string and not is_variable and not is_object_like:

                    if function_index >= 5:
                        self.error += 1
                        print(self.red_color + path + ":" + self.end +
                              " Your file cant contain more than 5 functions")

                    function_index += 1

    # Check namming with no uppercase
    def check_namming(self):

        for path in self.c_file_list:
            is_contain_uppercase = re.search('[A-Z]+', path)

            if is_contain_uppercase:
                self.error += 1
                print(self.red_color + path + ":" + self.end +
                      " All file and folder must respect snake case namming convention")

    def is_success(self):
        if self.error == 0:
            print(self.green_color + "OK" + self.end)


if __name__ == "__main__":

    try:
        get_folder = sys.argv[1]
    except:
        print("\033[31m Please enter a folder ! \033[0m")
        get_folder = ''

    norminette = Norminette(get_folder)
    norminette.get_c_files()
    norminette.check_max_function()
    norminette.check_namming()

    if get_folder != '':
        norminette.is_success()
