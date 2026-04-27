"""Game Stats module — tracks statistics for the Alien Invasion game."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Tracks statistics for the Alien Invasion game.

    Statistics include the current score, high score, max score,
    current level, and ships remaining.
    """

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize statistics.

        Args:
            game: The main AlienInvasion game instance.
        """
        self.settings = game.settings
        self.reset_stats()

        # High score persists across games
        self.high_score: int = 0
        self.game_active: bool = False
        self.game_over: bool = False

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left: int = self.settings.ship_limit
        self.score: int = 0
        self.level: int = 1
        self.max_score: int = 0