class Key():
    def __init__(self, gun: str, key: str):
        self.gun = gun
        self.key = key

    def change(self, new_key: str):
        self.key = new_key


class Settings():
    def __init__(self, main_gun="ak-47", alt_gun="glock", melee_gun="knife"):
        self.main = Key(main_gun, 1)
        self.alt = Key(alt_gun, 2)
        self.melee = Key(melee_gun, 3)

    def change_settings(self, *,  new_main: str = "1", new_alt: str = "2", new_melee: str = "3"):
        self.main.change(new_main)
        self.alt.change(new_alt)
        self.melee.change(new_melee)

    def print_setting(self):
        print(self.main.gun, self.main.key)
        print(self.alt.gun, self.alt.key)
        print(self.melee.gun, self.melee.key)


my_set = Settings()

print(my_set.alt.gun)
my_set.change_settings(new_main="mouse4", new_melee="mouse5", new_alt="1")
my_set.print_setting()
