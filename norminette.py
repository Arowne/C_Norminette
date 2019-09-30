import os
import re


class Norminette():

    def __init__(self, *args, **kwargs):
        self.current_folder = os.curdir
        self.c_file_list = []
        self.red_color = '\033[31m'
        self.green_color = '\033[32m'
        self.end = '\033[0m'

    # Get all c files
    def get_c_files(self):

        for root, directory, files in os.walk(self.current_folder):
            for get_file in files:

                get_match = re.search('.*\.c', get_file)

                if get_match:
                    self.c_file_list.append(root + "/" + get_file)

    # Check max function
    def check_max_function(self):

        for path in self.c_file_list:
            # Read file
            opened_file = open(path, 'r')
            content = opened_file.read()
            # Get line
            lines = content.split("\n")
            #Function index
            function_index = 0

            for line in lines:
                is_declaration = re.match('void|int|char|short|long|float|double\s\(*\)', line)
                is_contain_string = re.match('.*["]+', line)
                is_variable = re.match('.*[=]+', line)
                is_object_like = re.match('.*[:]+', line)
                
                if is_declaration and not is_contain_string and not is_variable and not is_object_like:

                    if function_index >= 5:
                        print(self.red_color + path + ":" + self.end +" Your file cant contain more than 5 functions")

                    function_index += 1


if __name__ == "__main__":
    norminette = Norminette()
    norminette.get_c_files()
    norminette.check_max_function()
