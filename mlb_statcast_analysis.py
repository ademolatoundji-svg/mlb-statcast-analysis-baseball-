"""
Projet : Comparaison des statistiques des joueurs de baseball avec Statcast
Comparaison entre Aaron Judge et Giancarlo Stanton (données 2015-2017)

Source des données : Statcast (via DataCamp)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 0. Chargement des données ────────────────────────────────────────
judge = pd.read_csv('judge.csv')
stanton = pd.read_csv('stanton.csv')

# Afficher toutes les colonnes (pandas en masque certaines par défaut)
pd.set_option('display.max_columns', None)


# ── Fonctions personnalisées ─────────────────────────────────────────
def assign_x_coord(row):
    """
    Attribue une coordonnée x aux numéros de zone de prise de Statcast.
    Les zones 11, 12, 13 et 14 sont ignorées pour simplifier le graphique.
    """
    # Tiers gauche de la zone de prise
    if row.zone in [1, 4, 7]:
        return 1
    # Tiers central de la zone de prise
    if row.zone in [2, 5, 8]:
        return 2
    # Tiers droit de la zone de prise
    if row.zone in [3, 6, 9]:
        return 3


def assign_y_coord(row):
    """
    Attribue une coordonnée y aux numéros de zone de prise de Statcast.
    Les zones 11, 12, 13 et 14 sont ignorées pour simplifier le graphique.
    """
    # Tiers supérieur de la zone de prise
    if row.zone in [1, 2, 3]:
        return 3
    # Tiers central de la zone de prise
    if row.zone in [4, 5, 6]:
        return 2
    # Tiers inférieur de la zone de prise
    if row.zone in [7, 8, 9]:
        return 1


# Afficher les cinq dernières lignes du fichier Aaron Judge (vérification)
print(judge.tail())


# ── 1. Compter les événements par joueur en 2017 ─────────────────────
judge_2017 = judge[judge['game_date'].str.startswith('2017')]
stanton_2017 = stanton[stanton['game_date'].str.startswith('2017')]

judge_events_2017 = judge_2017['events'].value_counts()
stanton_events_2017 = stanton_2017['events'].value_counts()

print(judge_events_2017)
print(stanton_events_2017)


# ── 2. Filtrer les home runs (zones <= 9 seulement) ───────────────────
judge_strike_hr = judge[(judge['events'] == 'home_run') &
                         (judge['zone'] <= 9)].copy()
stanton_strike_hr = stanton[(stanton['events'] == 'home_run') &
                             (stanton['zone'] <= 9)].copy()

judge_strike_hr['zone_x'] = judge_strike_hr.apply(assign_x_coord, axis=1)
judge_strike_hr['zone_y'] = judge_strike_hr.apply(assign_y_coord, axis=1)
stanton_strike_hr['zone_x'] = stanton_strike_hr.apply(assign_x_coord, axis=1)
stanton_strike_hr['zone_y'] = stanton_strike_hr.apply(assign_y_coord, axis=1)


# ── 3. Graphique launch_speed vs launch_angle ─────────────────────────
fig1, ax1 = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(data=judge_strike_hr, x='launch_angle',
                 y='launch_speed', ax=ax1[0])
ax1[0].set_title('Aaron Judge - Home Runs')

sns.scatterplot(data=stanton_strike_hr, x='launch_angle',
                 y='launch_speed', ax=ax1[1])
ax1[1].set_title('Giancarlo Stanton - Home Runs')

plt.tight_layout()
plt.show()

# Joueur avec les home runs les plus bas et les plus forts (angle médian)
judge_median_angle = judge_strike_hr['launch_angle'].median()
stanton_median_angle = stanton_strike_hr['launch_angle'].median()

if judge_median_angle < stanton_median_angle:
    player_hr = "Judge"
else:
    player_hr = "Stanton"


# ── 4. Histogrammes 2D des zones de prise ─────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist2d(judge_strike_hr['zone_x'].dropna(),
                judge_strike_hr['zone_y'].dropna(), bins=3)
axes[0].set_title('Aaron Judge - Zones HR')

axes[1].hist2d(stanton_strike_hr['zone_x'].dropna(),
                stanton_strike_hr['zone_y'].dropna(), bins=3)
axes[1].set_title('Giancarlo Stanton - Zones HR')

plt.tight_layout()
plt.show()


# ── 5. Comparer la vitesse des lancers (release_speed) ────────────────
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(judge_strike_hr['release_speed'], label='Judge', ax=ax)
sns.kdeplot(stanton_strike_hr['release_speed'], label='Stanton', ax=ax)
ax.set_title('Comparaison de la vitesse des lancers')
ax.legend()
plt.show()

# Joueur avec les lancers les plus rapides (vitesse médiane)
judge_median_speed = judge_strike_hr['release_speed'].median()
stanton_median_speed = stanton_strike_hr['release_speed'].median()

if judge_median_speed > stanton_median_speed:
    player_fast = "Judge"
else:
    player_fast = "Stanton"


# ── Résultats finaux ───────────────────────────────────────────────────
print(f"HR plus bas et plus forts : {player_hr}")
print(f"Lancers les plus rapides : {player_fast}")
