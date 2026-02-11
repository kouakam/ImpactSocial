#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération de présentation PowerPoint
Plateforme de Développement Participatif Local

Usage:
    python tools/generate_presentation.py
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Structure des slides : chaque élément contient titre, contenu (liste à puces) et notes
SLIDES_DATA = [
    {
        "title": "Plateforme de Développement Participatif Local",
        "subtitle": "Connecter les citoyens, les projets et les ressources pour un impact social durable",
        "content": [],
        "notes": """
Bienvenue à tous ! Aujourd'hui, nous allons vous présenter notre plateforme de développement participatif local.
Cette plateforme vise à créer un écosystème où citoyens, associations et institutions peuvent collaborer efficacement
pour développer des projets à impact social positif dans leur communauté.
"""
    },
    {
        "title": "Le Constat",
        "content": [
            "Manque de visibilité des projets locaux",
            "Difficultés de financement pour les initiatives citoyennes",
            "Communication fragmentée entre acteurs locaux",
            "Ressources sous-utilisées dans les communautés",
            "Besoin d'outils de coordination efficaces"
        ],
        "notes": """
Notre analyse du terrain révèle plusieurs problèmes majeurs. Les projets locaux manquent souvent de visibilité,
ce qui limite leur capacité à attirer des ressources. Les initiatives citoyennes peinent à trouver du financement.
La communication entre les différents acteurs est fragmentée, et de nombreuses ressources locales restent sous-utilisées
par manque de coordination.
"""
    },
    {
        "title": "Notre Vision",
        "content": [
            "Une plateforme numérique centralisée",
            "Faciliter la collaboration entre citoyens et institutions",
            "Transparence dans la gestion des projets",
            "Autonomisation des communautés locales",
            "Impact social mesurable et durable"
        ],
        "notes": """
Notre vision est de créer une plateforme numérique centralisée qui facilite la collaboration.
Nous voulons instaurer une transparence totale dans la gestion des projets, tout en autonomisant les communautés
locales pour qu'elles deviennent les actrices de leur propre développement. L'objectif final est de générer
un impact social mesurable et durable.
"""
    },
    {
        "title": "Fonctionnalités Principales",
        "content": [
            "Cartographie interactive des projets locaux",
            "Système de financement participatif",
            "Espace de collaboration et co-création",
            "Gestion de ressources partagées",
            "Tableau de bord d'impact social"
        ],
        "notes": """
La plateforme offre plusieurs fonctionnalités clés. D'abord, une cartographie interactive qui visualise tous les projets
locaux. Ensuite, un système de financement participatif intégré. Un espace de collaboration permet la co-création
de projets. La gestion des ressources partagées optimise l'utilisation des moyens disponibles. Enfin, un tableau de bord
mesure l'impact social de chaque initiative.
"""
    },
    {
        "title": "Pour les Citoyens",
        "content": [
            "Proposer et suivre des projets locaux",
            "Participer au financement de projets",
            "Rejoindre des initiatives existantes",
            "Partager des compétences et ressources",
            "Voter et prioriser les projets communautaires"
        ],
        "notes": """
Pour les citoyens, la plateforme offre de nombreuses possibilités. Ils peuvent proposer leurs propres projets
et suivre leur évolution. Ils peuvent contribuer financièrement à des projets qui les touchent. Ils peuvent rejoindre
des initiatives existantes, partager leurs compétences et leurs ressources. Enfin, ils peuvent voter pour prioriser
les projets qui comptent le plus pour leur communauté.
"""
    },
    {
        "title": "Pour les Associations",
        "content": [
            "Promouvoir leurs projets et actions",
            "Accéder à de nouveaux canaux de financement",
            "Collaborer avec d'autres organisations",
            "Recruter des bénévoles qualifiés",
            "Mesurer et communiquer leur impact"
        ],
        "notes": """
Les associations bénéficient d'outils puissants. Elles peuvent promouvoir leurs projets auprès d'un large public,
accéder à de nouveaux canaux de financement, et collaborer avec d'autres organisations de manière structurée.
La plateforme facilite aussi le recrutement de bénévoles qualifiés et offre des outils pour mesurer et communiquer
leur impact social de manière crédible.
"""
    },
    {
        "title": "Pour les Institutions Publiques",
        "content": [
            "Visualiser les besoins de la communauté",
            "Allouer les ressources de manière optimale",
            "Engager le dialogue avec les citoyens",
            "Suivre l'impact des politiques publiques",
            "Renforcer la démocratie participative"
        ],
        "notes": """
Les institutions publiques gagnent en efficacité et en légitimité. Elles peuvent visualiser en temps réel les besoins
de la communauté, allouer les ressources de manière plus optimale, et engager un dialogue constructif avec les citoyens.
La plateforme leur permet de suivre l'impact réel de leurs politiques publiques et de renforcer la démocratie
participative sur leur territoire.
"""
    },
    {
        "title": "Architecture Technique",
        "content": [
            "Application web responsive (React/Angular)",
            "API REST sécurisée",
            "Base de données évolutive",
            "Système de géolocalisation intégré",
            "Passerelles de paiement sécurisées"
        ],
        "notes": """
Sur le plan technique, nous avons opté pour une architecture moderne et robuste. L'application web est responsive
pour s'adapter à tous les appareils. L'API REST sécurisée garantit la protection des données. La base de données
est conçue pour évoluer avec la croissance de la plateforme. Le système de géolocalisation permet une visualisation
cartographique précise, et les passerelles de paiement sont conformes aux standards de sécurité les plus élevés.
"""
    },
    {
        "title": "Modèle de Financement",
        "content": [
            "Crowdfunding pour les projets citoyens",
            "Subventions publiques et privées",
            "Partenariats avec entreprises locales",
            "Frais de service optionnels (freemium)",
            "Dons et mécénat"
        ],
        "notes": """
Notre modèle économique est diversifié et durable. Le crowdfunding permet aux citoyens de financer directement
les projets qui les intéressent. Nous facilitons l'accès aux subventions publiques et privées. Les partenariats
avec des entreprises locales créent un écosystème vertueux. Un modèle freemium avec des services optionnels
assure notre viabilité financière, et nous acceptons les dons et le mécénat pour soutenir notre mission sociale.
"""
    },
    {
        "title": "Sécurité et Confidentialité",
        "content": [
            "Chiffrement des données sensibles",
            "Conformité RGPD",
            "Authentification sécurisée",
            "Modération des contenus",
            "Audit de sécurité régulier"
        ],
        "notes": """
La sécurité est au cœur de notre plateforme. Toutes les données sensibles sont chiffrées. Nous sommes pleinement
conformes au RGPD pour protéger la vie privée des utilisateurs. L'authentification utilise des standards modernes
et sécurisés. Nous modérons les contenus pour garantir un environnement sain. Des audits de sécurité réguliers
sont effectués par des experts indépendants.
"""
    },
    {
        "title": "Mesure d'Impact",
        "content": [
            "Indicateurs sociaux quantitatifs",
            "Évaluation qualitative des projets",
            "Suivi de l'engagement communautaire",
            "Reporting transparent pour les financeurs",
            "Analyse des retombées à long terme"
        ],
        "notes": """
Mesurer l'impact est essentiel pour nous. Nous utilisons des indicateurs sociaux quantitatifs rigoureux,
complétés par une évaluation qualitative approfondie des projets. Le suivi de l'engagement communautaire
nous permet de mesurer la vitalité de l'écosystème. Nous offrons un reporting transparent pour les financeurs,
et nous analysons les retombées à long terme pour comprendre vraiment l'effet de nos actions.
"""
    },
    {
        "title": "Roadmap de Développement",
        "content": [
            "Phase 1 : MVP avec fonctionnalités de base (3 mois)",
            "Phase 2 : Système de financement participatif (2 mois)",
            "Phase 3 : Outils de collaboration avancés (3 mois)",
            "Phase 4 : Application mobile native (4 mois)",
            "Phase 5 : Intelligence artificielle et recommandations (6 mois)"
        ],
        "notes": """
Notre roadmap est ambitieuse mais réaliste. En phase 1, nous livrons un MVP avec les fonctionnalités de base en 3 mois.
La phase 2 introduit le système de financement participatif en 2 mois. La phase 3 développe les outils de collaboration
avancés en 3 mois. La phase 4 déploie une application mobile native en 4 mois. Enfin, la phase 5 intègre l'intelligence
artificielle pour des recommandations personnalisées en 6 mois.
"""
    },
    {
        "title": "Nos Partenaires",
        "content": [
            "Collectivités territoriales",
            "Associations de quartier",
            "Fondations et ONG",
            "Entreprises à mission sociale",
            "Universités et centres de recherche"
        ],
        "notes": """
Nous avons déjà établi des partenariats stratégiques avec plusieurs acteurs clés. Des collectivités territoriales
nous soutiennent et souhaitent déployer la plateforme. Des associations de quartier sont prêtes à être nos premiers
utilisateurs. Des fondations et ONG nous accompagnent. Des entreprises à mission sociale veulent s'engager à nos côtés.
Enfin, des universités et centres de recherche nous aident à évaluer notre impact scientifiquement.
"""
    },
    {
        "title": "Budget et Ressources",
        "content": [
            "Développement technique : 150 000 €",
            "Marketing et communication : 50 000 €",
            "Ressources humaines : 100 000 €",
            "Infrastructure et hébergement : 30 000 €",
            "Total première année : 330 000 €"
        ],
        "notes": """
Pour la première année, nous avons établi un budget détaillé. Le développement technique représente 150 000 euros
pour construire une plateforme robuste et scalable. Le marketing et la communication nécessitent 50 000 euros
pour faire connaître la plateforme. Les ressources humaines représentent 100 000 euros pour constituer une équipe
compétente. L'infrastructure et l'hébergement coûtent 30 000 euros. Au total, nous avons besoin de 330 000 euros
pour lancer et faire fonctionner la plateforme pendant la première année.
"""
    },
    {
        "title": "Rejoignez-nous !",
        "content": [
            "Contactez-nous : contact@impactsocial.org",
            "Site web : www.impactsocial.org",
            "Réseaux sociaux : @ImpactSocial",
            "Contribuez au projet sur GitHub",
            "Ensemble, créons l'impact !"
        ],
        "notes": """
Nous sommes à un moment crucial et nous avons besoin de vous ! Que vous soyez citoyen, association, institution
ou entreprise, vous avez un rôle à jouer dans cette aventure. Contactez-nous par email, visitez notre site web,
suivez-nous sur les réseaux sociaux, ou contribuez directement au code sur GitHub. Ensemble, nous pouvons créer
un impact social durable et transformer nos communautés. Merci de votre attention et rejoignez-nous dans cette aventure !
"""
    }
]


