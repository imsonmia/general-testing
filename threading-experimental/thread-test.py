# IF YOU SEE THIS, GIT VCS SHOULD BE WORKING PROPERLY
# Last Edited 2021-01-25 13:46:04
import threading
import time
if __name__ == '__main__':
    def even():
        i = 0
        while True:
            print(i)
            i += 2
            time.sleep(2)


    def odd():
        i = 1
        while True:
            print(i)
            i += 2
            time.sleep(1)

    thread_even = threading.Thread(target=even)
    thread_odd = threading.Thread(target=odd)
    thread_even.start()
    thread_odd.start()