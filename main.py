

def get_conf():
    result = []
    reading = False

    with open("config.cfg", "r") as file:
        for line in file:
            line = line.strip()

            if line == "info_you_want:":
                reading = True
                continue

            if reading:
                if line == "" or line.endswith(":"):
                    break
                result.append(line)

    return result


def get_name_os():
    with open("/etc/os-release", "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("PRETTY_NAME="):
                hodnota = line.split("=", 1)[1].strip('"')
                print(f"OS: {hodnota}")
                break

def get_host_name():
    with open("/etc/hostname", "r") as file:
        vsechny_radky = file.readlines()
        prvni_radek = vsechny_radky[0].strip()
        print (f"Hostname: {prvni_radek}")

def get_timezone():
    with open("/etc/timezone", "r") as file:
        vsechny_radky = file.readlines()
        prvni_radek = vsechny_radky[0].strip()
        print (f"Timezone: {prvni_radek}")

def get_cpu_name():
    with open("/proc/cpuinfo", "r") as file:
        for line in file:
            line = line.strip()
            if "model name" in line:
                hodnota = line.split(":", 1)[1].strip()
                print(f"CPU: {hodnota}")
                break

def get_cpu_cores():
    with open("/proc/cpuinfo", "r") as file:
        for line in file:
            line = line.strip()
            if "cpu cores" in line:
                hodnota = line.split(":", 1)[1].strip()
                print(f"Cores: {hodnota}")
                break

def get_ram_free():
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemAvailable:"):  
                return line.split()[1]  

def get_ram_total():
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemTotal:"):
                return line.split()[1]

def ram():
    print(f"RAM: {get_ram_total()} kB / {get_ram_free()} kB")

def hardware():
    print("----Hardware Info----")

def space():
    print()

def get_uptime():  
    with open("/proc/uptime", "r") as file:
        for line in file:
            cislo = line.split()
            min_cislo = float(cislo[0]) / 60
            min_cislo  = round(min_cislo, 2)
            print(f"Uptime {min_cislo} mins")
        
def space():
    print()

def harware():
    print("-----Hardware-----")

info_you_want_dict = {
"get_host_name": get_host_name,
"get_name_os": get_name_os,
"get_timezone": get_timezone,
"get_cpu_name": get_cpu_name,
"get_cpu_cores": get_cpu_cores,
"get_ram": ram,
"get_uptime": get_uptime,
"space": space,
"Hardware": hardware}

def main():
    wanted = get_conf()

    for item in wanted:
        func = info_you_want_dict.get(item)
        if func:
            func()
        else:
            print(f"Unknown item in config: {item}")



if __name__ == "__main__":
    main()


