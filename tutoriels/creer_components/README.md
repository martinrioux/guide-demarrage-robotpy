# Comment créer un nouveau 'component'

Le code inclus un example de création d'un composant simple.

Dans ce cas ci, supossont que nous voulons rajouter un covoyeur qui stop dès qu'un actuateur est actionné (objet présent).

La première étape est de créer un fichier pour cette composante dans `./components/convoyeur_driver.py`.

On doit spécifier les mécanismes (moteurs, actuateurs et autre components) dans ce fichier

Supposont que notre convoyeur est composé d'un moteur sparkmax et un actionneur (limit switch) sur un port digitale du roboRIO

Commencez par aller voir le contenu du fichier [convoyeur_driver.py](./components/convoyeur_driver.py), puis par la suite [robot.py](./robot.py)

Un exemple d'utilisation du 'component' en mode autonome est retrouvé dans [auto_modes.py](./autonomous/auto_modes.py)
