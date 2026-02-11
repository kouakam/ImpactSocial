# Documentation ImpactSocial

Ce répertoire contient la documentation et les ressources de présentation pour le projet ImpactSocial.

## Présentations

### Plateforme de Développement Participatif Local

**Fichier :** `presentations/plateforme-developpement-participatif.pptx`

Cette présentation décrit la vision, les fonctionnalités et la valeur de la plateforme de développement participatif local ImpactSocial.

**Contenu de la présentation :**
- 15 diapositives couvrant tous les aspects du projet
- Notes de présentation pour l'orateur incluses sur chaque diapositive
- Emplacements prévus pour les schémas et wireframes

**Comment utiliser cette présentation :**
1. Ouvrir le fichier avec Microsoft PowerPoint, LibreOffice Impress, ou tout autre logiciel compatible avec le format .pptx
2. Consulter les notes de présentation (menu Affichage > Notes) pour les scripts oraux
3. Personnaliser le contenu selon vos besoins
4. Ajouter les schémas et wireframes dans les diapositives qui contiennent des placeholders

**Comment régénérer ou modifier la présentation :**

La présentation a été générée à partir du fichier markdown `presentation-plateforme-developpement-participatif.md` en utilisant la bibliothèque Python `python-pptx`.

Pour régénérer la présentation après avoir modifié le contenu markdown :

```bash
# Installer python-pptx si nécessaire
pip install python-pptx

# Utiliser le script de génération (créer un script similaire à celui utilisé initialement)
# Le script parse le fichier markdown et génère automatiquement les diapositives
python3 generate_presentation.py
```

**Structure du fichier markdown source :**
- Chaque section `## Slide X : Titre` définit une nouvelle diapositive
- Les points clés sont listés avec des tirets `-`
- Les notes de présentation sont entre guillemets après `**Notes de présentation :**`
- Les placeholders pour schémas sont marqués `**[Placeholder : Description]**`

## Autres ressources

Ce répertoire sera enrichi au fur et à mesure du développement du projet avec :
- Documentation technique
- Guides utilisateurs
- Spécifications fonctionnelles
- Wireframes et maquettes
- Architecture système

---

**Projet :** ImpactSocial - Plateforme de Développement Participatif Local  
**Dépôt :** https://github.com/kouakam/ImpactSocial
