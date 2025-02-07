# multiprocessing - многопроцессность
import time
from multiprocessing import Pool, Process


def worker(name):
    print(f'{name} started')
    time.sleep(1)
    print(f'{name} finished')


def main():
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(f'Process-{i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
