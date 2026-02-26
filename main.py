import os

def get_conf():
    result = []
    reading = False

    try:
        with open("config.cfg", "r") as file:
            for line in file:
                line = line.strip()

                # Skip empty lines or comments outside the section
                if not line or line.startswith("#"):
                    continue

                if line == "info_you_want:":
                    reading = True
                    continue

                if reading:
                    # If we hit another section (ends with :), stop reading
                    if line.endswith(":") and line != "info_you_want:":
                        break
                    result.append(line)
    except FileNotFoundError:
        print("Error: config.cfg not found.")
    
    return result

def get_name_os():
    try:
        with open("/etc/os-release", "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("PRETTY_NAME="):
                    value = line.split("=", 1)[1].strip('"')
                    print(f"OS: {value}")
                    break
    except FileNotFoundError:
        print("OS: Info not found")

def get_host_name():
    try:
        with open("/etc/hostname", "r") as file:
            # .read().strip() is safer than indexing readlines()
            host = file.read().strip()
            if host:
                print(f"Hostname: {host}")
            else:
                print("Hostname: [File is empty]")
    except Exception as e:
        print(f"Hostname: Could not read ({e})")

def get_timezone():
    try:
        with open("/etc/timezone", "r") as file:
            tz = file.read().strip()
            print(f"Timezone: {tz}")
    except Exception:
        print("Timezone: Not found")

def get_cpu_name():
    try:
        with open("/proc/cpuinfo", "r") as file:
            for line in file:
                if "model name" in line:
                    value = line.split(":", 1)[1].strip()
                    print(f"CPU: {value}")
                    break
    except FileNotFoundError:
        print("CPU: Info unavailable")

def get_cpu_cores():
    try:
        with open("/proc/cpuinfo", "r") as file:
            for line in file:
                if "cpu cores" in line:
                    value = line.split(":", 1)[1].strip()
                    print(f"Cores: {value}")
                    break
    except FileNotFoundError:
        print("Cores: Info unavailable")

def get_ram_free():
    try:
        with open("/proc/meminfo", "r") as file:
            for line in file:
                if line.startswith("MemAvailable:"):  
                    return line.split()[1]
    except FileNotFoundError:
        return "0"

def get_ram_total():
    try:
        with open("/proc/meminfo", "r") as file:
            for line in file:
                if line.startswith("MemTotal:"):
                    return line.split()[1]
    except FileNotFoundError:
        return "0"

def ram():
    print(f"RAM: {get_ram_total()} kB / {get_ram_free()} kB")

def hardware():
    print("----Hardware Info----")

def space():
    print()

def get_uptime():
    try:
        with open("/proc/uptime", "r") as file:
            line = file.readline()
            if line:
                seconds = float(line.split()[0])
                minutes = round(seconds / 60, 2)
                print(f"Uptime: {minutes} mins")
    except FileNotFoundError:
        print("Uptime: Unavailable")

# Dictionary mapping config names to functions
info_you_want_dict = {
    "get_host_name": get_host_name,
    "get_name_os": get_name_os,
    "get_timezone": get_timezone,
    "get_cpu_name": get_cpu_name,
    "get_cpu_cores": get_cpu_cores,
    "get_ram": ram,
    "get_uptime": get_uptime,
    "space": space,
    "hardware": hardware,
    "Hardware": hardware
}

def main():
    wanted = get_conf()

    if not wanted:
        print("No items found in config to display.")
        return

    for item in wanted:
        func = info_you_want_dict.get(item)
        if func:
            func()
        else:
            print(f"Unknown item in config: {item}")

if __name__ == "__main__":
    main()