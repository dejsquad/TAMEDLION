def air_viscosity(T, unit='SI'):
    # Parameters for SI units
    mu_ref_SI = 1.716e-5  # kg/(m*s)
    T_ref_SI = 323        # Kelvin
    S_SI = 110.0          # Kelvin

    # Parameters for USC units
    mu_ref_USC = 3.737e-7 # slug/(ft*s)
    T_ref_USC = 518.67    # Rankine
    S_USC = 198.72        # Rankine

    if unit.lower() == 'si':
        mu_ref = mu_ref_SI
        T_ref = T_ref_SI
        S = S_SI
        unit_str = 'kg/(m*s)'
    elif unit.lower() == 'usc':
        mu_ref = mu_ref_USC
        T_ref = T_ref_USC
        S = S_USC
        unit_str = 'slug/(ft*s)'
    else:
        raise ValueError("Invalid unit. Please choose 'SI' or 'USC'.")

    viscosity = mu_ref * (T / T_ref)**(3/2) * (T_ref + S) / (T + S)
    return viscosity, unit_str


def main():
    try:
        temperature_str = input("Enter temperature (e.g., 300 K, 70 F, 100 C): ")
        temperature_value, temperature_unit = temperature_str.split(' ')
        temperature_value = float(temperature_value)

        if temperature_unit.upper() == 'K':
            viscosity_SI, unit_str_SI = air_viscosity(temperature_value, unit='SI')
            viscosity_USC, unit_str_USC = air_viscosity(temperature_value, unit='USC')
            print(f"Viscosity of air at {temperature_value} K: {viscosity_SI} {unit_str_SI}")
            print(f"Viscosity of air at {temperature_value} K: {viscosity_USC} {unit_str_USC}")

        elif temperature_unit.upper() == 'C':
            temperature_value += 273.15  # Convert Celsius to Kelvin
            viscosity_SI, unit_str_SI = air_viscosity(temperature_value, unit='SI')
            viscosity_USC, unit_str_USC = air_viscosity(temperature_value, unit='USC')
            print(f"Viscosity of air at {temperature_value - 273.15}°C: {viscosity_SI} {unit_str_SI}")
            print(f"Viscosity of air at {temperature_value - 273.15}°C: {viscosity_USC} {unit_str_USC}")

        elif temperature_unit.upper() == 'F':
            temperature_value = (temperature_value - 32) * 5 / 9 + 273.15  # Convert Fahrenheit to Kelvin
            viscosity_SI, unit_str_SI = air_viscosity(temperature_value, unit='SI')
            viscosity_USC, unit_str_USC = air_viscosity(temperature_value, unit='USC')
            print(f"Viscosity of air at {temperature_value - 273.15}°C: {viscosity_SI} {unit_str_SI}")
            print(f"Viscosity of air at {temperature_value - 273.15}°C: {viscosity_USC} {unit_str_USC}")

        else:
            raise ValueError("Invalid temperature unit. Please use 'K', 'C', or 'F'.")

    except ValueError as ve:
        print("Error:", ve)


if __name__ == "__main__":
    main()
