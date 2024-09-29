class Denomination:
    def __init__(self, coins=None):
        # Create empty coin list if no coin list provided
        self.coins = coins if coins is not None else []


