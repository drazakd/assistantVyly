# # Importation des modules nécessaires
# import speech_recognition as sr
# import pyttsx3 as ttx
# import pywhatkit
# import webbrowser as wb
# import sys

# # Configuration du module Text-to-Speech (TTS)
# listener = sr.Recognizer()
# engine = ttx.init()  # Initialisation du moteur Text-to-Speech
# voices = engine.getProperty('voices')
# engine.setProperty('voice', 'french')  # Configuration de la voix en français

# # Fonction pour permettre à l'assistant de parler
# def parler(text):
#     engine.say(text)
#     engine.runAndWait()

# # Fonction pour écouter la voix de l'utilisateur via le microphone
# def ecouter():
#     command = ""
#     try:
#         with sr.Microphone() as source:
#             print("Parlez maintenant")
#             voix = listener.listen(source, timeout=9)  # Enregistrement de la voix pendant 9 secondes au maximum
#             command = listener.recognize_google(voix, language='fr-FR').lower()  # Reconnaissance vocale via Google
#             print(f"vous avez dit {str(command).capitalize()}")  # Affichage de ce que l'utilisateur a dit
#     except sr.UnknownValueError:
#         print("La reconnaissance vocale n'a pas pu comprendre l'audio")
#     except sr.RequestError as e:
#         print(f"Erreur lors de la requête à l'API Google Speech Recognition: {str(e)}")
#     except Exception as e:
#         print(f"Une erreur s'est produite: {str(e)}")
#     return command

# # Fonction principale de l'assistant
# def yly():
#     voix = ecouter()  # Récupération de la commande vocale de l'utilisateur
#     if voix is not None:  # Vérification si une commande a été détectée
#         if "arrete-toi" in voix.lower() or 'arretes-toi' in voix.lower():
#             parler("J'ai été ravie de vous avoir aidé")  # Message de sortie si l'utilisateur demande à arrêter
#             sys.exit()  # Arrêt du programme

#         if "recherche sur youtube" in voix.lower():
#             recherche_sur_youtube(voix)  # Recherche sur YouTube
#         elif "recherche sur google" in voix.lower():
#             recherche_sur_google(voix)  # Recherche sur Google
#         elif "youtube" in voix.lower():
#             jouer_sur_youtube(voix)  # Lecture de musique sur YouTube
#         elif any(word in voix.lower() for word in ["comment", "qui est", "quelle est", "quel est"]):
#             rechercher_wikipedia(voix)  # Recherche sur Wikipedia
#         else:
#             parler("Je suis juste en mesure de rechercher sur youtube, google et wikipedia")
#     else:
#         parler("Je n'ai pas bien compris")

# # Fonction pour la recherche sur YouTube
# def recherche_sur_youtube(voix):
#     url_index = voix.split().index("youtube") + 1
#     element_a_rechercher = voix.split()[url_index:]
#     parler("D'accord je lance la recherche sur youtube")
#     url_wb = "https://www.youtube.com/results?search_query=" + "+".join(element_a_rechercher)
#     wb.open(url_wb, new=2)

# # Fonction pour la recherche sur Google
# def recherche_sur_google(voix):
#     url_index = voix.split().index("google") + 1
#     element_a_rechercher = voix.split()[url_index:]
#     parler("D'accord je lance la recherche sur google")
#     url_wb = "https://www.google.com/search?q=" + "+".join(element_a_rechercher)
#     wb.open(url_wb, new=2)

# # Fonction pour jouer sur YouTube
# def jouer_sur_youtube(voix):
#     element_a_rechercher = voix.replace("youtube", "")
#     parler("D'accord je mets la musique sur youtube")
#     pywhatkit.playonyt(element_a_rechercher)

# # Fonction pour rechercher sur Wikipedia
# def rechercher_wikipedia(voix):
#     import wikipedia as wk
#     wk.set_lang("fr")
#     info_rech = wk.summary(voix, 1)
#     print(info_rech)
#     parler(str(info_rech))

# # Point d'entrée du script
# if __name__ == "__main__":
#     while True:
#         yly()







# import speech_recognition as sr
# import pyttsx3 as ttx
# import pywhatkit
# import webbrowser as wb
# import sys
# import wikipedia as wk

# # Configuration du moteur Text-to-Speech (TTS)
# engine = ttx.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', 'french')

# # Configuration du reconnaître de la voix
# listener = sr.Recognizer()

# # Fonction pour permettre à l'assistant de parler
# def parler(text):
#     engine.say(text)
#     engine.runAndWait()

