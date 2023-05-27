<div align="center"><h2><b>VascoCyber - Toolbox</b></h2></div>

<p align="center"><img src="..\logo.png" alt="Logo" width="400" height="400"></p>

VascoCyber Toolbox est un script Python qui fournit une collection d'outils de cybersécurité pour vous aider dans diverses tâches de sécurité. Il offre une interface conviviale pour interagir avec différents outils, ce qui vous permet d'effectuer des analyses de réseau, des reconnaissances DNS, des collectes d'informations et des tâches d'exploitation.

## Fonctionnalités

- **Analyse du réseau** : Effectuez des analyses de réseau à l'aide de Nmap avec diverses options d'analyse telles que l'analyse TCP SYN, l'analyse TCP connect, l'analyse UDP, etc.
- **Reconnaissance DNS** : Obtenez des informations DNS à l'aide d'outils tels que Whois, Fierce et Dnsenum pour recueillir des détails sur les enregistrements de domaine et explorer les informations liées au DNS.
- **Collecte d'informations** : Utilisez TheHarvester pour recueillir des informations sur une cible à partir de sources en ligne telles que les moteurs de recherche et les plateformes de médias sociaux.
- **Exploitation** : Recherchez des exploits à l'aide de Searchsploit pour des logiciels ou des systèmes d'exploitation spécifiques.
- **Commande personnalisée** : Bénéficiez de la flexibilité d'entrer des commandes personnalisées dans certains outils pour une utilisation avancée.

## Pré-requis

- Python 3.x
- Les paquets Python requis peuvent être installés en utilisant la commande `pip install -r requirements.txt`

## Utilisation

1. Clonez le dépôt ou téléchargez le script `VascoCyber.py`.

2. Installez les paquets Python requis à l'aide de la commande `pip install -r requirements.txt`.

3. Exécutez le script à l'aide de la commande `python VascoCyber.py`.

4. Choisissez une catégorie d'outils dans les options du menu : Analyse du réseau, Reconnaissance DNS, Collecte d'informations, Exploitation ou Quitter.

5. Sélectionnez un outil spécifique parmi les options disponibles dans la catégorie choisie.

6. Suivez les instructions pour fournir les informations requises et sélectionner les options souhaitées.

7. Visualisez les résultats affichés dans le terminal.

8. Naviguez dans le menu pour sélectionner d'autres outils ou choisissez Quitter pour quitter le script

Voici un exemple d'utilisation :

```
$ python VascoCyber.py

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

```

## Contribution

Les contributions à VascoCyber Toolbox sont les bienvenues ! Si vous avez des améliorations, des corrections de bugs ou des fonctionnalités supplémentaires à suggérer, veuillez ouvrir un ticket ou soumettre une demande d'extension.

## License

Le projet est soumis à la licence [MIT License](LICENSE).
