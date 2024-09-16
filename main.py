from fastapi import FastAPI
from config.database import conect,end_database
from routers.turmas import router as turma_router
from routers.categorias import router as categorias_router
from routers.usuarios import router as usuarios_router
from routers.tipos import router as tipos_router
from routers.cotagens import router as contagens_router

app = FastAPI()


app.add_event_handler(event_type='startup', func=conect)
app.add_event_handler(event_type='shutdown',func=end_database)

app.include_router(turma_router)
app.include_router(categorias_router)
app.include_router(usuarios_router)
app.include_router(tipos_router)
app.include_router(contagens_router)