from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

next_id = 1
orgs_list = []

class OrganisationCreate(BaseModel):
    name: str | None = None
    status: str | None = None
    description: str | None = None

@app.get("/")
def home():
    return {"message": "api running using python fastapi framework"}

@app.post("/organisations")
def create_orgs(org: OrganisationCreate):
    global next_id

    organisation = {
        "id": next_id,
        "name": org.name,
        "status": org.status,
        "description": org.description
    }

    next_id += 1

    orgs_list.append(organisation)

    return {
        "message": "Organisation created.",
        "org": organisation
    }

@app.get("/listorgs")
def list_orgs():
    return orgs_list

@app.get("/listorgs/{id}")
def get_org(id: int):
    for o in orgs_list:
        if o["id"] == id:
            return o

    return {"message": "Organization not found"}

@app.delete("/listorgs/{id}")
def delete_org(id: int):
    for o in orgs_list:
        if o["id"] == id:
            orgs_list.remove(o)
            return {"message": f"org with id {id} deleted."}

    return {"message": "Organization not found"}

@app.put("/listorgs/{id}")
def update_org(id: int, org: OrganisationCreate):

    for o in orgs_list:

        if o["id"] == id:

            o["name"] = org.name
            o["status"] = org.status
            o["description"] = org.description

            return o

    return {"message": "Organization not found"}

@app.patch("/listorgs/{id}")
def patch_org(id: int, org: OrganisationCreate):

    for o in orgs_list:

        if o["id"] == id:

            if org.name is not None:
                o["name"] = org.name

            if org.status is not None:
                o["status"] = org.status

            if org.description is not None:
                o["description"] = org.description

            return o

    return {"message": "Organisation not found"}