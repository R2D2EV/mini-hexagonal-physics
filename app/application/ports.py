"""
PORT

Define QUÉ necesita la aplicación.

No define CÓMO se hace.

La aplicación necesita un repositorio capaz de cumplir un contrato que:

1. guardar cálculos
2. devolver cálculos

El PORT no debería saber de:
- PostgreSQL
- MongoDB
- archivo.json

"""

from typing import Protocol

from app.domain.energy import EnergyCalculation


class EnergyRepository(Protocol):

    def save(
        self,
        calculation: EnergyCalculation,
    ) -> None:
        ...

    def list_all(
            self,
    ) -> list[EnergyCalculation]:
        ...