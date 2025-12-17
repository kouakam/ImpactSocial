using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace ImpactSocial.Infrastructure;

/// <summary>
/// Dependency injection configuration for the Infrastructure layer
/// </summary>
public static class DependencyInjection
{
    /// <summary>
    /// Adds Infrastructure layer services to the dependency injection container
    /// </summary>
    /// <param name="services">The service collection</param>
    /// <param name="configuration">The configuration</param>
    /// <returns>The service collection</returns>
    public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
    {
        // Services for infrastructure will be added here
        // Email, SMS, Storage, Payment, Identity, etc.

        return services;
    }
}
