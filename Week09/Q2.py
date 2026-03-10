
# ============================================================
#  WEEK 09 LAB — Q2: SEQUENTIAL vs THREADED EXECUTION
#  COMP2152 — [Rehaan Lachporia: 101594859]
# ============================================================

import time
import threading


# TODO: Complete simulate_task(name, duration, lock)
#   1. lock.acquire(), print(f"[START] {name}"), lock.release()
#   2. time.sleep(duration)
#   3. lock.acquire(), print(f"[DONE]  {name} ({duration}s)"), lock.release()
def simulate_task(name, duration, lock):
    lock.acquire()
    print(f"[START] {name}")
    lock.release()

    time.sleep(duration)

    lock.acquire()
    print(f"[DONE] {name} ({duration}s)")
    lock.release()


# TODO: Complete run_threaded(tasks, lock)
#   1. Create an empty list: threads = []
#   2. For each (name, duration) in tasks:
#        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
#        threads.append(t)
#   3. Loop to start all threads
#   4. Loop to join  all threads  (separate loop!)
def run_threaded(tasks, lock):
    threads = []
    for name, duration in tasks:
        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    lock = threading.Lock()
    lock.acquire()
    print("only one thread prints at a time")
    lock.release()
# --- Provided below — error handling example from Week 06 ---

def run_sequential(tasks, lock):
    for name, duration in tasks:
        simulate_task(name, duration, lock)


if __name__ == "__main__":
    print("=" * 60)
    print("  SEQUENTIAL vs THREADED EXECUTION")
    print("=" * 60)

    tasks = [("Brew Coffee", 3), ("Toast Bread", 2), ("Fry Eggs", 4)]
    lock = threading.Lock()

    print("\n--- Running SEQUENTIALLY ---")
    try:
        t0 = time.time()
        run_sequential(tasks, lock)
        seq = time.time() - t0
        print(f"Sequential time: {seq:.2f} seconds")
    except Exception as e:
        print(f"[ERROR] {e}")
        seq = None

    print("\n--- Running with THREADS ---")
    try:
        t0 = time.time()
        run_threaded(tasks, lock)
        thr = time.time() - t0
        print(f"Threaded time: {thr:.2f} seconds")
    except Exception as e:
        print(f"[ERROR] {e}")
        thr = None

    if seq and thr and thr > 0:
        print(f"\nSpeedup: {seq / thr:.2f}x faster with threads!")

    print("\n" + "=" * 60)
