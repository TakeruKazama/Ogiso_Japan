from django.db import models


class Player(models.Model):
    class Meta:
        verbose_name = '選手'

    name = models.CharField(max_length=100)


class Event(models.Model):
    class Meta:
        verbose_name = '大会'

    RULE_CHOICES = (
        (0, '総当たり'),
        (1, 'トーナメント'),
    )

    name = models.CharField(max_length=100)
    rule = models.CharField(choices=RULE_CHOICES, default=0)
    set_to_win = models.IntegerField(default=3)
    member = models.ManyToManyField(Player)


class Game(models.Model):
    class Meta:
        verbose_name = '試合の組み合わせ'

    event = models.ForeignKey(Event)
    match_number = models.IntegerField()
    player1 = models.ForeignKey(Player)
    player2 = models.ForeignKey(Player)


class Point(models.Model):
    class Meta:
        verbose_name = '得点'

    game = models.ForeignKey(Game)
    set_number = models.IntegerField()
    player1_point = models.IntegerField()
    player2_point = models.IntegerField()
