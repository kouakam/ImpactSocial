# Guide de démarrage - ImpactSocial

Ce guide vous aidera à configurer l'environnement de développement et à démarrer avec le projet ImpactSocial.

## Prérequis

### Logiciels requis

1. **.NET 8.0 SDK**
   - Télécharger depuis [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/8.0)
   - Vérifier l'installation : `dotnet --version`

2. **IDE / Éditeur de code**
   - Visual Studio 2022 (17.8 ou supérieur) - Recommandé pour Windows
   - Visual Studio Code avec extensions C# - Multi-plateforme
   - JetBrains Rider - Alternative premium

3. **SQL Server** (ou PostgreSQL)
   - SQL Server Express (gratuit) - Windows
   - SQL Server Developer Edition (gratuit) - Windows/Linux/Docker
   - PostgreSQL 13+ - Alternative multi-plateforme

4. **Docker Desktop** (optionnel mais recommandé)
   - Pour SQL Server et Redis en conteneurs

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/kouakam/ImpactSocial.git
cd ImpactSocial
```

### 2. Configuration de la base de données

#### Option A : Utiliser Docker (Recommandé)

```bash
docker-compose up -d sqlserver
```

#### Option B : Installation locale

Si vous avez SQL Server installé localement, mettez à jour la chaîne de connexion dans `src/Presentation/ImpactSocial.WebAPI/appsettings.Development.json` :

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=ImpactSocialDb_Dev;Trusted_Connection=True;TrustServerCertificate=True;MultipleActiveResultSets=true"
  }
}
```

### 3. Restaurer les dépendances

```bash
dotnet restore
```

### 4. Appliquer les migrations (une fois créées)

```bash
cd src/Infrastructure/ImpactSocial.Persistence
dotnet ef database update --startup-project ../../Presentation/ImpactSocial.WebAPI
```

### 5. Construire la solution

```bash
dotnet build
```

## Exécution

### Lancer l'API

```bash
cd src/Presentation/ImpactSocial.WebAPI
dotnet run
```

L'API sera disponible sur :
- HTTPS : `https://localhost:7001`
- HTTP : `http://localhost:5001`
- Swagger UI : `https://localhost:7001/swagger`

### Lancer Blazor WebAssembly

```bash
cd src/Presentation/ImpactSocial.BlazorWasm
dotnet run
```

### Lancer Blazor Server

```bash
cd src/Presentation/ImpactSocial.BlazorServer
dotnet run
```

### Exécuter avec Docker

```bash
docker-compose up
```

## Structure du projet

```
ImpactSocial/
├── src/
│   ├── Core/
│   │   ├── ImpactSocial.Domain/         # Logique métier
│   │   └── ImpactSocial.Application/    # Use cases
│   ├── Infrastructure/
│   │   ├── ImpactSocial.Persistence/    # Accès aux données
│   │   └── ImpactSocial.Infrastructure/ # Services externes
│   └── Presentation/
│       ├── ImpactSocial.WebAPI/         # API REST
│       ├── ImpactSocial.BlazorWasm/     # Client Blazor WASM
│       └── ImpactSocial.BlazorServer/   # Client Blazor Server
└── tests/                                # Tests unitaires et d'intégration
```

## Développement

### Ajouter une nouvelle entité

1. Créer l'entité dans `ImpactSocial.Domain/Entities/`
2. Créer la configuration EF Core dans `ImpactSocial.Persistence/Configurations/`
3. Ajouter le DbSet dans `ApplicationDbContext`
4. Créer une migration :
   ```bash
   dotnet ef migrations add AddNewEntity --startup-project ../../Presentation/ImpactSocial.WebAPI
   ```

### Ajouter un Command/Query

1. Créer le Command/Query dans `ImpactSocial.Application/Commands/` ou `Queries/`
2. Créer le Handler correspondant
3. Créer le Validator FluentValidation
4. Créer le Controller dans WebAPI

