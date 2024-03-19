# Installation sur le roboRIO

Si ce n'est pas fait, commencez par les étapes d'[Installation sur l'ordinateur](/installation_ordinateur.md)

Commencez par installer la dernière version du firmware sur votre roboRIO ainsi que votre radio.

- [Pour le roboRIO 1](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/imaging-your-roborio.html)
- [Pour le roboRIO 2](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/roborio2-imaging.html)
- [Pour la radio](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/radio-programming.html)

## Installation RobotPy

Le robot n'est généralement pas capable de se connecter à internet. Il faut donc réaliser les commandes en 2 temps: Connecté sur Internet puis ensuite connecté sur le robot.

Si le terminal vous demande votre numéro d'équipe, saisissez-le. Cette information permet de trouver votre roboRIO sur le réseau.

### Installation de Python sur le roboRIO et mise à jours

Ouvrez un terminal (Powershell sur Windows) et écrivez les commandes suivantes:

```shell
#  Connecté sur internet
robotpy sync
#  Puis connecté sur le robot
robotpy deploy
```

**NOTE**: Pour activer ou désactiver des modules (Ex.: ctre, rev, navx), ajoutez ou retirez les de la liste `robotpy_extras` du fichier `pyproject.toml` de votre projet.

Une fois tout installé, validez le bon fonctionnement par le [Projet de Test](/patrons/projet_de_test/README.md)
