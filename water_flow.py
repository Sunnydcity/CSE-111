def water_column_height(tower_height: float, tank_height: float) -> float:
    """Calculate the water column height using the formula: h = t + (3 * w) / 4."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height: float) -> float:
    """
    Calculate the pressure caused by the water column.
    P = (ρ * g * h) / 1000
    ρ = 998.2 kg/m³ (density of water), g = 9.80665 m/s² (gravity)
    """
    ρ = 998.2  # density in kg/m³
    g = 9.80665  # gravity in m/s²
    return (ρ * g * height) / 1000


def pressure_loss_from_pipe(pipe_diameter: float, pipe_length: float, friction_factor: float, fluid_velocity: float) -> float:
    """
    Calculate the pressure loss due to friction in a pipe.
    P = -(f * L * ρ * v²) / (2000 * d)
    """
    ρ = 998.2  # density in kg/m³
    return -(friction_factor * pipe_length * ρ * fluid_velocity**2) / (2000 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity: float, quantity_fittings: int) -> float:
    """
    Calculate the pressure loss due to fittings.
    P = -(0.04 * ρ * v² * n) / 2000
    """
    ρ = 998.2  # density of water in kg/m³
    return -(0.04 * ρ * fluid_velocity**2 * quantity_fittings) / 2000


def reynolds_number(hydraulic_diameter: float, fluid_velocity: float) -> float:
    """
    Calculate the Reynolds number.
    R = (ρ * d * v) / μ
    ρ = 998.2 kg/m³ (density of water), μ = 0.0010016 Pa·s (dynamic viscosity)
    """
    ρ = 998.2  # density of water in kg/m³
    μ = 0.0010016  # dynamic viscosity of water in Pa·s
    return (ρ * hydraulic_diameter * fluid_velocity) / μ


def pressure_loss_from_pipe_reduction(larger_diameter: float, fluid_velocity: float, reynolds_number: float, smaller_diameter: float) -> float:
    """
    Calculate the pressure loss due to a reduction in pipe diameter.
    k = 0.1 + (50 / R) * ((D/d)^4 - 1)
    P = -(k * ρ * v²) / 2000
    """
    ρ = 998.2  # density of water in kg/m³
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -(k * ρ * fluid_velocity**2) / 2000


def main():
    try:
        tower_height = float(input("Height of water tower (meters): "))
        tank_height = float(input("Height of water tank walls (meters): "))
        length1 = float(input("Length of supply pipe from tank to lot (meters): "))
        quantity_angles = int(input("Number of 90° angles in supply pipe: "))
        length2 = float(input("Length of pipe from supply to house (meters): "))
        
        # Water column height and pressure gain
        water_height = water_column_height(tower_height, tank_height)
        pressure = pressure_gain_from_water_height(water_height)

        # Pressure loss due to the first pipe
        pressure += pressure_loss_from_pipe(
            PVC_SCHED80_INNER_DIAMETER, length1, PVC_SCHED80_FRICTION_FACTOR, SUPPLY_VELOCITY
        )

        # Pressure loss due to fittings
        pressure += pressure_loss_from_fittings(SUPPLY_VELOCITY, quantity_angles)

        # Pressure loss due to pipe reduction
        reynolds = reynolds_number(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY)
        pressure += pressure_loss_from_pipe_reduction(
            PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY, reynolds, HDPE_SDR11_INNER_DIAMETER
        )

        # Pressure loss due to second pipe
        pressure += pressure_loss_from_pipe(
            HDPE_SDR11_INNER_DIAMETER, length2, HDPE_SDR11_FRICTION_FACTOR, HOUSEHOLD_VELOCITY
        )

        # Output the final pressure
        print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for heights and lengths.")


# Constants for pipe specifications
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters (11.294 inches)
PVC_SCHED80_FRICTION_FACTOR = 0.013   # unitless
SUPPLY_VELOCITY = 1.65                # meters/second

HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters (1.917 inches)
HDPE_SDR11_FRICTION_FACTOR = 0.018    # unitless
HOUSEHOLD_VELOCITY = 1.75             # meters/second


if __name__ == "__main__":
    main()
