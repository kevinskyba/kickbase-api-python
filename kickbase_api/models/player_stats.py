class PlayerStats():
    market_value_change: int = None
    market_value_change_percent: float = None

    def __init__(self, d: dict = {}):
        self.market_value_change = d['leaguePlayer']['marketValueChange']
        self.market_value_change_percent = d['leaguePlayer']['marketValueChangePercent']
