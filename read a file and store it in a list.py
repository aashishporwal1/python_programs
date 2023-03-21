with open("FILE.txt") as file:
    content_list = file.readlines()

content_list = [x.strip() for x in content_list]
print(content_list)