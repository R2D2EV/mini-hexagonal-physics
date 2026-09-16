"""
COMPOSITION ROUTE

Aquí ensamblamos todas las piezas.

repository
    ↓
use cases
    ↓
FastAPI adapter

Este es prácticamente el único lugar que conoce
las implementaciones concretas.
"""

from fastapi import FastAPI

from app.application.use_cases import (
    CalculateKineticEnergy,
    ListEnergyCalculations
)

from app.infrastructure.api import create_router
from app.infrastructure.repository import InMemoryEnergyRepository

# --------------------------------------------------
# 1. Creamos el adaptador de persistencia
# --------------------------------------------------

repository = InMemoryEnergyRepository()

# --------------------------------------------------
# 2. Inyectamos el repositorio en los casos de uso
# --------------------------------------------------

calculate_energy = CalculateKineticEnergy(
    repository=repository,
)

list_calculations = ListEnergyCalculations(
    repository=repository
)

# --------------------------------------------------
# 3. Creamos FastAPI
# --------------------------------------------------

app = FastAPI(
    title="Mini Hexagonal Physics API"
)

# --------------------------------------------------
# 4. Conectamos el adaptador HTTP
# --------------------------------------------------

router = create_router(
    calculate_energy=calculate_energy,
    list_calculations=list_calculations,
)

app.include_router(router)