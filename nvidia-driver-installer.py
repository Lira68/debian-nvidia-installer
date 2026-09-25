import subprocess
import os

output = input("""Вас вітає скрипт оновлення, встановлення і перевстановлення драйверів нвідіа у дебіан
1  Видалити драйвера Нвідіа
2  Встановити дравйвера Нвідіа
3  Додати nonfree репозиторії
-----> """)


try:
    output = int(output)

except Exception as error :
    print("Введіть коректне значення")

else:
    
    if int(output) > 3:
        print("Введіть коректне значення")


if output == 1 :
    os.system("sudo apt remove --purge nvidia-* && sudo reboot")


if output == 2 :
    os.system("sudo apt install -y firmware-linux firmware-linux-nonfree firmware-misc-nonfree && sudo apt install -y linux-headers-$(uname -r) dkms && sudo apt install linux-headers-$(uname -r) nvidia-driver firmware-misc-nonfree && sudo reboot")


if output == 3 :
    repo_check = subprocess.check_output(["bash", "-c", "grep -RhE '^[[:space:]]*(Components:|deb )' /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null | grep -E 'contrib|non-free'"], text=True)

    if bool(repo_check) is True:
        print("Ви вже маєте nonfree репозиторй")

    else:
        os.system("sudo sed -i 's/ main$/ main contrib non-free non-free-firmware/' /etc/apt/sources.list && sudo apt update")
