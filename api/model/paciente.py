from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age = Column("Age", Float)
    gender = Column("Gender", String(50))
    height = Column("Height", Float)
    weight = Column("Weight", Float)
    calc = Column("CALC", String(4))
    favc = Column("FAVC", String(4))
    fcvc = Column("FCVC", Float)
    ncp = Column("NCP", Float)
    scc = Column("SCC", String(4))
    smoke = Column("SMOKE", String(4))
    ch2o = Column("CH2O", Float)
    family_history_with_overweight = Column("Family_History_With_Overweight", String(4))
    faf = Column("FAF", Integer)
    tue = Column("TUE", Integer)
    caec = Column("CAEC", String(50))
    mtrans = Column("MTRANS", String(50))
    nobeyesdad = Column("NObeyesdad", String(50), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self,name:str, age:float, gender:str , height: float , weight: float,
                 calc:str , favc:str , fcvc: float , ncp:float , scc:str , smoke:str , ch2o: float,
                 family_history_with_overweight:str , faf:int , tue: int , caec:str , mtrans:str , nobeyesdad:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
        name: nome do paciente
        Age: Caracteristica, Continua, "Idade"
        Gender(Gênero): Característica, Categórica, "Gênero"
        Height(Altura): Característica, Contínua
        Weight(Peso): Característica, Contínua
        CALC: Característica, Categórica, "Com que frequência você consome álcool?"
        FAVC: Característica, Binária, "Você consome alimentos de alto teor calórico com frequência?"
        FCVC: Característica, Inteira, "Você costuma comer vegetais em suas refeições?"
        NCP: Característica, Contínua, "Quantas refeições principais você faz diariamente?"
        SCC: Característica, Binária, "Você monitora as calorias que consome diariamente?"
        SMOKE(FUMA): Característica, Binária, "Você fuma?"
        CH2O: Característica, Contínua, "Quanta água você bebe diariamente?"
        family_history_with_overweight(Histórico familiar de sobrepeso): Característica, Binária, "Algum membro da família já sofreu ou sofre de sobrepeso?"
        FAF: Característica, Contínua, "Com que frequência você pratica atividade física?"
        TUE: Característica, Inteira, "Quanto tempo você usa dispositivos tecnológicos como celular, videogames, televisão, computador e outros?"
        CAEC: Característica, Categórica, "Você come algum alimento entre as refeições?"
        MTRANS: Característica, Categórica, "Qual meio de transporte você costuma usar?"
        NObeyesdad: Alvo, Categórica, "Nível de obesidade"
        data_insercao: data de quando o paciente foi inserido à base
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight =  weight
        self.calc = calc
        self.favc = favc
        self.fcvc = fcvc
        self.ncp = ncp
        self.scc = scc
        self.smoke = smoke
        self.ch2o = ch2o
        self.family_history_with_overweight = family_history_with_overweight
        self.faf = faf
        self.tue = tue
        self.caec = caec
        self.mtrans = mtrans
        self.nobeyesdad = nobeyesdad


        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao