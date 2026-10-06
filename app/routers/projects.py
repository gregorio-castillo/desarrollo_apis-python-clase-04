from fastapi import APIRouter, HTTPException

from app.schemas.projects import (
    ProjectCreate,
    ProjectResponse,
)
from app.services.projects import (
    create_project,
    get_project,
    list_projects,
)


router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.post(
        "", 
        response_model=ProjectResponse,
        status_code=201,
        )
def create_project_endpoint(
    request: ProjectCreate,
) -> ProjectResponse:
    return create_project(
        name=request.name,
        description=request.description,
    )

@router.get(
    "",
    response_model=list[ProjectResponse],
)
def list_projects_endpoint(
    status: str | None = None,
) -> list[ProjectResponse]:
    return list_projects(
        status=status,
        )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def read_project_endpoint(
    project_id: int,
) -> ProjectResponse:
    project = get_project(
        project_id = project_id,
    )

    if project is None:
        raise HTTPException(
            status_code = 404,
            detail="Project not found",
        )

    return project