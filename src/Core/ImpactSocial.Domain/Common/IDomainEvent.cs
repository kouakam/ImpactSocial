namespace ImpactSocial.Domain.Common;

/// <summary>
/// Represents a domain event that can be published and handled
/// </summary>
public interface IDomainEvent
{
    /// <summary>
    /// Gets the date and time when the event occurred
    /// </summary>
    DateTime OccurredOn { get; }
}
