

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



def main():
    get_host_name()
    get_name_os()
    get_timezone()
    print("----Hardware Info----")
    get_cpu_name()


if __name__ == "__main__":
    main()
