import subprocess
import platform
import psutil

def main():
    os_name = platform.system()
    print(f"Operating System: {os_name}")
    print(f"OS: {os_name}: \nplatform: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor() or 'Undefined'} {platform.machine()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"CORE CPU: {psutil.cpu_count(logical=True)} logical/ {psutil.cpu_count(logical=False)} physical")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    print(f"Disk: {round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB")
    if os_name == "Linux":
        cmd = [
            "nmcli", 
            "-t", 
            "-f", 
            "DEVICE,TYPE,STATE", 
            "device", 
            "status"
        ]
    elif os_name == "Windows":
        cmd = [
            "netsh",
            "wlan",
            "show",
            "interfaces"
        ]
    else:
        print(f"Unsupported OS: {os_name}")
        return
    
    output = subprocess.check_output(cmd).decode("utf-8")
    print(output)


if __name__ == "__main__":
    main()