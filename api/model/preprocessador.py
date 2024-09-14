import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class PreProcessador:

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def preparar_form(self,form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
       # Criar um dicionário com os valores recebidos do formulário
        data = {
            'Age': [form.age],
            'Gender': [form.gender],
            'Height': [form.height],
            'Weight': [form.weight],
            'CALC': [form.calc],
            'FAVC': [form.favc],
            'FCVC': [form.fcvc],
            'NCP': [form.ncp],
            'SCC': [form.scc],
            'SMOKE': [form.smoke],
            'CH2O': [form.ch2o],
            'family_history_with_overweight': [form.family_history_with_overweight],
            'FAF': [form.faf],
            'TUE': [form.tue],
            'CAEC': [form.caec],
            'MTRANS': [form.mtrans]
        }
        
        # Converter em DataFrame
        df = pd.DataFrame(data)
        
        # Codificar variáveis categóricas (usar o mesmo método que você usou no treino)
        df_encoded = pd.get_dummies(df)
        
        # Carregar as colunas do treino
        colunas_treino = pd.read_csv('./MachineLearning/data/X_test_dataset_obesidade.csv').columns
        
        # Verificar o alinhamento das colunas (as colunas de df_encoded devem ter o mesmo número e ordem)
        df_encoded = df_encoded.reindex(columns=colunas_treino, fill_value=0)
        
        # Verificar se o número de colunas está correto
        if df_encoded.shape[1] != len(colunas_treino):
            raise ValueError("Erro: o número de colunas no formulário não corresponde ao número esperado do conjunto de treino.")

        # Converter o DataFrame para numpy array
        df_encoded_np = df_encoded.values
        
        # Certificar que as colunas estejam alinhadas com as colunas do treino
        with open('./MachineLearning/scalers/standard_scaler_obesidade.pkl', 'rb') as f:
            scaler = pickle.load(f)
                
        # Normalizar/padronizar os dados de entrada
        X_input = scaler.transform(df_encoded_np)
        
        return X_input
    
    def scaler(self,X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/scalers/standard_scaler_obesidade.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
