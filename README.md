# RGM Intelligence AI

### Prévision des ventes et simulation de stratégies tarifaires

## Présentation

RGM Intelligence AI est un projet de Data Science appliqué au secteur de la grande distribution.

L'objectif est d'exploiter des données historiques de ventes et de prix pour développer un modèle prédictif et un outil interactif de simulation du chiffre d'affaires.

## Technologies utilisées

- **Python** : Pandas, NumPy
- **Machine Learning** : XGBoost, Scikit-learn
- **Statistiques** : Statsmodels
- **Application web** : Streamlit
- **Données** : Walmart M5 Forecasting (Kaggle)

## Fonctionnalités

**1. Prévision des ventes**

Développement d'un modèle XGBoost utilisant les prix, les variables calendaires et les ventes historiques.

Résultats sur 2 800 observations de test :

| Modèle | MAE |
|---|---:|
| XGBoost | 1,214 |
| Prévision naïve (J-7) | 1,435 |

XGBoost réduit l'erreur absolue moyenne d'environ **15,4 %** par rapport à la méthode naïve.

**2. Analyse exploratoire de l'élasticité-prix**

Estimation d'une régression log-log pour étudier l'association entre les variations de prix et les quantités vendues.

L'estimation réalisée sur un premier produit n'étant pas statistiquement significative, elle n'est pas utilisée pour formuler des recommandations tarifaires.

**3. Simulateur commercial Streamlit**

Développement d'une interface interactive permettant de :

- Sélectionner un produit et un magasin.
- Modifier le prix de vente.
- Définir une hypothèse d'élasticité-prix.
- Simuler les quantités vendues et le chiffre d'affaires journalier.

## Limites

Ce projet constitue un prototype exploratoire réalisé sur un échantillon de 100 séries produit-magasin.

L'évaluation du modèle repose sur des prévisions à un jour utilisant des ventes passées observées.

Les simulations tarifaires utilisent une élasticité hypothétique et ne constituent pas des recommandations causales ou commerciales validées.

## Exécution

Installer les dépendances :

```bash
pip install pandas numpy scikit-learn xgboost statsmodels streamlit
```

Lancer l'application depuis le dossier contenant `app.py` et `donnees_app.csv` :

```bash
python -m streamlit run app.py
```

## Perspectives

- Étendre l'entraînement à davantage de produits et magasins.
- Améliorer la validation temporelle du modèle.
- Approfondir l'estimation des effets des prix et promotions.
- Développer des fonctionnalités d'aide à la décision commerciale.