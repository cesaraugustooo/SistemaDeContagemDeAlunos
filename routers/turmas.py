from fastapi import APIRouter,HTTPException
from schemas.categoria import CategoriaSchemaCreate,CategoriaSchema,CategoriaRead,CategoriaList,CategoriaUpdate,TurmaCreate,TurmaBase,TurmaOut,TurmaUpdate,TurmaRead
from models.turmas import Categoria,Turma
from fastapi.responses import HTMLResponse


router = APIRouter(prefix='/turmas', tags=['Turmas'])


@router.post("/turmas", response_model=TurmaOut)
async def create_turma(turma1: TurmaCreate):
    nova_turma = Turma.create(**turma1.model_dump())
    return nova_turma

@router.get("/turmas", response_model=list[TurmaOut])
async def list_turmas():
    turmas = Turma.select().where(Turma.ativo == True)
    return turmas

@router.put("/turmas/{turma_id}", response_model=TurmaOut)
async def update_turma(turma_id: int, turma: TurmaUpdate):
    Turma.update(**turma.dict(exclude_unset=True)).where(Turma.id == turma_id).execute()
    return Turma.get_by_id(turma_id)

@router.delete("/turmas/{turma_id}")
async def deactivate_turma(turma_id: int):
    Turma.update(ativo=False).where(Turma.id == turma_id).execute()
    return {"message": "Turma desativada com sucesso"}