def create_title_slide(prs, data):
    """Crée la slide de titre"""
    slide_layout = prs.slide_layouts[0]  # Layout titre
    slide = prs.slides.add_slide(slide_layout)
    
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = data["title"]
    subtitle.text = data.get("subtitle", "")
    
    # Ajouter les notes
    if "notes" in data:
        notes_slide = slide.notes_slide
        notes_slide.notes_text_frame.text = data["notes"]
    
    return slide


def create_content_slide(prs, data):
    """Crée une slide avec titre et contenu à puces"""
    slide_layout = prs.slide_layouts[1]  # Layout titre et contenu
    slide = prs.slides.add_slide(slide_layout)
    
    title = slide.shapes.title
    title.text = data["title"]
    
    # Ajouter le contenu à puces
    content_placeholder = slide.placeholders[1]
    text_frame = content_placeholder.text_frame
    text_frame.clear()
    
    for i, bullet_point in enumerate(data["content"]):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        p.text = bullet_point
        p.level = 0
    
    # Ajouter les notes
    if "notes" in data:
        notes_slide = slide.notes_slide
        notes_slide.notes_text_frame.text = data["notes"]
    
    return slide


def generate_presentation(output_path):
    """Génère la présentation PowerPoint complète"""
    
    # Créer une présentation vide
    prs = Presentation()
    
    # Définir la taille de la slide (16:9)
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Créer les slides
    for i, slide_data in enumerate(SLIDES_DATA):
        print(f"Création de la slide {i+1}/{len(SLIDES_DATA)}: {slide_data['title']}")
        
        if i == 0:
            # Première slide = titre
            create_title_slide(prs, slide_data)
        else:
            # Autres slides = contenu
            create_content_slide(prs, slide_data)
    
    # Créer le dossier de sortie si nécessaire
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"Dossier créé : {output_dir}")
    
    # Sauvegarder la présentation
    prs.save(output_path)
    print(f"\nPrésentation générée avec succès : {output_path}")
    print(f"Nombre total de slides : {len(prs.slides)}")
    
    return output_path


def main():
    """Point d'entrée principal"""
    # Chemin de sortie par défaut
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output_path = os.path.join(repo_root, "docs", "presentations", "plateforme-developpement-participatif.pptx")
    
    print("=" * 70)
    print("Génération de la présentation PowerPoint")
    print("Plateforme de Développement Participatif Local")
    print("=" * 70)
    print()
    
    try:
        generate_presentation(output_path)
        print("\n✓ Génération terminée avec succès !")
        print(f"\nLe fichier peut être ouvert avec Microsoft PowerPoint, LibreOffice Impress")
        print("ou tout autre logiciel compatible avec le format .pptx")
    except Exception as e:
        print(f"\n✗ Erreur lors de la génération : {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
