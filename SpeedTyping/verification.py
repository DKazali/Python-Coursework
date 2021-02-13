class Verification:
    attempts = 0
    Mode = None
    win_lose = None

    def set_mode(self, m):
        self.Mode = m

    def ver(self, random, user):
        if random == user:
            return True
        else:
            self.attempts += 1
            return False

    def reset_attempts(self):
        if self.attempts > 0:
            self.attempts = 0

    def n_attempts(self):
        if self.Mode == 'Normal' and self.attempts >= 5:
            self.win_lose = 'Lose'
            return self.win_lose
        else:
            self.win_lose = 'Win'
        if self.Mode == 'Hard' and self.attempts >= 3:
            self.win_lose = 'Lose'
            return self.win_lose
        else:
            self.win_lose = 'Win'
        if self.Mode == 'Extreme' and self.attempts >= 1:
            self.win_lose = 'Lose'
            return self.win_lose
        else:
            self.win_lose = 'Win'
