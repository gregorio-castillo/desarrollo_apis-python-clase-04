from app.schemas.projects import ProjectResponse


def create_project(
    name: str,
    description: str | None,
) -> ProjectResponse:
    return ProjectResponse(
        id=1,
        name=name,
        description=description,
        status="active",
    )


def list_projects(
    status: str | None = None,
) -> list[ProjectResponse]:
    projects = [
        ProjectResponse(
            id=1,
            name="API Course",
            description=None,
            status="active",
        ),
        ProjectResponse(
            id=2,
            name="Legacy Project",
            description=None,
            status="inactive",
        ),
    ]

    if status is None:
        return projects

    return [
        project
        for project in projects
        if project.status == status
    ]


def get_project(
    project_id: int,
) -> ProjectResponse | None:
    if project_id != 1:
        return None
    
    return ProjectResponse(
        id=project_id,
        name="API Course",
        description=None,
        status="active",
    )