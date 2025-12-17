# ImpactSocial

[![Build and Test](https://github.com/kouakam/ImpactSocial/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/kouakam/ImpactSocial/actions/workflows/build-and-test.yml)

## 📖 Description

ImpactSocial est une plateforme de gestion d'impact social développée avec .NET 8.0, utilisant Clean Architecture et Domain-Driven Design (DDD). Le projet vise à faciliter la gestion, le suivi et l'analyse d'initiatives à impact social.

## 🏗️ Architecture

Le projet suit les principes de Clean Architecture avec une séparation claire des responsabilités :

- **Core Layer** : Contient la logique métier et les règles d'application
  - `ImpactSocial.Domain` : Entités, Value Objects, Aggregates, Domain Events
  - `ImpactSocial.Application` : Use Cases, Commands, Queries, DTOs, Validators

- **Infrastructure Layer** : Implémentation des détails techniques
  - `ImpactSocial.Persistence` : DbContext, Repositories, Migrations
  - `ImpactSocial.Infrastructure` : Services externes (Email, SMS, Storage, Payment)

- **Presentation Layer** : Interfaces utilisateur
  - `ImpactSocial.WebAPI` : API REST avec Swagger
  - `ImpactSocial.BlazorWasm` : Application Blazor WebAssembly
  - `ImpactSocial.BlazorServer` : Application Blazor Server

## 🚀 Prérequis

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
- SQL Server ou PostgreSQL
- Docker (optionnel)

## 📦 Installation

### Cloner le dépôt

```bash
git clone https://github.com/kouakam/ImpactSocial.git
cd ImpactSocial
```

### Restaurer les dépendances

```bash
dotnet restore
```

### Construire le projet

```bash
dotnet build
```

### Exécuter les tests

```bash
dotnet test
```

### Lancer l'API

```bash
cd src/Presentation/ImpactSocial.WebAPI
dotnet run
```

L'API sera disponible sur `https://localhost:7001` et la documentation Swagger sur `https://localhost:7001/swagger`

## 🐳 Docker

### Construire et lancer avec Docker Compose

```bash
docker-compose up -d
```

Cela va démarrer :
- L'API REST sur le port 7001
- SQL Server sur le port 1433

## 🧪 Tests

Le projet inclut différents types de tests :

- **Unit Tests** : Tests unitaires pour Domain et Application
- **Integration Tests** : Tests d'intégration pour Infrastructure
- **Functional Tests** : Tests fonctionnels pour WebAPI

```bash
# Exécuter tous les tests
dotnet test

# Exécuter les tests avec couverture
dotnet test --collect:"XPlat Code Coverage"
```

## 📚 Documentation

- [Architecture](docs/ARCHITECTURE.md) : Documentation détaillée de l'architecture
- [Getting Started](docs/GETTING_STARTED.md) : Guide de démarrage pour les développeurs

## 🛠️ Technologies

- **Framework** : .NET 8.0
- **ORM** : Entity Framework Core 8.0
- **Mediator** : MediatR 12.2.0
- **Mapping** : AutoMapper 12.0.1
- **Validation** : FluentValidation 11.9.0
- **Logging** : Serilog 8.0.0
- **API Documentation** : Swagger/OpenAPI
- **Frontend** : Blazor (WebAssembly & Server)
- **UI Library** : MudBlazor 6.11.2
- **Database** : SQL Server / PostgreSQL
- **Caching** : Redis
- **Testing** : xUnit, Moq, FluentAssertions, Bogus

## 🤝 Contribution

Les contributions sont les bienvenues ! Veuillez consulter le guide de contribution pour plus d'informations.

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 License

Copyright © 2025 ImpactSocial Team

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.