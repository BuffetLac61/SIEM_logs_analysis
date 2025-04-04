#!/home/alexis/dev/bin/python3
import pandas as pd
from collections import Counter
import re


error_log_path = input("Chemin du fichier de logs d'erreur : ")


with open(error_log_path, "r") as f:
    error_logs = f.readlines()


warn_lines = [line for line in error_logs] #if '[warn]' in line

# On extrait les messages après "[client ...]"
warn_messages = [
    re.sub(r'.*\[client [0-9\.]+\] ', '', line).strip()
    for line in warn_lines
]

# On extrait les IPs des clients depuis les lignes warn
warn_ips = [
    re.search(r'\[client ([0-9\.]+)\]', line).group(1)
    for line in warn_lines if re.search(r'\[client ([0-9\.]+)\]', line)
]

# les occurrences de chaque message et chaque IP
warn_counter = Counter(warn_messages)
warn_ip_counter = Counter(warn_ips)
print(warn_ip_counter)

# On transforme en DataFrame pour affichage clair
warn_df = pd.DataFrame(warn_counter.items(), columns=['Warning Message', 'Count'])
warn_df = warn_df.sort_values(by='Count', ascending=False).reset_index(drop=True)

warn_df_ip = pd.DataFrame(warn_ip_counter.items(), columns=['Warning ip', 'Count'])
warn_df_ip = warn_df_ip.sort_values(by='Count', ascending=False).reset_index(drop=True)

print(warn_df)
print(warn_df_ip)