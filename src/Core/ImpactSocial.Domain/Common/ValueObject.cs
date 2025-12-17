namespace ImpactSocial.Domain.Common;

/// <summary>
/// Base class for value objects following DDD principles
/// </summary>
public abstract class ValueObject
{
    /// <summary>
    /// Gets the components used for equality comparison
    /// </summary>
    /// <returns>The components to compare</returns>
    protected abstract IEnumerable<object?> GetEqualityComponents();

    /// <summary>
    /// Determines whether the specified object is equal to the current object
    /// </summary>
    /// <param name="obj">The object to compare with the current object</param>
    /// <returns>true if the specified object is equal to the current object; otherwise, false</returns>
    public override bool Equals(object? obj)
    {
        if (obj == null || obj.GetType() != GetType())
            return false;

        var other = (ValueObject)obj;
        return GetEqualityComponents().SequenceEqual(other.GetEqualityComponents());
    }

    /// <summary>
    /// Serves as the default hash function
    /// </summary>
    /// <returns>A hash code for the current object</returns>
    public override int GetHashCode()
    {
        return GetEqualityComponents()
            .Select(x => x?.GetHashCode() ?? 0)
            .Aggregate((x, y) => x ^ y);
    }

    /// <summary>
    /// Equality operator
    /// </summary>
    /// <param name="left">Left value object</param>
    /// <param name="right">Right value object</param>
    /// <returns>true if both value objects are equal; otherwise, false</returns>
    public static bool operator ==(ValueObject? left, ValueObject? right)
    {
        if (left is null && right is null) return true;
        if (left is null || right is null) return false;
        return left.Equals(right);
    }

    /// <summary>
    /// Inequality operator
    /// </summary>
    /// <param name="left">Left value object</param>
    /// <param name="right">Right value object</param>
    /// <returns>true if both value objects are not equal; otherwise, false</returns>
    public static bool operator !=(ValueObject? left, ValueObject? right)
    {
        return !(left == right);
    }
}
