import time  # Python time module

timer_seconds = int(input("How many seconds ? "))

time_end = time.time() + timer_seconds  # The timer should end x seconds after now
time_now = time.time()
while time_now < time_end:
    print(f'Timer will run another {int(time_end - time_now)} seconds.')
    time.sleep(1)
    # Most important step of all
    time_now = time.time()

print('Timer done!')
