import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Charger les données dans un DataFrame
df = pd.read_csv('df2-9.csv', parse_dates=['date'])
mois='septembre'
mois_num=9
numb_jour_mois=30


# Créer une liste pour stocker les débits cumulés pour chaque jour
debit_cumules = []
# Créer une liste pour stocker les noms des jours de la semaine
jours_semaine = []

# Boucle à travers les jours de avril
for i in range(1,numb_jour_mois+1):
    # Filtrer les données pour le jour en cours
    jour = df[df['date'].dt.day == i]

    # Calculer le débit cumulé pour ce jour
    debit_cumule = jour['debit'].sum()

    # Ajouter le débit cumulé à la liste
    debit_cumules.append(debit_cumule)

    # Déterminer le nom du jour de la semaine correspondant à i
    nom_jour = calendar.day_name[calendar.weekday(2022, mois_num, i)]
    jours_semaine.append(nom_jour + ' '+str(i))

# Créer un DataFrame à partir des listes
df_debit_cumule = pd.DataFrame({'debit_cumule': debit_cumules, 'jour_semaine': jours_semaine}, index=range(1,numb_jour_mois+1))

# Afficher le graphique en utilisant un graphique en barres
ax = df_debit_cumule.plot.bar(x='jour_semaine', y='debit_cumule', figsize=(10, 5), legend=False)
ax.set_xlabel('Jour de ' + mois)
ax.set_ylabel('Débit cumulé')
ax.set_title('Débit cumulé pour chaque jour de ' + mois)
plt.show()
