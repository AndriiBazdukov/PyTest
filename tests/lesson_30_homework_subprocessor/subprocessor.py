import subprocess
import platform


def ping_websites(websites, count=3):
    system_platform = platform.system().lower()

    if system_platform == "windows":
        command_template = "ping -n {count} {website}"
    else:
        command_template = "ping -c {count} {website}"

    for website in websites:
        command = command_template.format(count=count, website=website)
        result = subprocess.run(command, shell=True, check=True, text=True)
        print(f"Ping results for {website}:\n{result.stdout}")


websites_to_ping = ["www.google.com", "www.gmail.com", "www.ukr.net"]
ping_websites(websites_to_ping)
