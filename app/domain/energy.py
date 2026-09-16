"""

DOMAIN

Contiene las reglas fundamentales del problema.

No sabe:
- qué es FastAPI
- qué es PostgreSQL
- qué es HTTP
- qué es Docker
- qué es GCP

Solamente conoce física.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class EnergyCalculation:
    mass_kg: float
    speed_m_s: float
    energy_j: float

    @classmethod
    def create(
        cls,
        mass_kg: float,
        speed_m_s: float,
    ) -> "EnergyCalculation":

        if mass_kg <= 0:
            raise ValueError("Mass must be greater than zero.")

        if speed_m_s < 0:
            raise ValueError("Speed cannot be negative.")

        energy_j = 0.5 * mass_kg * speed_m_s**2

        return cls(
            mass_kg=mass_kg,
            speed_m_s=speed_m_s,
            energy_j=energy_j,
        )