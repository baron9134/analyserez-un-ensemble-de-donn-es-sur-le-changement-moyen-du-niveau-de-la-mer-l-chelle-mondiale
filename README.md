# analyserez-un-ensemble-de-donn-es-sur-le-changement-moyen-du-niveau-de-la-mer-l-chelle-mondiale
"""
# README

## Projet : Prédiction du Niveau de la Mer

### Description :
Ce script analyse l'élévation du niveau de la mer sur une période allant de 1880 à 2050 en utilisant un ensemble de données provenant de la NASA. Il génère un graphique montrant les données historiques et les prédictions pour l'avenir, avec une courbe de dispersion et des lignes de régression linéaire.

### Objectifs :
1. Lire les données provenant du fichier `epa-sea-level.csv`.
2. Tracer un graphique de dispersion avec l'année sur l'axe des abscisses et l'élévation du niveau de la mer sur l'axe des ordonnées.
3. Ajouter une ligne de régression pour toutes les années et prévoir l'élévation du niveau de la mer jusqu'en 2050.
4. Ajouter une autre ligne de régression basée uniquement sur les années après 2000, avec une prévision pour 2050.
5. Afficher et sauvegarder le graphique généré.

### Dépendances :
- pandas
- matplotlib
- scipy

### Instructions :
1. Téléchargez le fichier `epa-sea-level.csv` contenant les données sur le niveau de la mer.
2. Placez le fichier dans le même répertoire que ce script.
3. Exécutez le script en utilisant la commande suivante :
    python sea_level_predictor.py
4. Le graphique sera généré et sauvegardé sous le nom `sea_level_rise_plot.png`.

### Exemple de Graphique :
Le script génère un graphique avec les éléments suivants :
- Un graphique de dispersion montrant les données historiques sur l'élévation du niveau de la mer.
- Deux lignes de régression :
  - Une pour toutes les données.
  - Une pour les données depuis l'an 2000.
- La prévision du niveau de la mer pour l'année 2050.

### Structure du Code :
1. **Lecture des données :** La fonction `read_data()` charge les données depuis le fichier CSV.
2. **Création du graphique de dispersion :** La fonction `create_scatter_plot()` trace un graphique de dispersion avec l'année et le niveau de la mer.
3. **Régression linéaire pour toutes les données :** La fonction `draw_best_fit_line()` trace la ligne de meilleure régression pour toutes les années.
4. **Régression linéaire depuis 2000 :** La fonction `draw_best_fit_line_since_2000()` trace la ligne de meilleure régression uniquement pour les années après 2000.
5. **Affichage et sauvegarde du graphique :** La fonction `save_and_show_plot()` sauvegarde le graphique dans un fichier PNG et l'affiche.

### Exemple de Sortie :
Un fichier PNG appelé `sea_level_rise_plot.png` sera généré et contiendra un graphique montrant l'évolution du niveau de la mer, avec des lignes de régression basées sur les années complètes et les années depuis 2000, ainsi que les prévisions pour 2050.

### Auteur :
Développé par [Votre Nom] pour le défi de prévision du niveau de la mer.

"""
