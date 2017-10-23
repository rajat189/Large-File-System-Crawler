import threading
from queue import Queue
from process import Process
from general import *
BaseDir = os.getcwd()+'\Test'
QueueFile = 'Temp\queue.txt'
queue = Queue()
Process(BaseDir)

def job():
	while True:
		url = queue.get()
		Process.move_dir(threading.current_thread().name, url)
		queue.task_done()

def create_jobs():
	for link in file_to_set(QueueFile):
		queue.put(link)
	queue.join()
	crawl()

def crawl():
	queued_links = file_to_set(QueueFile)
	if len(queued_links)>0:
		t = threading.Thread(target=job)
		t.start()
		create_jobs()

crawl()
