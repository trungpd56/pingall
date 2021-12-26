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
                        total += 1
                        iphost = line.strip()
                        result = subprocess.run(["ping", "-n", "1", "-w", "1000", iphost], capture_output=True)
                        print(result.stdout.decode())
                        print(result.stderr.decode())
                        if result.returncode:
                                print(f'{iphost} inactive')
                                inactive += 1
        print(f"{t}---{inactive}/{total} host is inactive")
        print("*" * 23)
        print("\n")
        time.sleep(5)
