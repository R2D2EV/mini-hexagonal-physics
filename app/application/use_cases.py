"""

APPLICATION

Coordina los casos de uso.

No calcula directamente la física.
No sabe dónde se guardan los datos.
No sabe que existe FastAPI.

Orquesta:

input
→ dominio
→ repositorio
→ resultado
"""

from app.application.ports import EnergyRepository
from app.domain.energy import EnergyCalculation

class CalculateKineticEnergy:

    def __init__(
        self,
        repository: EnergyRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        mass_kg: float,
        speed_m_s: float,
    ) -> EnergyCalculation:

        calculation = EnergyCalculation.create(
            mass_kg=mass_kg,
            speed_m_s=speed_m_s,
        )
        self.repository.save(calculation)

        return calculation

class ListEnergyCalculations:

    def __init__(
        self,
        repository: EnergyRepository
    ) -> None:
        self.repository = repository

    def execute(
        self,
    ) -> list[EnergyCalculation]:

        return self.repository.list_all()
"""
repository = InMemoryEnergyRepository()
                  │
                  ▼
use_case = CalculateKineticEnergy(repository)
                  │
                  │
                  └── use_case.repository = repository


use_case.execute(4, 5)
        │
        ▼
EnergyCalculation.create(4, 5)
        │
        ▼
EnergyCalculation(4, 5, 50)
        │
        ▼
calculation
        │
        ▼
self.repository.save(calculation)
        │
        ▼
use_case.repository.save(calculation)
        │
        ▼
repository.save(calculation)

"""
