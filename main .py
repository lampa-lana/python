# # Реализовать решение следующей задачи:
# «Есть два писателя, которые по очереди в течении определенного времени(у каждого разное) пишут в одну книгу.
#  Данная книга очень популярна, у неё есть как минимум 3 фаната(читателя),
# которые ждут не дождутся, чтобы прочитать новые записи из неё.
#  Каждый читатель и писатель – отдельный поток. Одновременно книгу может читать несколько читателей,
# но писать единовременно может только один писатель.»
import threading
import time
from threading import Thread, Event, get_ident, BoundedSemaphore, Lock, RLock


bs = BoundedSemaphore(1)
event = Event()
variable = ""
variable2 = ""
lock = RLock()
mutex = threading.RLock()


def producer1():
    with mutex:
        bs.acquire()
        event.set()
        global variable
        variable += "Я Писатель1 и пишу очень хорошо "
        print(" Писатель 1 говорит: Все ждите, пока я  работаю! Поток {} время {}".format(
            threading.get_ident(), time.ctime()))
        bs.release()
        time.sleep(1)


def producer2():
    with mutex:
        bs.acquire()
        event.set()
        global variable2
        variable2 += "Я Писатель2 и пишу лучше Писателя 1 "
        print(" Писатель 2 говорит: Все ждите, пока работаю я ! Поток {} время {}".format(
            threading.get_ident(), time.ctime()))
        bs.release()
        time.sleep(5)


def consumer(thread_id):
    while True:
        event.wait()
        print("{} - Я взял! Вот что там было: {}, {}. (Поток {} время {})".format(thread_id,
                                                                                  variable, variable2, threading.get_ident(), time.ctime()))


if __name__ == '__main__':
    start = time.time()
    t1 = [threading.Thread(target=producer1)] + \
        [threading.Thread(target=producer2)]
    threads = (Thread(target=consumer, args=(thread_id, ))
               for thread_id in range(5))

    for t in t1:
        t.start()
    for t in t1:
        t.join(timeout=5)
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=5)

    event.clear()
    print((time.time() - start))
