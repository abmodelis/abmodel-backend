from fastapi import APIRouter, Depends

from app.core.domain.user import SpecializationArea

from ..dependencies.specializations import ApiGetAll

router = APIRouter()


@router.get("/specializations", response_model=list[SpecializationArea])
async def get_all_specializations(get_all: ApiGetAll = Depends()) -> list[SpecializationArea]:
    return get_all()
