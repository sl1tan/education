str = input()
new = str[str.find("h") + 1: str.rfind("h")].replace("h", "H")
print(str[:str.find("h") + 1] + new + str[str.rfind("h"):])
