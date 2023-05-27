<div align="center"><h2><b>Kruptos</b></h2></div>

<p align="center"><img src="..\logo.png" alt="Logo" width="400" height="400"></p>

Kruptos is a Python-based tool that helps to check the presence of a given username across a variety of popular websites. It allows users to quickly see where a specific username is in use.

## Installation

You need Python 3.6 or later to run Kruptos. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems. In Ubuntu, you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

1. Clone the repository:

    ```
    $ git clone https://github.com/Dooniess/FNDCorp-Cybersecurity-Tools.git
    ```
   
2. Go into the cloned directory:

    ```
    $ cd Kruptos
    ```

3. Install the necessary dependencies:

    ```
    $ pip3 install -r requirements.txt
    ```

## Usage

1. Run the Python script:

    ```
    $ python3 kruptos.py
    ```

2. When run, the script will prompt you to enter a username:

    ```
    Veuillez entrer le nom d'utilisateur à vérifier : 
    ```

3. Enter the username you wish to check and hit Enter.

4. The script will check the presence of this username across a list of websites and display the results in the console. If the username is found on a site, it prints `True` in green with the corresponding link. If the username is not found, it prints `False` in red.

## Supported Websites

Currently, the tool checks the following websites:

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

