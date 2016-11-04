from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    join_year = models.IntegerField(default=1993)

    def __str__(self):
        return self.team_name


class Game(models.Model):
    RESULT_CHOICES = (
     ('WN', '勝利'),
     ('LS', '敗北'),
     ('DR', '引き分け'),
     ('YT', '未実施')
    )
    team = models.ForeignKey(Team, related_name='team')
    opponent = models.ForeignKey(Team, related_name='opponent_team')
    year = models.IntegerField(default=0)
    result = models.CharField(max_length=2, choices=RESULT_CHOICES,
                              default='YT')
