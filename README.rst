===================
Cul De Chouette Bot
===================

Warning, this Cul de Chouette Bot is Français !

Bon, pour que ça marche, ça doit être installé avec la version "dev" de
`CmdBot <https://github.com/brunobord/cmdbot>`_.

Tu l'installes, tu le lances "normalement" (avec un fichier de conf en ".ini",
faut suivre la doc de CmdBot)

Les règles
==========

Pour le moment, on utilise les règles les plus simples possibles. À savoir, les
combinaisons de base :

* Chouette,
* Velute,
* Chouette Velute
* Cul de Chouette
* Suite (dans le cadre de la suite, on doit dire "grelotte ça picote".
  Normalement, il ne peut pas y avoir d'ex-aequo.)

Les autres règles seront (peut-être) implémentées dans le futur. Si tu es sage.

Commandes
=========

.. note::

    Les commandes indiquées comme *direct* doivent être précédées du nom du bot.
    Genre::

        <No` > cmdbot: init


.. note::

    Les commandes indiquées comme "admin" ne peuvent être lancées que par un des
    admins définis dans la configuration.

* `init` : [*direct*, *admin*] - démarre les inscriptions au jeu.
* `moi` : s'inscrire au jeu
* `start` ou `commencer`: [*direct*, *admin*] - une fois les inscriptions terminées, on démarre
  le jeu.
* `roll` ou `jouer`: le joueur dont c'est le tour lance les dés.
* `scores`: indique les scores des joueurs.
* `status` ou `statut`: [*direct*] - donne le statut du jeu et le score.
* `stop`: [*direct*, *admin*] - arrête la partie
* `clean` ou `virer` : [*direct*, *admin*] - vire un joueur de la partie. **ATTENTION !** Cette fonction nécessite la
  version "GIT" de `CmdBot <https://github.com/brunobord/cmdbot>`_.
