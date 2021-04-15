import threading
import time


def main():
    threads = [
        threading.Thread(target=greater, args=('Yury', 3), daemon=True),
        threading.Thread(target=greater, args=('Stiven', 2), daemon=True),
        threading.Thread(target=greater, args=('Boris', 4), daemon=True)
    ]
    [thread.start() for thread in threads]
    print('hello from main!')
    [thread.join() for thread in threads]
    print('Done!')


def greater(name: str, times: int):
    for _ in range(0, times):
        print(f'Hello, {name}')
        time.sleep(1)


if __name__ == '__main__':
    main()
