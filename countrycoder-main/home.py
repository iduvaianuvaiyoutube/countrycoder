
print("     ████████████████████████████████")
print("     █            █████             █")
print("                ██ █ ██")
print("              ██   █   ██")
print("             ██    █    ██")
print("            ██     █     ██")
print("          ███████████████████")
print("         ██        █         ██")
print("        ██     ╔══╗█╔══╗      ██")
print("       ██      ╚║║╝█║╔╗║       ██")
print("      ██       ╔║║╗█║╠╣║        ██   ")
print("    ██         ╚══╝█╚╝╚╝         ██")
print("   █████████████████████████████████")
print("   ╔══╗╔╗        ╔╗ ╔══╗           ╔╗")
print("   ╚║║╬╝╠╦╦═╦═╦═╗╠╣ ║╔╗╠═╦╦╦╦═╦═╦═╗╠╣")
print("   ╔║║╣╬║║╠╗║╔╣╬╚╣║ ║╠╣║║║║║╠╗║╔╣╬╚╣║")
print("   ╚══╩═╩═╝╚═╝╚══╩╝ ╚╝╚╩╩═╩═╝╚═╝╚══╩╝")



import os



print("██╗ █████╗        █████╗  █████╗ ██╗   ██╗███╗  ██╗████████╗██████╗ ██╗   ██╗")
print("██║██╔══██╗      ██╔══██╗██╔══██╗██║   ██║████╗ ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝")
print("██║███████║█████╗██║  ╚═╝██║  ██║██║   ██║██╔██╗██║   ██║   ██████╔╝ ╚████╔╝ ")
print("██║██╔  ██║╚════╝██║  ██╗██║  ██║██║   ██║██║╚████║   ██║   ██╔══██╗  ╚██╔╝  ")
print("██║██║  ██║      ╚█████╔╝╚█████╔╝╚██████╔╝██║ ╚███║   ██║   ██║  ██║   ██║   ")
print("╚═╝╚═╝  ╚═╝       ╚════╝  ╚════╝  ╚═════╝ ╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ")

print("                Hi there! Welcome to Country Coder Tool Set\n")
print("Please select below numbers to visit tools\n")
print("1. Country Coder\n2. Info\n3. Conversation\n4. game\n")

while True:
    user_input = input("Enter the tool number : ")

    if user_input.lower() == 'exit':
        print("Thank you for using Country Coder Tool Set")
        break

    elif user_input == "1":
        file_path = "C:\\Users\\gcc\\Desktop\\countrycoder-main\\country_coder.py"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                code = file.read()
                exec(code)
        except FileNotFoundError:
            print(f"File not found. Please make sure '{file_path}' exists.")

    elif user_input == "2":
        print("Some information about the Info tool.")
        file_path = "C:\\Users\\gcc\\Desktop\\countrycoder-main\\info.py"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                code = file.read()
                exec(code)
        except FileNotFoundError:
            print(f"File not found. Please make sure '{file_path}' exists.")

    elif user_input == "3":
        file_path = "C:\\Users\\gcc\\Desktop\\countrycoder-main\\conversation.py"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                code = file.read()
                exec(code)
        except FileNotFoundError:
            print(f"File not found. Please make sure '{file_path}' exists.")            


    else:
        print("Sorry, I can't recognize your input. Please try again. If you want to exit, type 'exit'.")
