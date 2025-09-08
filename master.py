import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

classement = [111, 94, 80, 76, 67, 60, 50, 48, 45, 43, 40, 37, 31, 30, 30]
jour = np.array(range(len(classement)))

def modele_exp(x, a, b, c):
    return a * np.exp(b * x) + c

# Ajustement du modèle exponentiel
params, _ = curve_fit(modele_exp, jour, classement, p0=(100, -0.1, 10))

# Prédiction pour les jours existants et futurs
x = np.linspace(0, 24, 300)
y = modele_exp(x, *params)

jour_futur = 40
prediction = modele_exp(jour_futur, *params)

plt.plot(jour, classement, "o", label="Données")
plt.plot(x, y, "-", label="Modèle exponentiel")
plt.plot(jour_futur, prediction, "rx", label=f"Prédiction jour {jour_futur} ({prediction:.1f})")
plt.xlabel("Jour")
plt.ylabel("Classement")
plt.legend()
plt.show()