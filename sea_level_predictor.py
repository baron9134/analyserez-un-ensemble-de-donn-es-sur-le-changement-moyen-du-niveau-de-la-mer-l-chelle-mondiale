import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# 1. Utiliser pandas pour importer les données
def read_data():
    # Charger les données depuis le fichier CSV
    data = pd.read_csv('epa-sea-level.csv')
    return data

# 2. Utiliser matplotlib pour créer une courbe de dispersion
def create_scatter_plot(data):
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

# 3. Calculer la ligne de meilleur ajustement pour toutes les données
def draw_best_fit_line(data):
    # Calculer la régression linéaire pour toutes les années
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    
    # Tracer la ligne de meilleure ajustement pour toutes les années
    years_extended = range(1880, 2051)  # Prolonger l'axe des années jusqu'en 2050
    sea_levels = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels, label="Best Fit Line (All Data)", color='red')

# 4. Calculer la ligne de meilleur ajustement pour les années après 2000
def draw_best_fit_line_since_2000(data):
    data_since_2000 = data[data['Year'] >= 2000]  # Filtrer les données après 2000
    
    # Calculer la régression linéaire pour les années depuis 2000
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_since_2000['Year'], data_since_2000['CSIRO Adjusted Sea Level'])
    
    # Tracer la ligne de meilleure ajustement pour les années après 2000
    years_extended = range(2000, 2051)  # Prolonger l'axe des années jusqu'en 2050
    sea_levels = [slope_2000 * year + intercept_2000 for year in years_extended]
    plt.plot(years_extended, sea_levels, label="Best Fit Line (Since 2000)", color='green')

# 5. Sauvegarder et afficher le graphique
def save_and_show_plot():
    plt.legend()
    plt.savefig('sea_level_rise_plot.png')  # Sauvegarder l'image
    plt.show()  # Afficher le graphique

def main():
    # Lire les données
    data = read_data()

    # Créer la courbe de dispersion
    create_scatter_plot(data)

    # Tracer la ligne de meilleur ajustement pour toutes les années
    draw_best_fit_line(data)

    # Tracer la ligne de meilleur ajustement pour les années après 2000
    draw_best_fit_line_since_2000(data)

    # Sauvegarder et afficher le graphique
    save_and_show_plot()

if __name__ == '__main__':
    main()
