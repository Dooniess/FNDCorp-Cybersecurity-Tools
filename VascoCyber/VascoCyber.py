#!/usr/bin/env python3
import subprocess
import questionary
from termcolor import colored
import pyfiglet

# Fonction pour imprimer l'en-tête de l'application
def print_header():
    print("\n\n")
    banner = pyfiglet.figlet_format("FNDCORP", font="pagga")
    print(colored(banner, 'red'))
    banner1 = pyfiglet.figlet_format("Cybersecurity Tools", font="pagga")
    print(colored(banner1, 'red'))
    print("\n\n")

# Fonction pour exécuter les commandes des outils en utilisant subprocess
def run_tool(tool, target=None, options=None):
    # Si l'utilisateur a sélectionné l'option "Commande personnalisée"
    if options and "Commande personnalisée" in options:
        custom_command = questionary.text(f"Entrez votre commande personnalisée pour {tool} :").ask().split()
        command = [tool, *custom_command]
    else:
        # Configuration des commandes pour chaque outil en fonction des options choisies par l'utilisateur
        if tool == 'nmap':
            command = ['nmap', *options, target]
        elif tool == 'whois':
            command = ['whois', target]
        elif tool == 'fierce':
            command = ['fierce', *options, '-dns', target]
        elif tool == 'dnsenum':
            command = ['dnsenum', *options, target]
        elif tool == 'searchsploit':
            command = ['searchsploit', target]
        elif tool == 'theHarvester':
            command = ['theHarvester', '-d', target]

    try:
        # Exécute la commande et récupère la sortie
        result = subprocess.run(command, stdout=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        # En cas d'erreur lors de l'exécution de la commande, retourne un message d'erreur
        return f"Une erreur s'est produite lors de l'exécution de {tool}: {e.output.decode('utf-8')}"

# Fonction principale
def main():
    # Affiche l'en-tête
    print_header()

    # Boucle principale pour permettre à l'utilisateur de choisir les outils et les options
    while True:
        category_choice = questionary.select(
            "Catégorie d'outils :",
            choices=["Scanning réseau", "Reconnaissance DNS", "Collecte d'informations", "Exploitation", "Quitter"]).ask()
        # Selon la catégorie choisie, propose une liste d'outils et d'options
        if category_choice == "Scanning réseau":
            tool_choice = questionary.select(
                "Outil de scanning réseau :",
                choices=["Nmap", "Retour"]).ask()
            if tool_choice == "Nmap":
                target = questionary.text("Cible à scanner :").ask()
                nmap_options = questionary.checkbox(
                    "Choisissez les options de Nmap :",
                    choices=["-sS (TCP SYN scan)",
                             "-sT (TCP connect)",
                             "-sU (UDP scan)",
                             "-sN (Scans TCP Null, FIN et Xmas)",
                             "-sV : Version Detection - détermine les versions des services en cours d'exécution sur l'hôte cible)",
                             "-Pn (Considérer tous les hôtes comme étant connectés)",
                             "-A (Enable OS detection, version detection, script scanning, and traceroute)",
                             "-p- (Scan all ports)",
                             "-F (Fast mode - Scan fewer ports)",
                             "-T4 (Aggressive timing template)",
                             "-T5 (Insane timing template)",
                             "-sV (Version detection)",
                             "-O (OS detection)",
                             "-v (Increase verbosity level)",
                             "Commande personnalisée"]).ask()
                print(run_tool('nmap', target, nmap_options))
        elif category_choice == "Reconnaissance DNS":
            tool_choice = questionary.select(
                "Outil de reconnaissance DNS :",
                choices=["Whois", "Fierce", "Dnsenum", "Retour"]).ask()
            if tool_choice == "Whois":
                target = questionary.text("Cible pour whois :").ask()
                print(run_tool('whois', target))
            elif tool_choice == "Fierce":
                target = questionary.text("Cible pour fierce :").ask()
                fierce_options = questionary.checkbox(
                    "Choisissez les options pour Fierce :",
                    choices=["-dns (Target domain)",
                             "-dnsserver (Custom DNS server to use)",
                             "-range (IP Range to use for reverse lookups)",
                             "-file (File containing IP ranges for reverse lookups)",
                             "-wide (Scan whole class C of discovered domains)",
                             "Commande personnalisée"]).ask()
                print(run_tool('fierce', target, fierce_options))
            elif tool_choice == "Dnsenum":
                target = questionary.text("Entrez la cible pour dnsenum :").ask()
                dnsenum_options = questionary.checkbox(
                    "Options pour Dnsenum :",
                    choices=["--enum (Shortcut option equivalent to --threads 5 -s 20 -w)",
                             "--noreverse (Skip the reverse lookup operations)",
                             "--dnsserver (Use this DNS server to perform all A, NS and MX queries, the AXFR and PTR queries are sent to the domain's NS servers)",
                             "-f (Use a file for input)",
                             "-u (Check for updates)",
                             "-r (Enable recursive whois lookups)",
                             "-p (Set the number of threads)",
                             "-d (Delay between whois requests)",
                             "Commande personnalisée"]).ask()
                print(run_tool('dnsenum', target, dnsenum_options))
        elif category_choice == "Collecte d'informations":
            tool_choice = questionary.select(
                "Outil de collecte d'informations :",
                choices=["TheHarvester", "Retour"]).ask()
            if tool_choice == "TheHarvester":
                target = questionary.text("Cible pour TheHarvester :").ask()
                theHarvester_options = questionary.checkbox(
                    "Options pour TheHarvester :",
                    choices=["-d (Domain to search or company name)",
                             "-b (Data source: baidu, bing, bingapi, bingv6, bufferoverun, certspotter, crtsh, dnsdumpster, dogpile, github-code, google, hunter, intelx, linkedin, netcraft, otx, pentesttools, projetdiscovery, securityTrails, spyse, sublist3r, threatcrowd, trello, twitter, urlscan, virustotal, yahoo, all)",
                             "-l (Limit the number of results to work with bing and google)",
                             "-h (Use Shodan to query discovered hosts)",
                             "-c (Use DNSDumpster to query discovered hosts)",
                             "-e (Use Certspotter to query discovered hosts)",
                             "-g (Use GitHub code to query discovered hosts)",
                             "-p (Use thePentest to query discovered hosts)",
                             "-s (Use SecurityTrails to query discovered hosts)",
                             "-v (Use Virustotal to query discovered hosts)",
                             "Commande personnalisée"]).ask()
                print(run_tool('theHarvester', target, theHarvester_options))
        elif category_choice == "Exploitation":
            tool_choice = questionary.select(
                "Outil d'exploitation :",
                choices=["Searchsploit", "Retour"]).ask()
            if tool_choice == "Searchsploit":
                target = questionary.text("Entrez le nom du logiciel ou du système d'exploitation à exploiter :").ask()
                print(run_tool('searchsploit', target))
        elif category_choice == "Quitter":
            # Quitte la boucle et termine le programme
            break

# Exécute la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()
