#main
from scenes.menu import MainMenu
from config.settings import Settings

# Cria o menu
game_settings = Settings()
menu = MainMenu(game_settings.screen_width, game_settings.screen_height)

# Start the main loop
menu.main_loop()

