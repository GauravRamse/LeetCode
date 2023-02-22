##################################################################
# test.py
import time
import argparse

# According to your function
def solve(a, b):
    for i in range(4):
        time.sleep(3)
    return a+b


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, default= 2)
    parser.add_argument("b", type= int, default=3)
    args = parser.parse_args()


    solve(args.a, args.b)


##################################################################
# 5. Subprocess_for_printil_live_time_of_execution.py
# Line 11 put your file name where you put function

import subprocess

import time
from datetime import datetime

start_time = datetime.now()

# Call the function in a subprocess without waiting for the result
process = subprocess.Popen(["python", "./test.py", "2", "3"])

while True:
    return_code = process.poll()
    if return_code is not None:
        print(f"Subprocess has completed with time {time_str}", end = "\n")
        break
    else:

        end = datetime.now() - start_time
        time_str = str(end)
        time_str = ":".join(time_str.split(".")[:-1])
        print("Current time is ", time_str, end = "\r")

        time.sleep(1)