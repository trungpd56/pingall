import subprocess
import os
import time
from datetime import datetime



while True:
        print("**********Trung-VDT**********")
        now = datetime.now()
        t = now.strftime("%H:%M:%S")
        inactive = 0
        total = 0
        with open('iplist', 'r') as f:
                for line in f:
                        with open(os.devnull, "wb") as limbo:
                                total += 1
                                iphost = line.strip()
                                result = subprocess.Popen(["ping", "-n", "1", "-w", "1000", iphost],
                                                          stdout=limbo, stderr=limbo).wait()
                                if result:
                                        print(f'{iphost} inactive')
                                        inactive += 1
        print(f"{t}---{inactive}/{total} host is inactive")
        print("*" * 23)
        print("\n")
        time.sleep(5)
