from general import *
class Process:

    fileLocation = 'Temp'
    base_path = ''
    queue_file = ''
    visited_file = ''
    queue = set()
    visited = set()

    def __init__(self, base_path):
        Process.base_path = base_path
        Process.queue_file = Process.fileLocation + '/queue.txt'
        Process.visited_file = Process.fileLocation + '/visited.txt'
        self.boot()
        self.move_dir('First Process', Process.base_path)

    @staticmethod
    def boot():
        create_project_dir(Process.fileLocation)
        create_data_files(Process.fileLocation, Process.base_path)
        Process.queue = file_to_set(Process.queue_file)
        Process.visited = file_to_set(Process.visited_file)

    @staticmethod
    def move_dir(thread_name, page_url):
        if page_url not in Process.visited:
            Process.add_list_to_queue(Process.gather_list(page_url))
            Process.queue.remove(page_url)
            Process.visited.add(page_url)
            Process.update_files()

    @staticmethod
    def gather_list(page_url):
        all_dir = set()
        test_directory = page_url
        if os.path.isfile(test_directory):
            return all_dir
        for child in os.listdir(test_directory):
            all_dir.add(test_directory+"\\"+child)
        return all_dir

    @staticmethod
    def add_list_to_queue(links):
        if len(links)==0:return
        for url in links:
            if (url in Process.queue) or (url in Process.visited):
                continue
            Process.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Process.queue, Process.queue_file)
        set_to_file(Process.visited, Process.visited_file)
