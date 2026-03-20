import os
import platform
import datetime

def get_e5er_status():
    # macOS system uptime logic
    uptime = os.popen("uptime").read().strip()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n" + "="*40)
    print("           E 5 E R .  CORE")
    print("="*40)
    print(f" OPERATOR  : {platform.node()}")
    print(f" SYSTEM    : {platform.system()} {platform.release()}")
    print(f" DATE      : {current_time}")
    print(f" UPTIME    : {uptime}")
    print("="*40)
    print(" STATUS    : [ EXECUTED . ]")
    print("="*40 + "\n")

if __name__ == "__main__":
    get_e5er_status()