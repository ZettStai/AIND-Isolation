

# Helper Functions

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return not bool(gameState.get_legal_moves())  # by Assumption 1


def min_value(self,game,depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(game):
        return 1  # by Assumption 2
    v = float("inf")
    for m in game.get_legal_moves():
        v = min(v, max_value(game.forecast_move(m),depth - 1))
    return v


def max_value(self,game,depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if self.time_left() < self.TIMER_THRESHOLD:
        raise SearchTimeout()
    if depth == 0:
        return self.score(game, self)

    if terminal_test(game):
        return -1  # by assumption 2
    v = float("-inf")
    for m in game.get_legal_moves():
        v = max(v, min_value(game.forecast_move(m), depth - 1))
    return v