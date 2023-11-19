from os import system
from colorama import Fore, init 
import subprocess
from time import sleep  
init(autoreset="true")


def banner():
    system("cls")
    print(Fore.RED + """

███████████████████████████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██▄─█─▄███▄─▄▄▀██▀▄─██▄─▄▄▀███─▄▄▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
██─▄─▀██─▀─███▄─▄█████─▄─▄██─▀─███─▄─▄███─███▀██─▄─▄██─▀─██─███▀██─▄▀███─▄█▀██─▄─▄█
▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

------------------------------- "Penxloiw Group" ----------------------------------

Author: baycpp                    Version: 1.1                   Instagram: bay.cpp

""")


def rarCrackerWithWordlist():
    wordlist = input(Fore.CYAN + "Wordlist dosyasını giriniz: ")
    rar = input(Fore.CYAN + "Rar dosyasını giriniz: ")
    print("")

    f = open(wordlist, "r")
    lines = f.readlines()

    for line in lines:
        command = f"7z.exe x {rar} -p{line} -Y"
        p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        p.communicate(input='Y \n'.encode())
        
        if p.returncode == 0:
            print(Fore.GREEN + "Şifre Bulundu: ", line)
            break

        else:
            print(Fore.RED + "Denenen Şifre: ", line)
        

def rarCrackerWithCombination():
    print("Bu seçenek şuan kullanılamaz.")

def process():
    print("1: Wordlist")
    print("2: Kombinasyon")

    process_input = input(Fore.CYAN + "\nİşlem giriniz: ")

    if process_input == "1":
        rarCrackerWithWordlist()

    elif process_input == "2":
        rarCrackerWithCombination()

    else:
        print("Hatalı işlem girdiniz!")

banner()
process()
