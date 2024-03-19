
import rev
import wpilib
from dataclasses import dataclass
from magicbot import tunable, will_reset_to


# Classe de configuration de notre module, facultatif
@dataclass
class ConvoyeurConfig:
    inverser_convoyeur: bool = False


class Convoyeur:
    # On définis le matériel ici, mais ne pas oublier de le déclarer dans robot.py
    # Par exemple, dans le fichier robot.py, dans la fonction `createObjects(self)`, on s'attends à retrouver les lignes:
    # convoyeur_config = ConvoyeurConfig(vitesse=0.5)
    # convoyeur_moteur = rev.CANSparkMax(5)
    # convoyeur_actuateur = wpilib.DigitalInput(0)
    moteur: rev.CANSparkMax
    actuateur: wpilib.DigitalInput
    config: ConvoyeurConfig

    # Les `tunable` sont accessible depuis les Network Tables pour facilement modifier la valeur en temps réel
    vitesse_max = tunable(1)

    # Les `will_reset_to` sont des variables remises automatiquement à une valeur par défaut après chaque boucle
    __forcer_a_tourner = will_reset_to(False)

    def setup(self):
        """
        Appelé après l'injection
        """
        self.moteur.setOpenLoopRampRate(0.5)  # Limite l'accélération du moteur

    def forcer_a_tourner(self):
        """
        Force le convoyeur à tourner même si l'actuateur n'est pas activé
        """
        self.__forcer_a_tourner = True

    def objet_present(self) -> bool:
        """
        Retourne True si un objet est détecté
        """
        return self.actuateur.get()

    def execute(self):
        """
        Cette fonction est appelé à chaque itération/boucle
        C'est ici qu'on doit écrire la valeur dans nos moteurs
        """

        # Par défaut, le convoyeur ne tourne pas
        vitesse = 0

        # Si l'objet n'est pas détecté et qu'on reçoit la commande "forcer_a_tourner_convoyeur()" le convoyeur tourne
        if not self.objet_present() and self.__forcer_a_tourner:
            vitesse = self.vitesse_max

        # Selon la configuration, on inverse le convoyeur
        if self.config.inverser_convoyeur:
            vitesse = -vitesse

        # On écrit la vitesse dans le moteur, c'est ce qui le fera tourner
        self.moteur.set(vitesse)

        # self.__forcer_a_tourner est remis à zéro automatiquement due à: will_reset_to(False)
