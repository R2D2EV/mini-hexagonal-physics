"""
OUTBOUND ADAPTER

Implementación concreta del puerto EnergyRepository.

En este ejemplo usamos simplemente una lista de Python.

Mañana podríamos reemplazar este adaptador por:

- PostgreSQL
- Cloud SQL
- Firestore
- SQLite

sin modificar el dominio.
"""

from app.domain.energy import EnergyCalculation


class InMemoryEnergyRepository:
    def __init__(self) -> None:
        self._calculations: list[EnergyCalculation] = []

    def save(
        self,
        calculation: EnergyCalculation,
    ) -> None:
        self._calculations.append(calculation)

    def list_all(
        self,
    ) -> list[EnergyCalculation]:

        return self._calculations.copy()

