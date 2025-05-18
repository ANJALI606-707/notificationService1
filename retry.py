import time

def retry_send(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            func()
            return True
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    return False
