# Installation sur l'ordinateur

Notez que les plateformes supportées sont:

- Windows 10 ou plus
- Ubuntu 22.04 ou plus
- macOS 11 ou plus

## Installation Outils de Jeu FRC et Visual Studio Code

Commencez par installer les [Outils de Jeu FRC](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-2/frc-game-tools.html) sur votre ordinateur.

Il est suggéré d'installer [Visual Studio Code](https://code.visualstudio.com/download) séparément plutôt qu'avec les Outils de Jeu.

Ouvrez VS Code et installez l'extension de Python. Il s'agit d'un outil pour assister au développement de code Python.

![alt text](/media/python-ext.png "Menu Extension à gauche -> Recherchez Python et installez le premier résultat (officiel de Microsoft)")

## Installation Python

Une version de Python entre 3.8 et 3.11 doit être installée:
- [Python pour Windows](https://www.python.org/downloads/windows/)
- [Python pour macOS](https://www.python.org/downloads/macos/)
- Python devrait déjà être installé pour Linux

Lors de l'installation, cochez Add python.exe to PATH

![alt text](/media/python-windows.png "Add python.exe to PATH")

Vous pouvez également désactiver la limite de longueur de PATH

![alt text](/media/python-path-limit.png "Disable Path Length Limit")

## Installation RobotPy

Ouvrez un terminal (Powershell sur Windows) et écrivez les commandes suivantes:

```shell
# Pour Windows
py -3 -m pip install robotpy

# Pour Windows si vous n'avez pas les droits administrateur
py -3 -m pip install --user robotpy[

# Pour Linux et macOS
pip3 install robotpy

# Pour Linux et macOS si vous n'avez pas les droits administrateur
pip3 install --user robotpy

```

Pour les habitués, il est également possible d'installer RobotPy dans un environnement virtuel [venv](https://docs.python.org/3/library/venv.html)

Vous pouvez maintenant poursuivre avec l'[Installation sur le roboRIO](/installation_roborio.md)

## Mettre à jours RobotPy

Ajustez le fichier `pyproject.toml` de votre projet selon vos besoins.

Ouvrez un terminal (Powershell sur Windows) et écrivez les commandes suivantes:

```shell
robotpy sync
```

Le RoboRIO sera mis à jours à la prochaine commande `robotpy deploy`

**NOTE**: Pour activer ou désactiver des modules (Ex.: ctre, rev, navx), ajoutez ou retirez les de la liste `robotpy_extras` du fichier `pyproject.toml` de votre projet.
