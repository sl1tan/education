str = input()
print(str[:str.find("h")] + str[str.rfind("h") + 1:])
