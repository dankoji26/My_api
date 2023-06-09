from pydantic import BaseModel

class
class Etudiant(BaseModel):
    matricule: str
    nom: str
    postnom: str
    prenom: str
    genre: str