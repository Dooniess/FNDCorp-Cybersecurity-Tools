# Importation des bibliothèques nécessaires
import requests
from termcolor import colored

# Définition de la fonction pour vérifier le nom d'utilisateur
def check_username(username):
    # Dictionnaire des sites avec les URL de profil correspondantes
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

    # Pour chaque site et URL dans le dictionnaire
    for site, url in sites.items():
        try:
            # Faites une requête GET à l'URL
            response = requests.get(url)
            # Si le statut de la réponse est 200 (OK), l'utilisateur existe
            if response.status_code == 200:
                # Imprimez "True" en vert
                print(colored(f"{site}: True", 'green'))
                # Affichez le lien vers le profil
                print(f"\tLink: {url}")
            else:
                # Sinon, imprimez "False" en rouge
                print(colored(f"{site}: False", 'red'))
        # Attrapez toute exception provenant de la requête
        except requests.RequestException as e:
            # Imprimez l'erreur
            print(f"Une erreur s'est produite lors de la vérification de {site}: {e}")

# Définition de la fonction principale
def main():
    # Demandez à l'utilisateur le nom d'utilisateur à vérifier
    username = input("Veuillez entrer le nom d'utilisateur à vérifier : ")
    # Appellez la fonction check_username avec le nom d'utilisateur en entrée
    check_username(username)

# Si ce fichier est exécuté en tant que script principal, exécutez la fonction principale
if __name__ == "__main__":
    main()
