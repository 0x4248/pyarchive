# pyarchive
# Quickly create and manage archives for large amount of data
# GitHub: https://www.github.com/lewisevans2007/pyarchive
# Licence: GNU General Public License v3.0
# By: Lewis Evans

from colorama import Fore, Back, Style
import os
import random
import tarfile
import re

class verbose:
    def log(message):
        print(Fore.GREEN+"[+] "+Style.RESET_ALL+message)
    def question(message):
        print(Fore.YELLOW+"[?] "+Style.RESET_ALL+message)    
    def warn(message):
        print(Fore.YELLOW+"[!] "+Style.RESET_ALL+message)    
    def error(message):
        print(Fore.RED+"[-] "+Style.RESET_ALL+message)   
    def critical(message):
        print(Fore.RED+"[x] "+Style.RESET_ALL+message)
    def info(message):
        print(Fore.CYAN+"[*] "+Style.RESET_ALL+message)

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ ==  "__main__":
    print("Welcome to PyArchive console type help to get help.")
    cmd_input_line = "PyArchive ("+Fore.BLUE+"Not Selected"+Style.RESET_ALL+")>"
    in_archive = False
    current_archive = ""
    start_dir = os.getcwd()
    while True:
        cmd = input(cmd_input_line)
        if cmd.upper() == "SELECT":
            print("Enter location of PYARCHIVE file e.g (/archives/1F54AF)")
            path = input(">")
            try:
                os.chdir(start_dir)
                os.chdir(path)
            except:
                verbose.error("Archive not found if it does not exist create one with "+Fore.GREEN+"create"+Style.RESET_ALL+".")
                continue
            if os.path.exists("PYARCHIVE"):
                verbose.log("Set archive to "+path)
            else:
                verbose.error("Archive not found if it does not exist create one with "+Fore.GREEN+"create"+Style.RESET_ALL+".")
                continue
            cmd_input_line = "archive ("+Fore.CYAN+path+Style.RESET_ALL+")>"
            in_archive = True
            current_archive = path
        if cmd.upper() == "CREATE":
            location = input("Enter where to put the archive>")
            verbose.info("Creating warehouse.")
            try:
                os.chdir(location)
            except:
                verbose.error("Path doesn't exist.")
                continue
            warehouse = str(hex(random.randint(1,16777215))).replace("0x","")
            os.mkdir(warehouse)
            f = open(warehouse+"/PYARCHIVE","w")
            f.write("This is a pyarchive")
            f.close()
            title = input("Title of archive>")
            f = open(warehouse+"/TITLE.txt","w")
            f.write(title)
            f.close()
            verbose.info("Archive created. the location is "+os.getcwd()+"\\"+warehouse)
        if cmd.upper() == "ADD":
            if in_archive == True:
                location = input("Location of folder containing files>")
                if os.path.isdir(location):
                    pass
                else:
                    verbose.error("Location: "+location+" doses not exist")
                    continue
                while True:
                    title = input("Title of archive>")
                    if len(title) != 0:
                        break
                
                description = input("Description of archive (Leave blank for none)>")
                author = input("Author of archive (Leave blank for none)>")
                date = input("Date of known data creation (Leave blank for none)>")
                
                while True:
                    print("What is the type of data your are archiving\n1) text\n2) documents (doc's and PDF's)\n3) pictures\n4) audio\n5) video\n6) data\n7) software\n8) disk images (ISO files and VMDK)\n9) other\n10) other (will give prompt asking you what type)\n")
                    data_type = input("Enter number>")
                    if data_type == "1" or data_type.upper == "TEXT":
                        data_type = "text"
                        break
                    if data_type == "2" or data_type.upper == "DOCUMENTS":
                        data_type = "documents"
                        break
                    if data_type == "3" or data_type.upper == "PICTURES":
                        data_type = "pictures"
                        break
                    if data_type == "4" or data_type.upper == "AUDIO":
                        data_type = "audio"
                        break
                    if data_type == "5" or data_type.upper == "VIDEO":
                        data_type = "video"
                        break
                    if data_type == "6" or data_type.upper == "DATA":
                        data_type = "data"
                        break
                    if data_type == "7" or data_type.upper == "SOFTWARE":
                        data_type = "software"
                        break
                    if data_type == "8" or data_type.upper == "DISK IMAGES":
                        data_type = "disk images"
                        break
                    if data_type == "9" or data_type.upper == "OTHER":
                        data_type = "other"
                        break
                    if data_type == "10":
                        data_type = input("Enter data type>")
                        break
                    else:
                        print("Enter a valid number")

                if input("Do you want to place this archive in a specific location of your warehouse [Y/N]>").upper() == "Y":
                    section = input("Section in of warehouse [6 Digits] (Leave blank for random)>").lower()
                    shelf = input("Shelf in of warehouse [4 Digits] (Leave blank for random)>").lower()
                    if len(section) == 0:
                        section = str(hex(random.randint(1,16777215))).replace("0x","")
                    else:
                        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', section) == False:
                            verbose.error("Not a hex number")
                            section = str(hex(random.randint(1,16777215))).replace("0x","")
                        else:
                            if len(section) != 6:
                                verbose.error("Hex number should be 6 digits but it was "+str(len(section))+" digits long")

                    if len(shelf) == 0:
                        shelf = str(hex(random.randint(1,65535))).replace("0x","")
                    else:
                        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', shelf) == False:
                            verbose.error("Not a hex number")
                            shelf = str(hex(random.randint(1,65535))).replace("0x","")
                        else:
                            if len(shelf) != 4:
                                verbose.error("Hex number should be 4 digits but it was "+str(len(section))+" digits long")
                else:
                    section = str(hex(random.randint(1,16777215))).replace("0x","")
                    shelf = str(hex(random.randint(1,65535))).replace("0x","")
                box = str(hex(random.randint(1,65535))).replace("0x","")
                try:
                    os.mkdir(section)
                except:
                    verbose.log("Section already exists wont create a new one")
                os.chdir(section)
                try:
                    os.mkdir(shelf)
                except:
                    verbose.log("Shelf already exists wont create a new one")
                os.chdir(shelf)
                while True:
                    try:
                        os.mkdir(box)
                        break
                    except:
                        verbose.warn("Box already exists creating new box")
                os.chdir(box)

                f = open("TITLE.txt","w")
                f.write(title)
                f.close()
                f = open("DESCRIPTION.txt","w")
                f.write(description)
                f.close()
                f = open("AUTHOR.txt","w")
                f.write(author)
                f.close()
                f = open("DATE.txt","w")
                f.write(date)
                f.close()
                f = open("TYPE.txt","w")
                f.write(data_type)
                f.close()
                verbose.log("We are now boxing up your files and placing it in the warehouse if there are large files this will take time. Do not close the terminal.")
                make_tarfile(box+".tar.gz",location)
                print("Created archive at:"+os.getcwd())
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
            else:
                verbose.error("Not in a selected archive")
        if cmd.upper() == "SEARCH":
            term = input("Enter search term>")
            if in_archive == True:
                for root, subdirectories, files in os.walk(os.getcwd()):
                    for file in files:
                        if file == "TITLE.txt":
                            with open(os.path.join(root, file)) as f:
                                for line in f:
                                    if term in line:
                                        try:
                                            data_type = open(os.path.join(root, "TYPE.txt")).read()
                                        except:
                                            data_type = "None Set"
                                        verbose.log("Found in "+os.path.join(root, file).replace("TITLE.txt","")+" Data type:"+data_type)
                                        break
        if cmd.upper() == "EXIT" or cmd.upper() == "QUIT" or cmd.upper() == "E" or cmd.upper() == "Q":
            exit(0)
        
        