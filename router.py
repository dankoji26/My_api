from fastapi import APIRouter, HTTPException, status
from models import Etudiant

router = APIRouter()
list_etudiants = []


@router.post("/etudiants", status_code=status.HTTP_201_CREATED)
async def add_etudiant(etu: Etudiant) -> dict:
    list_etudiants.append(etu)

    return {"message": "Etudiant ajouté avec succès."}

@router.get("/etudiants")
async def get_all_etudiants() -> dict:
    return {"etudiants": list_etudiants}

@router.get("/etudiants/{matricule}")
async def get_etudiant_by_id(matricule: str) -> dict:
    for etudiant in list_etudiants:
        if etudiant.matricule == matricule:
            return {"etudiant": etudiant}
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Etudiant non trouvé."
    )

@router.put("/etudiants/{matricule}")
async def update_etudiant(matricule: str, etu: Etudiant) -> dict:
    position = -1
    for i, etudiant in enummerate(list_etudiants):
        if etudiant.matricule == matricule:
            position = 1
    if position >= 0:
        list_etudiants[position] = etu
        return {"message": "Etudiant modifié avec succès."}
    
    return {"message": "Etudiant non trouvé."}

@router.delete("/etudiants/{matricule}")
async def delete_etudiant(matricule: str) -> dict:
    for etudiant in list_etudiants:
        if etudiant.matricule == matricule:
            list_etudiants.remove(etudiant)
            return {"message": "Etudiant supprimé avec succès."}

        return {"message": "Etudiant non trouvé."}


