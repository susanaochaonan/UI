import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)


class Mythread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info('start loop'+str(nloop)+' at '+ctime())
    sleep(nsec)
    logging.info('end loop'+str(nloop)+' at '+ctime())

def main():
    loops=[1,3]
    logging.info('start all at '+ctime())
    threads=[]
    for i in range(len(loops)):
        t=Mythread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    logging.info("end all at "+ctime())


if __name__=='__main__':
    main()