Exemple de Command :

```csharp
// CreateUserCommand.cs
public record CreateUserCommand(string Name, string Email) : IRequest<Guid>;

// CreateUserCommandHandler.cs
public class CreateUserCommandHandler : IRequestHandler<CreateUserCommand, Guid>
{
    private readonly IApplicationDbContext _context;

    public CreateUserCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<Guid> Handle(CreateUserCommand request, CancellationToken cancellationToken)
    {
        // Implémentation
    }
}

// CreateUserCommandValidator.cs
public class CreateUserCommandValidator : AbstractValidator<CreateUserCommand>
{
    public CreateUserCommandValidator()
    {
        RuleFor(x => x.Name).NotEmpty().MaximumLength(100);
        RuleFor(x => x.Email).NotEmpty().EmailAddress();
    }
}
```

### Exécuter les tests

```bash
# Tous les tests
dotnet test

# Tests d'un projet spécifique
dotnet test tests/ImpactSocial.Domain.UnitTests

# Tests avec couverture
dotnet test --collect:"XPlat Code Coverage"
```

### Créer une migration

```bash
cd src/Infrastructure/ImpactSocial.Persistence
dotnet ef migrations add MigrationName --startup-project ../../Presentation/ImpactSocial.WebAPI
```

### Appliquer les migrations

```bash
cd src/Infrastructure/ImpactSocial.Persistence
dotnet ef database update --startup-project ../../Presentation/ImpactSocial.WebAPI
```

### Supprimer la dernière migration

```bash
cd src/Infrastructure/ImpactSocial.Persistence
dotnet ef migrations remove --startup-project ../../Presentation/ImpactSocial.WebAPI
```

## Outils utiles

### Extensions Visual Studio Code recommandées

- C# (Microsoft)
- C# Dev Kit (Microsoft)
- NuGet Package Manager
- Docker
- GitLens
- REST Client

### Extensions Visual Studio 2022 recommandées

- ReSharper (optionnel, payant)
- Entity Framework Core Power Tools
- Markdown Editor

## Bonnes pratiques

1. **Suivre les conventions C#**
   - PascalCase pour les classes, méthodes, propriétés
   - camelCase pour les variables locales
   - Préfixer les interfaces avec `I`

2. **Écrire des tests**
   - Tests unitaires pour la logique métier
   - Tests d'intégration pour les repositories
   - Tests fonctionnels pour les endpoints

3. **Documentation**
   - Ajouter des XML comments sur les classes et méthodes publiques
   - Mettre à jour le README pour les nouvelles fonctionnalités

4. **Commits Git**
   - Messages clairs et descriptifs
   - Commits atomiques (une fonctionnalité = un commit)

5. **Code Review**
   - Créer une Pull Request pour chaque fonctionnalité
   - Demander une revue avant de merger

## Résolution des problèmes

### Erreur de connexion à la base de données

Vérifier :
- SQL Server est en cours d'exécution
- La chaîne de connexion est correcte
- Les permissions utilisateur sont adéquates

### Erreur de build

```bash
# Nettoyer et reconstruire
dotnet clean
dotnet build
```

### Les migrations ne s'appliquent pas

```bash
# Supprimer la base de données et recréer
dotnet ef database drop --startup-project ../../Presentation/ImpactSocial.WebAPI
dotnet ef database update --startup-project ../../Presentation/ImpactSocial.WebAPI
```

## Ressources supplémentaires

- [Documentation .NET](https://docs.microsoft.com/dotnet/)
- [Entity Framework Core](https://docs.microsoft.com/ef/core/)
- [MediatR](https://github.com/jbogard/MediatR)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Domain-Driven Design](https://martinfowler.com/tags/domain%20driven%20design.html)

## Support

Pour toute question ou problème :
- Ouvrir une issue sur GitHub
- Consulter la documentation existante
- Contacter l'équipe de développement
