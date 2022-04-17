import time

def recursive(n):
    if n != 0:
        print(n)
        time.sleep(1)
        recursive(n-1)
    else:
        print("BOOM")

recursive(5)