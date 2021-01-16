class GameStats:
    """Track game statistics"""

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """
        Resets the statistics that can change during the game
        """
        self.ships_left = self.game_settings.ship_limit