list_name =[]
PLACEHOLDER ="[name]"
with open("../../../Desktop/file_3.txt") as file:
    # for i in file:
    contens = file.readlines()
        # list_name.append(contens)
        # print(contens)
# print(list_name)
# f = open("file_3 .txt","x")
# /Users/Admin/Desktop/file_3.txt
with open("starting_letter.txt") as letter_file:

    letter_file = letter_file.read()
    for i in contens:
        bien =  i.strip()
        new_letter = letter_file.replace(PLACEHOLDER,bien)
        # print(new_letter)
        with open(f"for_letter_{bien}.txt",mode="w") as file_name_new:
            file_name_new.write(new_letter)