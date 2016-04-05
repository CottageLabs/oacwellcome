import multiprocessing

bind = "127.0.0.1:5051"
workers = multiprocessing.cpu_count() * 2 + 1
proc_name = 'oacwellcome'
max_requests = 1000
