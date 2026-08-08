import re
def rearrange_name(name):
        x= re.search(r"^([\w .]+), ([\w .]+)$",name)
        print(x[2],x[1])