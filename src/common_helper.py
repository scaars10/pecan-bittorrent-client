
def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return content

