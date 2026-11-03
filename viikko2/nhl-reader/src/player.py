class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict["nationality"]
        self.team = player_dict["team"]
        self.goals = player_dict["goals"]
        self.assists = player_dict["assists"]
    
    def __str__(self):
        pisteet = self.goals + self.assists

        return (
            f"{self.name:22} {self.team:15} "
            f"{self.goals:2} + {self.assists:2} = {pisteet:3}"
        )
