#-*- coding: utf8 -*-
"""Game module. Handles the rules, etc
"""
import random


class Combinations(object):

    def __init__(self, dices):
        self.dices = dices

    @property
    def chouette(self):
        temp = {}
        for d in self.dices:
            if d not in temp:
                temp[d] = 0
            temp[d] += 1
        for key, value in temp.items():
            if value == 2:
                return key ** 2
        return 0

    @property
    def velute(self):
        if self.dices[0] == (self.dices[1] + self.dices[2]):
            return (self.dices[0] ** 2) * 2
        if self.dices[1] == (self.dices[0] + self.dices[2]):
            return (self.dices[1] ** 2) * 2
        if self.dices[2] == (self.dices[0] + self.dices[1]):
            return (self.dices[2] ** 2) * 2
        return 0

    @property
    def chouette_velute(self):
        temp = sorted(self.dices)
        if temp in ([1, 1, 2], [2, 2, 4], [3, 3, 6],):
            return (temp[-1] ** 2) * 2
        return 0

    @property
    def cul_de_chouette(self):
        temp = set(self.dices)
        if len(temp) == 1:
            return 40 + 10 * list(temp)[0]
        return 0

    @property
    def suite(self):
        temp = sorted(self.dices)
        if temp in ([1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]):
            return True
        return False

    def resultat(self):
        lines = []
        score = 0
        is_suite = False
        if self.chouette_velute:
            lines.append("Chouette Velute: %d" % self.chouette_velute)
            score = self.chouette_velute
        elif self.chouette:
            lines.append("Chouette: %d" % self.chouette)
            score = self.chouette
        elif self.velute:
            lines.append("Velute: %d" % self.velute)
            score = self.velute
        if self.cul_de_chouette:
            lines.append("Cul de Chouette: %d" % self.cul_de_chouette)
            score = self.cul_de_chouette
        if self.suite:
            is_suite = True
            lines.append("Suite ! Tout le monde doit dire")
            lines.append("     'Grelotte ça picote'")
            lines.append("Le dernier joueur perd 10 points")
            # lines.append(u"En cas d'égalité, les joueurs se départagent en criant")
            # lines.append(u"     Sans fin est la moisissure des bières bretonnes")
            # lines.append(u"Toujours égalité ? jeter les dés, le moins fort perd 20 points.")
            # lines.append(u"Si toujours égalité, on recommence pour perdre 30 points, 40 points, etc.")
        if not lines:
            lines.append('Néant... tu gagnes une grelottine')
        return score, lines, is_suite


class Game(object):

    def __init__(self):
        self.gamers = {}
        self.started = False
        self.opened_registration = True
        self.in_suite = False
        self.grelotte = []

    def stop(self):
        "Stop game"
        self.started = False

    def start(self):
        "Start game"
        self.started = True
        self.turns = self.gamers.keys()
        random.shuffle(self.turns)
        self.current = 0

    def next(self):
        "Move turn to the next gamer"
        self.current += 1
        if self.current >= len(self.turns):
            self.current = 0
        # get outside any special rules
        self.in_suite = False

    @property
    def current_gamer(self):
        "Return current gamer"
        return self.turns[self.current]

    def dices(self):
        "Return a triple dice roll"
        return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

    @property
    def in_special_rule(self):
        "Return 'True' if we're in a special rule process"
        return self.in_suite
