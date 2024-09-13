from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com obesidade")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os pacientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        # Se não houver pacientes
        return {"pacientes": []}, 200
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        print(pacientes)
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        Name(str): Nome do paciente
        Age(float): Característica, Contínua, "Idade"
        Gender(str): Característica, Categórica, "Gênero"
        Height(float): Característica, Contínua
        Weight(float): Característica, Contínua
        CALC(str): Característica, Categórica, "Com que frequência você consome álcool?"
        FAVC(str): Característica, Binária, "Você consome alimentos de alto teor calórico com frequência?"
        FCVC(float): Característica, Inteira, "Você costuma comer vegetais em suas refeições?"
        NCP(float): Característica, Contínua, "Quantas refeições principais você faz diariamente?"
        SCC(str): Característica, Binária, "Você monitora as calorias que consome diariamente?"
        SMOKE(str): Característica, Binária, "Você fuma?"
        CH2O(float): Característica, Contínua, "Quanta água você bebe diariamente?"
        family_history_with_overweight(str): Característica, Binária, "Algum membro da família já sofreu ou sofre de sobrepeso?"
        FAF(int): Característica, Contínua, "Com que frequência você pratica atividade física?"
        TUE(int): Característica, Inteira, "Quanto tempo você usa dispositivos tecnológicos como celular, videogames, televisão, computador e outros?"
        CAEC(str): Característica, Categórica, "Você come algum alimento entre as refeições?"
        MTRANS(str): Característica, Categórica, "Qual meio de transporte você costuma usar?"
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    # Instanciação das Classes
    #carregador = Carregador()
    model = Model()
    #avaliador = Avaliador()
    preProcessador = PreProcessador()
    pipeline = Pipeline()
    
    # Recuperando os dados do formulário
    name = form.name
    age = form.age
    gender = form.gender
    height = form.height
    weight = form.weight
    calc = form.calc
    favc = form.favc
    fcvc = form.fcvc
    ncp = form.ncp
    scc = form.scc
    smoke = form.smoke
    ch2o = form.ch2o
    family_history_with_overweight = form.family_history_with_overweight 
    faf = form.faf
    tue = form.tue
    caec = form.caec
    mtrans = form.mtrans
        
    # Preparando os dados para o modelo
    X_input = preProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/pipelines/bg_obesidade_pipeline.pkl' #'./MachineLearning/pipelines/bg_obesidade_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modeloPred = pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    #nobeyesdad = model.preditor(modeloPred, X_input)[0]
    
    paciente = Paciente(
                name = name,
                age = age,
                gender = gender,
                height = height,
                weight = weight,
                calc = calc,
                favc = favc,
                fcvc = fcvc,
                ncp = ncp,
                scc = scc,
                smoke = smoke,
                ch2o = ch2o,
                family_history_with_overweight = family_history_with_overweight,
                faf = faf,
                tue = tue,
                caec = caec,
                mtrans = mtrans,
                nobeyesdad = "nobeyesdad"
    )
    logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)