from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name : str = "Joao"
    age : float = 22
    gender : str  = "Male"
    height :  float  = 1.8
    weight :  float = 89.8
    calc : str  = "Sometimes"
    favc : str  = "no"
    fcvc :  float  = 2.0
    ncp : float  = 1.0
    scc : str  = "no"
    smoke : str  = "no"
    ch2o :  float = 2.0
    family_history_with_overweight : str  = "no"
    faf : int  = 0.0
    tue :  int  = 0.0
    caec : str  = "Sometimes"
    mtrans : str  = "Public_Transportation"
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name : str = "Joao"
    age : float = 22.0
    gender : str  = "Male"
    height :  float  = 1.8
    weight :  float = 89.8
    calc : str  = "Sometimes"
    favc : str  = "no"
    fcvc :  float  = 2.0
    ncp : float  = 1.0
    scc : str  = "no"
    smoke : str  = "no"
    ch2o :  float = 2.0
    family_history_with_overweight : str  = "no"
    faf : int  = 0
    tue :  int  = 0
    caec : str  = "Sometimes"
    mtrans : str  = "Public_Transportation"
    nobeyesdad : str =  None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Joao"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Joao"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
            "id":paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "gender": paciente.gender,
            "height": paciente.height,
            "weight": paciente.weight,
            "calc": paciente.calc,
            "favc": paciente.favc,
            "fcvc": paciente.fcvc,
            "ncp": paciente.ncp,
            "scc": paciente.scc,
            "smoke": paciente.smoke,
            "ch2o": paciente.ch2o,
            "family_history_with_overweight": paciente.family_history_with_overweight, 
            "faf": paciente.faf,
            "tue": paciente.tue,
            "caec": paciente.caec,
            "mtrans": paciente.mtrans,
            "nobeyesdad": paciente.nobeyesdad
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
                        "id":paciente.id,
                        "name": paciente.name,
                        "age": paciente.age,
                        "gender": paciente.gender,
                        "height": paciente.height,
                        "weight": paciente.weight,
                        "calc": paciente.calc,
                        "favc": paciente.favc,
                        "fcvc": paciente.fcvc,
                        "ncp": paciente.ncp,
                        "scc": paciente.scc,
                        "smoke": paciente.smoke,
                        "ch2o": paciente.ch2o,
                        "family_history_with_overweight": paciente.family_history_with_overweight, 
                        "faf": paciente.faf,
                        "tue": paciente.tue,
                        "caec": paciente.caec,
                        "mtrans": paciente.mtrans,
                        "nobeyesdad": paciente.nobeyesdad
        })

    return {"pacientes": result}

