capitals = {}
capitals["RU"] = "Moscow"
capitals["UK"] = "Kiev"
capitals["USA"] = "Washington"

for country in capitals:
    print(capitals[country])

print(*capitals.keys())
print(capitals.get("RU"))