# # Fonction pour écouter la voix de l'utilisateur via le microphone
# def ecouter():
#     try:
#         with sr.Microphone() as source:
#             print("Parlez maintenant")
#             voix = listener.listen(source, timeout=9)
#             command = listener.recognize_google(voix, language='fr-FR').lower()
#             print(f"Vous avez dit {command.capitalize()}")
#             return command
#     except Exception as e:
#         print(f"Une erreur s'est produite: {str(e)}")

# # Fonction principale de l'assistant
# def assistant():
#     command = ecouter()
#     if command:
#         if "arrete-toi" in command or 'arretes-toi' in command:
#             parler("J'ai été ravie de vous avoir aidé")
#             sys.exit()

#         if "recherche sur youtube" in command:
#             recherche_sur('youtube', command)
#         elif "recherche sur google" in command:
#             recherche_sur('google', command)
#         elif "youtube" in command:
#             jouer_sur_youtube(command)
#         elif any(word in command for word in ["comment", "qui est", "quelle est", "quel est"]):
#             rechercher_wikipedia(command)
#         else:
#             parler("Je suis juste en mesure de rechercher sur YouTube, Google et Wikipedia")
#     else:
#         parler("Je n'ai pas bien compris")

# # Fonction pour la recherche sur YouTube ou Google
# def recherche_sur(site, command):
#     url_index = command.split().index(site) + 1
#     element_a_rechercher = command.split()[url_index:]
#     parler(f"D'accord je lance la recherche sur {site}")
#     url_wb = f"https://www.{site}.com/results?search_query=" + "+".join(element_a_rechercher)
#     wb.open(url_wb, new=2)

# # Fonction pour jouer sur YouTube
# def jouer_sur_youtube(command):
#     element_a_rechercher = command.replace("youtube", "")
#     parler("D'accord je mets la musique sur YouTube")
#     pywhatkit.playonyt(element_a_rechercher)

# # Fonction pour rechercher sur Wikipedia
# def rechercher_wikipedia(command):
#     wk.set_lang("fr")
#     info_rech = wk.summary(command, 1)
#     print(info_rech)
#     parler(str(info_rech))

# # Point d'entrée du script
# if __name__ == "__main__":
#     while True:
#         assistant()


import tkinter as tk
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import webbrowser as wb
import wikipedia as wk
import sys


class AssistantInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assistant Vocal")

        self.engine = ttx.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'french')

        self.listener = sr.Recognizer()

        self.label = tk.Label(self, text="Parlez maintenant")
        self.label.pack()

        self.bouton = tk.Button(self, text="Activer l'assistant", command=self.assistant)
        self.bouton.pack()

    def parler(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def ecouter(self):
        try:
            with sr.Microphone() as source:
                voix = self.listener.listen(source, timeout=9)
                command = self.listener.recognize_google(voix, language='fr-FR').lower()
                self.label.config(text=f"Vous avez dit : {command.capitalize()}")
                return command
        except Exception as e:
            self.label.config(text=f"Une erreur s'est produite: {str(e)}")

    def assistant(self):
        command = self.ecouter()
        if command:
            if "arrete-toi" in command or 'arretes-toi' in command:
                self.parler("J'ai été ravie de vous avoir aidé")
                sys.exit()

            if "recherche sur youtube" in command:
                self.recherche_sur('youtube', command)
            elif "recherche sur google" in command:
                self.recherche_sur('google', command)
            elif "youtube" in command:
                self.jouer_sur_youtube(command)
            elif any(word in command for word in ["comment", "qui est", "quelle est", "quel est"]):
                self.rechercher_wikipedia(command)
            else:
                self.parler("Je suis juste en mesure de rechercher sur YouTube, Google et Wikipedia")

    def recherche_sur(self, site, command):
        url_index = command.split().index(site) + 1
        element_a_rechercher = command.split()[url_index:]
        self.parler(f"D'accord je lance la recherche sur {site}")
        url_wb = f"https://www.{site}.com/results?search_query=" + "+".join(element_a_rechercher)
        wb.open(url_wb, new=2)

    def jouer_sur_youtube(self, command):
        element_a_rechercher = command.replace("youtube", "")
        self.parler("D'accord je mets la musique sur YouTube")
        pywhatkit.playonyt(element_a_rechercher)

    def rechercher_wikipedia(self, command):
        wk.set_lang("fr")
        info_rech = wk.summary(command, 1)
        print(info_rech)
        self.parler(str(info_rech))


if __name__ == "__main__":
    app = AssistantInterface()
    app.mainloop()











