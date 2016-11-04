from django.db import models


class Team(models.Model):
    """チーム"""
    name = models.CharField('チーム名', max_length=100)

    def points(self):
        """勝ち点"""
        return len(self.win.all()) * 3 + len(self.draw.all())

    def total_match_num(self):
        """試合数"""
        return len(self.win.all())+len(self.draw.all())+len(self.lose.all())

    def score(self):
        s = 0
        for x in self.win.all():
            s += x.winner_score
        for x in self.draw.all():
            s += x.draw_score
        for x in self.lose.all():
            s += x.loser_score
        return s

    def anscore(self):
        s = 0
        for x in self.win.all():
            s += x.loser_score
        for x in self.draw.all():
            s += x.draw_score
        for x in self.lose.all():
            s += x.winner_score
        return s

    def score_dif(self):
        return self.score()-self.anscore()

    def __str__(self):
        return self.name


class Match(models.Model):
    winner = models.ForeignKey(Team, related_name='win', blank=True, null=True)
    loser = models.ForeignKey(Team, related_name='lose', blank=True, null=True)
    draw = models.ManyToManyField(Team, related_name='draw', blank=True)
    winner_score = models.IntegerField('勝者の点数', default=0)
    loser_score = models.IntegerField('敗者者の点数', default=0)
    draw_score = models.IntegerField('引き分け時の点数', default=0)
