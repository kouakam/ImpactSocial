# Scripts

Ce répertoire contient des scripts utilitaires pour le projet ImpactSocial.

## generate_presentation.py

Script Python pour générer ou régénérer la présentation PowerPoint à partir du fichier markdown.

**Usage:**
```bash
python3 scripts/generate_presentation.py
```

**Prérequis:**
```bash
pip install python-pptx
```

**Entrée:**
- `docs/presentation-plateforme-developpement-participatif.md` : Fichier markdown avec le contenu de la présentation

**Sortie:**
- `docs/presentations/plateforme-developpement-participatif.pptx` : Fichier PowerPoint généré

**Format du fichier markdown:**
Le fichier markdown doit suivre cette structure:
- Sections délimitées par `---`
- Chaque section commence par `## Slide X : Titre`
- `**Titre :**` et `**Sous-titre :**` pour la diapositive de titre
- `**Points clés :**` suivi d'une liste à puces avec `-`
- `**Notes de présentation :**` suivi du texte entre guillemets
- `**[Placeholder : Description]**` pour les emplacements réservés aux schémas
