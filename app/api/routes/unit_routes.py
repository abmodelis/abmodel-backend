from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.jwt import CurrenUserDependency
from app.api.dependencies.units_use_cases import SQLUnitCrud
from app.core.domain.unit import Unit
from app.core.use_cases.units.schemas import UnitIn

router = APIRouter()


@router.post("/", dependencies=[CurrenUserDependency], response_model=Unit)
async def create_unit(unit_in: UnitIn, crud: SQLUnitCrud = Depends()):
    return crud.create(unit_in)


@router.get("/", dependencies=[CurrenUserDependency], response_model=list[Unit])
async def get_all_units(crud: SQLUnitCrud = Depends()):
    return crud.get_all()


@router.put("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Unit)
async def update_by_id(entity_id: int, unit_in: UnitIn, crud: SQLUnitCrud = Depends()):
    unit = crud.update(entity_id, unit_in)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit


@router.delete("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Unit)
async def delete_by_id(entity_id: int, crud: SQLUnitCrud = Depends()):
    unit = crud.delete(entity_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit
