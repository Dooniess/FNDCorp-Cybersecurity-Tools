<div align="center"><h2><b>VascoCyber - Toolbox</b></h2></div>

<p align="center"><img src="logo.png" alt="Logo" width="400" height="400"></p>

VascoCyber Toolbox is a Python script that provides a collection of cybersecurity tools to assist you in various security tasks. It offers a user-friendly interface to interact with different tools, allowing you to perform network scans, DNS reconnaissance, information gathering, and exploitation tasks.

## Features

- **Network Scanning**: Perform network scans using Nmap with various scan options such as TCP SYN scan, TCP connect scan, UDP scan, and more.
- **DNS Reconnaissance**: Get DNS information using tools like Whois, Fierce, and Dnsenum to gather details about domain records, perform WHOIS lookups, and explore DNS-related information.
- **Information Gathering**: Use TheHarvester to gather information about a target from online sources such as search engines and social media platforms.
- **Exploitation**: Search for exploits using Searchsploit for specific software or operating systems.
- **Custom Command**: Benefit from flexibility to enter custom commands in certain tools for advanced usage.

## Prerequisites

- Python 3.x
- Required Python packages can be installed using the command `pip install -r requirements.txt`

## Usage

1. Clone the repository or download the `toolbox.py` script.

2. Install the required Python packages using the command `pip install -r requirements.txt`.

3. Run the script using the command `python toolbox.py`.

4. Choose a tool category from the menu options: Network Scanning, DNS Reconnaissance, Information Gathering, Exploitation, or Quit.

5. Select a specific tool from the available options in the chosen category.

6. Follow the prompts to provide the required information and select desired options.

7. View the results displayed in the terminal.

8. Navigate the menu to select other tools or choose Quit to exit the script.

Here's an example usage:

```
$ python toolbox.py

 ---------------------
< Welcome, Penguin! >
 ---------------------
        \
         \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/


Catégorie d'outils :
  [ ] Scanning réseau
  [ ] Reconnaissance DNS
  [ ] Collecte d'informations
  [ ] Exploitation
  [ ] Quitter

Choisissez une catégorie d'outils :
> Scanning réseau

Outil de scanning réseau :
  [ ] Nmap
  [ ] Retour

Choisissez un outil de scanning réseau :
> Nmap

Cible à scanner : 192.168.0.1

Choisissez les options de Nmap :
  [ ] -sS (TCP SYN scan)
  [ ] -sT (TCP connect)
  [ ] -sU (UDP scan)
  [ ] -sN (Scans TCP Null, FIN et Xmas)
  [ ] -sV : Version Detection - détermine les versions des services en cours d'exécution sur l'hôte cible)
  [ ] -Pn (Considérer tous les hôtes comme étant connectés)
  [ ] -A (Enable OS detection, version detection, script scanning, and traceroute)
  [ ] -p- (Scan all ports)
  [ ] -F (Fast mode - Scan fewer ports)
  [ ] -T4 (Aggressive timing template)
  [ ] -T5 (Insane timing template)
  [ ] -sV (Version detection)
  [ ] -O (OS detection)
  [ ] -v (Increase verbosity level)
  [ ] Commande personnalisée

> -sS -sV

Starting Nmap 7.91 ( https://nmap.org ) at 2023-05-18 10:00 EDT
Nmap scan report for 192.168.0.1
Host is up (0.0030s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
443/tcp  open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
8080/tcp open  http    Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap done: 1 IP address (1 host up) scanned in 1.45 seconds

Catégorie d'outils :
  [ ] Scanning réseau
  [ ] Reconnaissance DNS
  [ ] Collecte d'informations
  [ ] Exploitation
  [ ] Quitter

Choisissez une catégorie d'outils :
> Quitter

Au plaisir d'explorer la boîte à outils FNDCORP avec vous !
```

## Contribution

Contributions to FNDCORP Cybersecurity Toolbox are welcome! If you have any improvements, bug fixes, or additional features to suggest, please open an issue or submit a pull request.

## License

The project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance this README according to your preferences and any additional information you'd like to provide.
