"""
Test del núcleo de nuestra aplicación.

Observa que NO levantamos FastAPI.

Probamos directamente:

Use Case
+
Repository
+
Domain

Esto hace los tests pequeños y rápidos.
"""

from app.application.use_cases import CalculateKineticEnergy
from app.infrastructure.repository import InMemoryEnergyRepository


def test_calculate_kinetic_energy():

    repository = InMemoryEnergyRepository()

    use_case = CalculateKineticEnergy(
        repository=repository,
    )

    result = use_case.execute(
        mass_kg=10,
        speed_m_s=3,
    )

    assert result.energy_j == 45