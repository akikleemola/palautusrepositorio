MIN_POINTS_TO_WIN = 4
WINNING_POINT_DIFFERENCE = 2

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def get_score(self):
        score = ""

        if self.player1_points == self.player2_points:
            score = self.get_tied_score()
            
        elif (self.player1_points >= MIN_POINTS_TO_WIN or self.player2_points >= MIN_POINTS_TO_WIN):
            score = self.get_advantage_or_win_score()

        else:
            player1_score = self.get_point_name(self.player1_points)
            player2_score = self.get_point_name(self.player2_points)
            score = f"{player1_score}-{player2_score}"

        return score

    def get_advantage_or_win_score(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == 1:
            score = "Advantage player1"
        elif point_difference == -1:
            score = "Advantage player2"
        elif point_difference >= WINNING_POINT_DIFFERENCE:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score

    def get_point_name(self, points):
        point_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return point_names[points]

    def get_tied_score(self):
        if self.player1_points == 0:
            score = "Love-All"
        elif self.player1_points == 1:
            score = "Fifteen-All"
        elif self.player1_points == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"

        return score
