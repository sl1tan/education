import module as m

Game_set1 = m.Settings("m4", "usp", "bayonete")
Game_set2 = m.Settings()
Game_set2.change_settings(new_main="q")
Game_set1.print_setting()
Game_set2.print_setting()