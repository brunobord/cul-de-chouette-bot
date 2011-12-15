#!/usr/bin/env python
#-*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG)
from cmdbot.core import Bot
from cmdbot.decorators import admin, direct
from game import Game, Combinations


def in_game(f):
    "Decorator: only process if the game is initialised"
    def newfunc(bot, line):
        if bot.game:
            return f(bot, line)
    return newfunc


def in_running_game(f):
    "Decorator: only process if the game is running"
    def newfunc(bot, line):
        if bot.game and bot.game.started:
            return f(bot, line)
    return newfunc


def not_in_special_rule(f):
    "Decorator: do not process if the game is in a special rule case"
    def newfunc(bot, line):
        if not bot.game.in_special_rule:
            return f(bot, line)
    return newfunc


class CulDeChouetteBot(Bot):

    welcome_message = "Salut la compagnie ! Ça vous dirait un cul-de-chouette ?"
    exit_message = "Allez, ciao les enfants. Soyez sages."

    @property
    def game(self):
        if not hasattr(self, '_game'):
            self._game = Game()
        return self._game

    @direct
    @admin
    def do_init(self, line):
        "Initialise a game"
        logging.info('ici')
        if hasattr(self, 'game') and self.game.started:
            self.say("Non, on ne peut pas.")
            return
        self.say('Le jeu est prêt à commencer')
        self.say('Qui veut jouer ? (dire "moi")')

    @direct
    @admin
    @in_game
    def do_start(self, line):
        "Start the game"
        if len(self.game.gamers) < 3:
            self.say('Pas assez de joueurs. Inscrivez-vous en disant "moi"')
            return
        self.game.start()
        self.say('Ça démarre... qui commence ?...')
        self.say("c'est au tour de '%s'" % self.game.current_gamer)

    @in_game
    def do_scores(self, line):
        "Say the gamer list, with scores"
        s = []
        for nick, score in self.game.gamers.items():
            s.append('%s (%d)' % (nick, score))
        self.say('Inscrits: %s' % ', '.join(s))

    @in_game
    def do_moi(self, line):
        "Register the user"
        if line.nick_from not in self.game.gamers:
            self.game.gamers[line.nick_from] = 0
            self.say('%s est inscrit' % line.nick_from)
        else:
            self.say('déjà inscrit...')

    @in_game
    @in_running_game
    @not_in_special_rule
    def do_roll(self, line):
        "Roll the dice if it's your turn"
        if line.nick_from == self.game.current_gamer:
            dices = self.game.dices()
            self.say('Les dés: %s' % ', '.join(map(str, dices)))
            c = Combinations(dices)
            score, messages, is_suite = c.resultat()
            for message in messages:
                self.say(message)
            if is_suite:
                self.game.in_suite = True
                self.game.grelotte = []
                return  # nothing else to do ATM
            if score > 0:
                self.say('%s gagne %d points' % (line.nick_from, score))
                self.game.gamers[line.nick_from] += score

            if self.game.gamers[line.nick_from] >= 343:
                self.say("Le jeu est terminé ! C'est *%s* qui a gagné !" % str(line.nick_from))
                self.game.stop()
                return

            self.game.next()
            self.say("c'est au tour de '%s'" % self.game.current_gamer)
        else:
            self.say("C'est pas ton tour, manant !")

    def do_grelotte(self, line):
        "Grelotte ca picote"
        if self.game.in_suite:
            grelotte_line = ' '.join(line.message.split())
            if grelotte_line.startswith(u'grelotte ça picote') \
                    or grelotte_line.startswith(u'grelotte ca picote'):
                if line.nick_from not in self.game.grelotte:
                    self.game.grelotte.append(line.nick_from)
            # check if everyone's here
            difference = list(set(self.game.gamers.keys()).difference(set(self.game.grelotte)))
            if len(difference) == 1:
                gamer_nick = difference[0]
                self.say('%s perd 10 points' % (gamer_nick))
                self.game.gamers[gamer_nick] -= 10
                self.game.next()
                self.say("c'est au tour de '%s'" % self.game.current_gamer)

        else:
            # TODO: handle bevue
            self.say('Bévue !')

    @direct
    @admin
    def do_stop(self, line):
        "Stop the current game"
        self.say('Le jeu est arrêté')
        self.brain.game.stop()


if __name__ == '__main__':
    bot = CulDeChouetteBot()
    bot.run()
