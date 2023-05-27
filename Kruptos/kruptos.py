# Import des bibliothèques nécessaires
import click
import requests
from termcolor import colored
import pyfiglet
from tabulate import tabulate

# Fonction pour afficher l'en-tête du programme
def print_header():
    # Affichage d'un espace supplémentaire
    print("\n\n")
    # Conversion du texte "Kruptos" en art ASCII
    banner = pyfiglet.figlet_format("Kruptos", font="pagga")
    # Affichage du texte "Kruptos" en rouge
    print(colored(banner, 'red'))

# Affichage de l'en-tête à l'ouverture du programme
print_header()

# Fonction pour vérifier le nom d'utilisateur sur différents sites
def check_username(username):
    # Dictionnaire contenant les sites et leurs URL de profil correspondantes
    sites = {
        'Facebook': f'https://www.facebook.com/{username}',
        'YouTube': f'https://www.youtube.com/user/{username}',
        'WhatsApp': f'https://api.whatsapp.com/send?phone={username}',
        'Instagram': f'https://www.instagram.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'Pinterest': f'https://www.pinterest.com/{username}/',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'VK': f'https://vk.com/{username}',
        'Snapchat': f'https://www.snapchat.com/add/{username}',
        'GitHub': f'https://github.com/{username}',
        'SoundCloud': f'https://soundcloud.com/{username}',
        'Spotify': f'https://open.spotify.com/user/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}',
        'Medium': f'https://medium.com/@{username}',
        'Twitch': f'https://www.twitch.tv/{username}',
        '9GAG': f'https://9gag.com/u/{username}',
        'Behance': f'https://www.behance.net/{username}',
        'TradingView': f'https://www.tradingview.com/u/{username}/',
        'Kik': f'https://kik.me/{username}',
        'Giphy': f'https://giphy.com/{username}',
        'Genius': f'https://genius.com/{username}',
        'Fiverr': f'https://www.fiverr.com/{username}',
        'Freelancer': f'https://www.freelancer.com/u/{username}',
        'Imgur': f'https://imgur.com/user/{username}',
        'Roblox': f'https://www.roblox.com/user.aspx?username={username}',
        'Duolingo': f'https://www.duolingo.com/profile/{username}',
        'Codecademy': f'https://www.codecademy.com/profiles/{username}',
        'Bitbucket': f'https://bitbucket.org/{username}/',
        'Askfm': f'https://ask.fm/{username}'
    }

    # Liste pour stocker les résultats
    results = []

    # Pour chaque site et URL dans le dictionnaire
    for site, url in sites.items():
        try:
            # Effectuer une requête GET à l'URL
            response = requests.get(url)
            # Si le statut de la réponse est 200 (OK), l'utilisateur existe
            if response.status_code == 200:
                # Ajouter le résultat à la liste des résultats
                results.append([site, colored("True", 'green'), url])
            else:
                # Ajouter le résultat à la liste des résultats
                results.append([site, colored("False", 'red'), ""])
        # Attraper toute exception provenant de la requête
        except requests.RequestException as e:
            # Ajouter le résultat à la liste des résultats
            results.append([site, colored("Error", 'yellow'), str(e)])

    # Retourner les résultats
    return results

# Définition de la fonction principale
@click.command()
@click.option('--username', prompt='Veuillez entrer le nom d\'utilisateur à vérifier',
              help='Le nom d\'utilisateur à vérifier.')
def main(username):
    # Obtenir les résultats en appelant la fonction check_username
    results = check_username(username)
    # Affichage des résultats sous forme de tableau
    print(tabulate(results, headers=['Site', 'Existe', 'URL/Erreur']))

# Si ce fichier est exécuté en tant que script principal, exécutez la fonction principale
if __name__ == "__main__":
    main()