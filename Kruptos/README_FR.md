<div align="center"><h2><b>Kruptos</b></h2></div>

<p align="center"><img src="..\logo.png" alt="Logo" width="400" height="400"></p>

Kruptos est un outil basé sur Python qui permet de vérifier la présence d'un nom d'utilisateur donné sur une variété de sites web populaires. Il permet aux utilisateurs de voir rapidement où un nom d'utilisateur spécifique est utilisé.

## Installation

Vous avez besoin de Python 3.6 ou d'une version ultérieure pour utiliser Kruptos. Vous pouvez avoir plusieurs versions de Python (2.x et 3.x) installées sur le même système sans problème. Dans Ubuntu, vous pouvez installer Python 3 comme suit :

    $ sudo apt-get install python3 python3-pip

1. Clonez le référentiel :

    ```
    $ git clone https://github.com/Dooniess/Toolbox.git
    ```
   
2. Allez dans le répertoire cloné :

    ```
    $ cd Kruptos
    ```

3. Installez les dépendances nécessaires :

    ```
    $ pip3 install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script Python :

    ```
    $ python3 kruptos.py
    ```

2. Lors de l'exécution, le script vous invitera à saisir un nom d'utilisateur :

    ```
    Veuillez entrer le nom d'utilisateur à vérifier : 
    ```

3. Saisissez le nom d'utilisateur que vous souhaitez vérifier et appuyez sur Entrée.

4. Le script vérifiera la présence de ce nom d'utilisateur sur une liste de sites web et affichera les résultats dans la console. Si le nom d'utilisateur est trouvé sur un site, il affiche `True` en vert avec le lien correspondant. Si le nom d'utilisateur n'est pas trouvé, il affiche `False` en rouge.

## Sites web supportés

Actuellement, l'outil vérifie les sites web suivants :

- Facebook
- YouTube
- WhatsApp
- Instagram
- Twitter
- LinkedIn
- Pinterest
- Reddit
- VK
- Snapchat
- GitHub
- SoundCloud
- Spotify
- TikTok
- Medium
- Twitch
- 9GAG
- Behance
- TradingView
- Kik
- Giphy
- Genius
- Fiverr
- Freelancer
- Imgur
- Roblox
- Duolingo
- Codecademy
- Bitbucket
- Askfm