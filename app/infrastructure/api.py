"""
INBOUND ADAPTER

FastAPI traduce:

HTTP
↓
Python
↓
Use Case

FastAPI NO contiene la lógica de negocio.
"""

from dataclasses import asdict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.application.use_cases import (
    CalculateKineticEnergy,
    ListEnergyCalculations,
)

class EnergyRequest(BaseModel):
    mass_kg: float
    speed_m_s: float

def create_router(
        calculate_energy: CalculateKineticEnergy,
        list_calculations: ListEnergyCalculations,
) -> APIRouter:

    router = APIRouter()
    # Cjto. EndPoints - Post, Get , ...

    @router.post("/energy")
    def calculate(request: EnergyRequest):

        try:
            result = calculate_energy.execute(
                mass_kg=request.mass_kg,
                speed_m_s=request.speed_m_s
            )

            return asdict(result)

        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error),
            )

    @router.get("/history")
    def history():

        calculations = list_calculations.execute()

        return [
            asdict(calculation)
            for calculation in calculations
        ]

    return router