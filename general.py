import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_data_files(project_name, base_dir):
    queue = os.path.join(project_name , 'queue.txt')
    visited = os.path.join(project_name,"visited.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_dir)
    if not os.path.isfile(visited):
        write_file(visited, '')

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_contents(path):
    open(path, 'w').close()

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(dirs, file_name):
    with open(file_name,"w") as f:
        for l in sorted(dirs):
            f.write(l+"\n")
