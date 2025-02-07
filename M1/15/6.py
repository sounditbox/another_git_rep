import multiprocessing as mp


def foo(q):
    print('Process Started')
    q.put('Process Finished')


if __name__ == '__main__':
    # mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
