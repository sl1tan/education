str = input()
reverse_substr = str[str.find("h"):str.rfind("h") + 1]
reverse_substr = reverse_substr[::-1]
print(str[:str.find("h")] + reverse_substr + str[str.rfind("h") + 1:])
