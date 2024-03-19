# Projet de test

Projet permettant de tester que RobotPy est bien installé, ainsi qu'un apperçu des bases de RobotPy

Le projet de test utilise la base `TimedRobot`
```python
class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
```

Il s'agit d'une approche facile pour réaliser un robot, mais qui peut-être limitante pour un robot plus complexe.

C'est pour cette raison que `MagicRobot` est employé dans les autres patrons de projet.

## Démarrage

Commencez par copier le dossier `projet_de_test` au complet sur votre ordinateur et ouvrez ce dossier avec Visual Studio Code

Il est possible que VS Code vous pose cette question.

![alt text](/media/authoriser.png "Popup faire confiance apparait")

Cocher que vous faites confiance à l'auteur.

Pour vous assurer que Python est bien reconnu et les librairies bien installées, ouvrez le fichier robot.py et validez que dans la section `import`, le texte soit en vert. Ceci est signe que Visual Studio Code ainsi que RobotPy sont bien installés.

![alt text](/media/import-ok.png "import en vert")

Avoir VS Code bien configuré est important, car il permet entre autres d'examiner les fonctions possibles via l'IntelliSense. Par exemple, pour voir les modules existants de CTRE:

![alt text](/media/ctre-intellisense.png "Boite des choix de CTRE")

Ceci est également vrai pour voir les possibilités d'une variable déclarée

![alt text](/media/rev-intellisense.png "REV class")

Et lors que vous rajoutez les (), cela permet également de voir les arguments à donner à la méthode

![alt text](/media/rev-intellisense2.png "REV method args")

## Téléversement du code dans le robot

Afin de téléverser votre code dans le robot, le plus simple et d'ouvrir un terminal depuis VS Code.

![alt text](/media/nouveau-terminal.png "Terminal -> New Terminal")

Une nouvelle fenêtre va apparaitre dans le bas de l'éditeur. Dans cette dernière, écrire la commande suivante:

```shell
robotpy
```

![alt text](/media/terminal-1.png "Terminal 1")

Le résultat affiché vous montre les différentes possibilités les plus intéressants sont:
- deploy: Déploie le code sur le roboRIO. En cas de redémarrage, le code sera exécuté automatiquement. Bon pour les compétitions et essais finaux.
- sim: Démarrer le logiciel de simulation sur votre ordinateur.
- undeploy: Arrêter l'exécution automatique du code Python sur votre robot.

Plus particulièrement, vous pouvez exécuter la commande `deploy --nc`. Cela va ouvrir une netconsole qui vous permettra d'avoir directement dans votre terminal un retour d'information sur le robot. Vous y verrez également les commandes `print(...)` réalisées dans votre code.

**NOTE**: Bien que la commande `print()` est bien utile au débogage, en abuser peut ralentir l'exécution du code du robot.

La première fois, le numéro de votre équipe vous sera demandé afin de trouver votre roboRIO sur le réseau.

Vous devriez voir se répéter la ligne `Connecting to ........ `

![alt text](/media/deploy-nc.png "deploy --nc")

À partir de ce point, vous pouvez lancer le logiciel `Driver Station` officiel de la FRC et vous connecter à votre robot!

Utilisez ce projet afin de tester des pièces individuelles de robot et vous familiariser aux possibilités.

Pour un projet plus complet, allez voir les autres patrons de projet.
