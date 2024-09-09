/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/pacientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.name,
                                                item.age,
                                                item.gender,
                                                item.height,
                                                item.weight,
                                                item.calc,
                                                item.favc,
                                                item.fcvc,
                                                item.ncp,
                                                item.scc,
                                                item.smoke,
                                                item.ch2o,
                                                item.family_history_with_overweight,
                                                item.faf,
                                                item.tue,
                                                item.caec,
                                                item.mtrans,
                                                item.nobeyesdad
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputName,
                        inputAge ,
                        inputGender,
                        inputHeight, 
                        inputWeight,
                        inputCALC,
                        inputFAVC,
                        inputFCVC,
                        inputNCP,
                        inputSCC,
                        inputSMOKE, 
                        inputCH2O,
                        inputfamily_history_with_overweight, 
                        inputFAF, 
                        inputTUE, 
                        inputCAEC, 
                        inputMTRANS 
                        ) => {
    
  const formData = new FormData();
  formData.append('name', inputName);
  formData.append('age', inputAge);
  formData.append('gender', inputGender);
  formData.append('height', inputHeight);
  formData.append('weight', inputWeight);
  formData.append('calc', inputCALC);
  formData.append('favc', inputFAVC );
  formData.append('fcvc', inputFCVC );
  formData.append('ncp', inputNCP );
  formData.append('scc', inputSCC );
  formData.append('smoke', inputSMOKE );
  formData.append('ch2o', inputCH2O );
  formData.append('family_history_with_overweight', inputfamily_history_with_overweight );
  formData.append('faf', inputFAF );
  formData.append('tue', inputTUE );
  formData.append('caec', inputCAEC );
  formData.append('mtrans', inputMTRANS );

  let url = 'http://127.0.0.1:5000/paciente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/paciente?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputName = document.getElementById("newInput").value;
  let inputAge = document.getElementById("newAge").value;
  let inputGender =	document.getElementById("newGender").value;
  let inputHeight =	document.getElementById("newHeight").value;
  let inputWeight =	document.getElementById("newWeight").value;
  let inputCALC =	document.getElementById("newCALC").value;
  let inputFAVC =	document.getElementById("newFAVC").value;
  let inputFCVC =	document.getElementById("newFCVC").value;
  let inputNCP =	document.getElementById("newNCP").value;
  let inputSCC =	document.getElementById("newSCC").value;
  let inputSMOKE =	document.getElementById("newSMOKE").value;
  let inputCH2O =	document.getElementById("newCH2O").value;
  let inputfamily_history_with_overweight =	document.getElementById("newfamily_history_with_overweight").value;
  let inputFAF =	document.getElementById("newFAF").value;
  let inputTUE =	document.getElementById("newTUE").value;
  let inputCAEC =	document.getElementById("newCAEC").value;
  let inputMTRANS =	document.getElementById("newMTRANS").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/pacientes?nome=${inputName}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.pacientes && data.pacientes.some(item => item.name === inputPatient)) {
        alert("O paciente já está cadastrado.\nCadastre o paciente com um nome diferente ou atualize o existente.");
      } else if (inputName === '') {
        alert("O nome do paciente não pode ser vazio!");
      // } else if (isNaN(inputPreg) || isNaN(inputPlas) || isNaN(inputPres) || isNaN(inputSkin) || isNaN(inputTest) || isNaN(inputMass) || isNaN(inputPedi) || isNaN(inputAge)) {
      //   alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputName,inputAge,inputGender,inputHeight,inputWeight,inputCALC,inputFAVC,inputFCVC,inputNCP,inputSCC,inputSMOKE,inputCH2O,inputfamily_history_with_overweight,inputFAF,inputTUE,inputCAEC,inputMTRANS);
        postItem(inputName,inputAge,inputGender,inputHeight,inputWeight,inputCALC,inputFAVC,inputFCVC,inputNCP,inputSCC,inputSMOKE,inputCH2O,inputfamily_history_with_overweight,inputFAF,inputTUE,inputCAEC,inputMTRANS);
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (name,age,gender,height,weight,calc,favc,fcvc,ncp,scc,smoke,ch2o,family_history_with_overweight,faf,tue,caec,mtrans,nobeyesdad) => {
  var item = [name,age,gender,height,weight,calc,favc,fcvc,ncp,scc,smoke,ch2o,family_history_with_overweight,faf,tue,caec,mtrans,nobeyesdad];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newGender").value = "";
  document.getElementById("newHeight").value = "";
  document.getElementById("newWeight").value = "";
  document.getElementById("newCALC").value = "";
  document.getElementById("newFAVC").value = "";
  document.getElementById("newFCVC").value = "";
  document.getElementById("newNCP").value = "";
  document.getElementById("newSCC").value = "";
  document.getElementById("newSMOKE").value = "";
  document.getElementById("newCH2O").value = "";
  document.getElementById("newfamily_history_with_overweight").value = "";
  document.getElementById("newFAF").value = "";
  document.getElementById("newTUE").value = "";
  document.getElementById("newCAEC").value = "";
  document.getElementById("newMTRANS").value = "";

  removeElement();
}