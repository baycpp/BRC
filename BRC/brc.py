from itertools import combinations_with_replacement
from colorama import Fore, init 
from time import sleep  
from os import system
import subprocess

init(autoreset="true")

numbers_and_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = '!+%&/=?_-*,."#$|~'
turkish_characters = "ğüşiçö"

def banner():
    system("cls")
    print(Fore.RED + """

███████████████████████████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██▄─█─▄███▄─▄▄▀██▀▄─██▄─▄▄▀███─▄▄▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
██─▄─▀██─▀─███▄─▄█████─▄─▄██─▀─███─▄─▄███─███▀██─▄─▄██─▀─██─███▀██─▄▀███─▄█▀██─▄─▄█
▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

------------------------------- "Penxloiw Group" ----------------------------------

Author: baycpp                    Version: 1.2                   Instagram: bay.cpp

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
    

def combination_brute(characters):
    rar = input(Fore.CYAN + "Rar dosyasını giriniz: ")
    max_length = input(Fore.CYAN + "Maksimum kaç hane: ")

    return_code = 1

    for r in range(1, int(max_length)+1):
            if return_code == 0:
                break

            else:
                for combo in combinations_with_replacement(characters, r=r):
                    command = f"7z.exe x {rar} -p{''.join(combo)} -Y"
                    p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    p.communicate(input='Y \n'.encode())

                    if p.returncode == 0:
                        print(Fore.GREEN + "Şifre Bulundu: ", ''.join(combo))
                        return_code = 0
                        break

                    else:
                        print(Fore.RED + "Denenen Şifre: ", ''.join(combo))

def rarCrackerWithCombination():
    print("\n1: Olası tüm kombinasyonlar")
    print("2: Sadece Harfler [özel karakterler eklenebilir]")
    print("3: Sadece Sayılar [özel karakterler eklenebilir]")

    combination_input = input(Fore.CYAN + "\nİşlem giriniz: ")

    if combination_input == "1":
        characters = numbers_and_letters + special_characters + turkish_characters
        combination_brute(characters)

    elif combination_input == "2":
        special_characters_input = input("Özel karakterler eklemek ister misin Y/h: ")

        if special_characters_input == "Y" or special_characters_input == "y":
            characters = letters + special_characters
            combination_brute(characters)

        elif special_characters_input == "H" or special_characters_input == "h":
            characters = letters
            combination_brute(characters)

        else:
            print("Hatalı işlem girdiniz.")

    elif combination_input == "3":
        special_characters_input = input("Özel karakterler eklemek ister misin Y/h: ")

        if special_characters_input == "Y" or special_characters_input == "y":
            characters = numbers + special_characters
            combination_brute(characters)

        elif special_characters_input == "H" or special_characters_input == "h":
            characters = numbers
            combination_brute(characters)

    else:
        print("Hatalı işlem girdiniz.")

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
