# Outils de Génération de Présentation

Ce dossier contient des scripts utilitaires pour le projet ImpactSocial.

## Script de Génération de Présentation PowerPoint

Le script `generate_presentation.py` génère automatiquement une présentation PowerPoint professionnelle pour la "Plateforme de Développement Participatif Local".

### Prérequis

- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

Avant d'exécuter le script, installez les dépendances requises :

```bash
pip install -r requirements.txt
```

Ou installez directement python-pptx :

```bash
pip install python-pptx
```

### Utilisation

Pour générer la présentation, exécutez simplement :

```bash
python tools/generate_presentation.py
```

Ou depuis le dossier `tools/` :

```bash
cd tools
python generate_presentation.py
```

### Résultat

Le script génère un fichier PowerPoint :
- **Emplacement** : `docs/presentations/plateforme-developpement-participatif.pptx`
- **Nombre de slides** : 15
- **Format** : .pptx (compatible PowerPoint, LibreOffice Impress, Google Slides)

### Structure de la présentation

La présentation contient 15 slides couvrant :

1. **Slide de titre** : Présentation de la plateforme
2. **Le Constat** : Problèmes identifiés
3. **Notre Vision** : Objectifs et ambitions
4. **Fonctionnalités Principales** : Caractéristiques clés
5. **Pour les Citoyens** : Avantages pour les citoyens
6. **Pour les Associations** : Avantages pour les associations
7. **Pour les Institutions Publiques** : Avantages pour les institutions
8. **Architecture Technique** : Infrastructure et technologies
9. **Modèle de Financement** : Sources de revenus
10. **Sécurité et Confidentialité** : Mesures de protection
11. **Mesure d'Impact** : Indicateurs et suivi
12. **Roadmap de Développement** : Phases et timeline
13. **Nos Partenaires** : Écosystème de partenariats
14. **Budget et Ressources** : Plan financier
15. **Rejoignez-nous !** : Appel à l'action et contacts

### Personnalisation

Pour modifier le contenu de la présentation :

1. Ouvrez le fichier `generate_presentation.py`
2. Modifiez la structure `SLIDES_DATA` en haut du fichier
3. Chaque entrée contient :
   - `title` : Titre de la slide
   - `subtitle` : Sous-titre (optionnel, pour la slide de titre)
   - `content` : Liste de points à puces
   - `notes` : Notes du présentateur (pitch oral)
4. Re-exécutez le script pour régénérer la présentation

### Exemple de structure de slide

```python
{
    "title": "Titre de la slide",
    "content": [
        "Premier point",
        "Deuxième point",
        "Troisième point"
    ],
    "notes": "Notes pour le présentateur..."
}
```

### Dépendances

- **python-pptx** (v0.6.23) : Bibliothèque pour créer et modifier des fichiers PowerPoint

### Licence

Ce script fait partie du projet ImpactSocial.

### Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe à contact@impactsocial.org
