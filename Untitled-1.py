def air_viscosity(T):
    mu0 = 1.716e-5  # Reference viscosity at T0 = 273.15 K (in kg/(m*s))
    T0 = 273.15     # Reference temperature (in Kelvin)
    S = 110.4      # Sutherland constant for air (in Kelvin)

    viscosity = mu0 * (T / T0)**(3/2) * (T0 + S) / (T + S)
    return viscosity

# Example usage:
temperature = 600  # Temperature in Kelvin
viscosity = air_viscosity(temperature)
print(f"Viscosity of air at {temperature} K: {viscosity} kg/(m*s)")
