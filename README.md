# Comparaison des statistiques des joueurs de baseball avec Statcast

Analyse comparative entre **Aaron Judge** et **Giancarlo Stanton** (New York Yankees), à partir des données Statcast 2015–2017.

## Contexte

Statcast est un système de suivi de pointe (caméras haute résolution + radars) qui mesure avec précision la position et les déplacements des balles et des joueurs dans les 30 stades de la Major League Baseball. En 2017, Judge et Stanton ont dominé la ligue avec respectivement 52 et 59 home runs.

Ce projet nettoie, analyse et visualise les données pour comparer les deux joueurs sur plusieurs aspects : fréquence des événements, zones de frappe des home runs, vitesse et angle de lancer.

## Données

- `judge.csv` : données Statcast d'Aaron Judge (2015–2017)
- `stanton.csv` : données Statcast de Giancarlo Stanton (2015–2017)

Chaque ligne correspond à un lancer effectué face au batteur.

## Méthodologie

1. Comptage des événements de jeu (home run, strikeout, walk, etc.) pour la saison 2017
2. Filtrage des home runs situés dans la zone de prise (strike zone)
3. Visualisation de la vitesse de balle (`launch_speed`) vs l'angle de frappe (`launch_angle`)
4. Cartographie des zones de frappe des home runs (histogrammes 2D)
5. Comparaison de la vitesse des lancers reçus (`release_speed`)

## Résultats

- **Home runs les plus bas et les plus puissants (angle de frappe médian le plus faible)** : Stanton
- **Lancers les plus rapides reçus (vitesse médiane la plus élevée)** : Judge

## Outils utilisés

- Python
- pandas
- Matplotlib
- Seaborn

## Fichier

- `mlb_statcast_analysis.py` : script complet de l'analyse
