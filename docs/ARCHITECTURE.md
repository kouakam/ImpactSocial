# Architecture ImpactSocial

## Vue d'ensemble

ImpactSocial est construit selon les principes de **Clean Architecture** et **Domain-Driven Design (DDD)**. Cette architecture garantit la séparation des préoccupations, la testabilité et la maintenabilité du code.

## Principes directeurs

### Clean Architecture

La Clean Architecture divise l'application en couches concentriques :

1. **Core (Centre)** : Logique métier pure, indépendante de toute technologie
2. **Infrastructure (Extérieur)** : Implémentations concrètes et dépendances externes
3. **Presentation (Interface)** : Points d'entrée de l'application

### Règle de dépendance

Les dépendances pointent toujours vers l'intérieur :
- Le Domain ne dépend de rien
- L'Application ne dépend que du Domain
- L'Infrastructure dépend de l'Application et du Domain
- La Presentation dépend de l'Application et de l'Infrastructure

## Structure des couches

### 1. Core Layer

#### ImpactSocial.Domain

Contient la logique métier pure et les règles invariantes du domaine.

**Responsabilités :**
- Définir les entités métier
- Implémenter les Value Objects
- Gérer les Aggregates
- Définir les Domain Events
- Lever des Domain Exceptions

**Dépendances :** Aucune (pure C#)

**Composants clés :**
- `BaseEntity` : Classe de base pour toutes les entités
- `ValueObject` : Classe de base pour les Value Objects
- `IDomainEvent` : Interface pour les événements du domaine
- `DomainException` : Exception personnalisée du domaine

#### ImpactSocial.Application

Contient les use cases et la logique d'application.

**Responsabilités :**
- Définir les Commands et Queries (CQRS)
- Implémenter les handlers MediatR
- Définir les DTOs pour les transferts de données
- Créer les validateurs FluentValidation
- Gérer les mappings AutoMapper
- Définir les interfaces pour les services d'infrastructure

**Dépendances :**
- ImpactSocial.Domain

**Composants clés :**
- `IApplicationDbContext` : Interface du contexte de base de données
- `ValidationBehavior` : Comportement de validation des requêtes
- `DependencyInjection` : Configuration de l'injection de dépendances

### 2. Infrastructure Layer

#### ImpactSocial.Persistence

Gère la persistance des données avec Entity Framework Core.

**Responsabilités :**
- Implémenter le DbContext
- Configurer les entités (EntityTypeConfiguration)
- Implémenter les repositories
- Gérer les migrations
- Intercepter les événements du domaine

**Dépendances :**
- ImpactSocial.Domain
- ImpactSocial.Application
- Entity Framework Core

**Composants clés :**
- `ApplicationDbContext` : Contexte de base de données EF Core
- `DependencyInjection` : Configuration de la persistence

#### ImpactSocial.Infrastructure

Implémente les services externes et les intégrations.

**Responsabilités :**
- Authentification et autorisation (JWT)
- Services de messagerie (Email, SMS)
- Stockage de fichiers (Azure Blob Storage)
- Paiements (Stripe)
- Caching (Redis)
- Logging (Serilog)

**Dépendances :**
- ImpactSocial.Application
- ImpactSocial.Persistence
- Librairies tierces

### 3. Presentation Layer

#### ImpactSocial.WebAPI

API REST avec Swagger pour la documentation.

**Responsabilités :**
- Exposer les endpoints REST
- Gérer l'authentification JWT
- Configurer CORS
- Documenter l'API avec Swagger
- Gérer les middlewares
- Implémenter SignalR pour le temps réel

**Dépendances :**
- ImpactSocial.Application
- ImpactSocial.Infrastructure
- ImpactSocial.Persistence

#### ImpactSocial.BlazorWasm

Application Blazor WebAssembly pour l'interface utilisateur client.

**Responsabilités :**
- Interface utilisateur interactive
- Consommation de l'API
- Stockage local
- Composants réutilisables avec MudBlazor

**Dépendances :**
- MudBlazor
- Blazored.LocalStorage

#### ImpactSocial.BlazorServer

Application Blazor Server pour une alternative avec rendering côté serveur.

**Responsabilités :**
- Interface utilisateur avec rendering serveur
- Communication temps réel avec SignalR
- Accès direct aux services

**Dépendances :**
- ImpactSocial.Application
- ImpactSocial.Infrastructure
- MudBlazor

## Patterns implémentés

### CQRS (Command Query Responsibility Segregation)

Séparation des opérations de lecture (Queries) et d'écriture (Commands) :
- **Commands** : Modifient l'état de l'application
- **Queries** : Lisent l'état sans le modifier

### Mediator Pattern

Utilisation de MediatR pour découpler les handlers des requêtes.

### Repository Pattern

Abstraction de la couche d'accès aux données (implémentée si nécessaire).

### Unit of Work

Géré par Entity Framework Core via le DbContext.

### Dependency Injection

Utilisation native de l'injection de dépendances .NET.

## Stratégie de test

### Tests unitaires
- **Domain.UnitTests** : Tests des entités et Value Objects
- **Application.UnitTests** : Tests des handlers et validateurs

### Tests d'intégration
- **Infrastructure.IntegrationTests** : Tests de la persistance et des services

### Tests fonctionnels
- **WebAPI.FunctionalTests** : Tests end-to-end de l'API

## Sécurité

- **Authentication** : JWT Bearer tokens
- **Authorization** : Policies basées sur les rôles
- **Validation** : FluentValidation pour toutes les entrées
- **CORS** : Configuration stricte des origines autorisées
- **Rate Limiting** : Protection contre les abus

## Performance

- **Caching** : Redis pour la mise en cache distribuée
- **Async/Await** : Opérations asynchrones partout
- **Pagination** : Pour toutes les listes
- **Projections** : Utilisation de DTOs pour réduire les données transférées

## Scalabilité

L'architecture permet :
- Déploiement horizontal de l'API
- Séparation des bases de données lecture/écriture (si nécessaire)
- Mise en cache distribuée avec Redis
- Utilisation de message queues (future implémentation)

## Maintenance

- **Logging structuré** : Serilog avec contexte enrichi
- **Health Checks** : Endpoints de santé pour le monitoring
- **Documentation** : XML comments et Swagger
- **Clean Code** : Conventions et bonnes pratiques C#
