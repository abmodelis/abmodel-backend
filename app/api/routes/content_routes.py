from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.contents_use_cases import SQLContentsCrud
from app.api.dependencies.jwt import CurrenUserDependency
from app.core.domain.content import Content
from app.core.use_cases.contents.schemas import ContentIn

router = APIRouter()


@router.post("/", dependencies=[CurrenUserDependency], response_model=Content)
async def create_content(content_in: ContentIn, crud: SQLContentsCrud = Depends()):
    try:
        return crud.create(content_in)
    except Exception as error:
        # TODO: create error handler
        raise HTTPException(status_code=409, detail=repr(error)) from error


@router.get("/", dependencies=[CurrenUserDependency], response_model=list[Content])
async def get_all_contents(crud: SQLContentsCrud = Depends()):
    return crud.get_all()


@router.get("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Content)
async def get_content_by_id(entity_id: int, crud: SQLContentsCrud = Depends()):
    content = crud.get_by_id(entity_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content


@router.put("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Content)
async def update_content(entity_id: int, content_in: ContentIn, crud: SQLContentsCrud = Depends()):
    try:
        return crud.update(entity_id, content_in)
    except Exception as error:
        # TODO: create error handler
        raise HTTPException(status_code=209, detail=repr(error)) from error


@router.delete("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Content)
async def delete_content(entity_id: int, crud: SQLContentsCrud = Depends()):
    content = crud.delete(entity_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content
