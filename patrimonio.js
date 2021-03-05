var saldoCarteira = 0;
var cotasPossuidas = 0;
var patrimonio = 0;
var arrayResultado = [];


function calculaTabela() {
    limparTela();

    var aporteInicial = parseFloat(document.getElementById("nmAporte").value);
    var aporteMensal = parseFloat(document.getElementById("nmAporteMensal").value);
    var vlCota = parseFloat(document.getElementById("nmCota").value);
    var dividendo = parseFloat(document.getElementById("nmDividendo").value);
    var prazo = parseInt(document.getElementById("nmPrazo").value);



    cotasPossuidas = cotasPossuidas + Math.trunc(aporteInicial / vlCota);

    var lucroMes = cotasPossuidas * dividendo;

    saldoCarteira = saldoCarteira + (aporteInicial - (cotasPossuidas * vlCota)) +lucroMes;
    patrimonio = saldoCarteira + (cotasPossuidas * vlCota);


    arrayResultado = [{
        mesAtual: 0,
        cotasNaCarteira: cotasPossuidas,
        saldoFinal: saldoCarteira.toFixed(2),
        patrimonioAtual: patrimonio.toFixed(2),
        lucroAtual: lucroMes.toFixed(2)
    }];


    for (let linhaMes = 1; linhaMes <= prazo; linhaMes++) {
        saldoCarteira = saldoCarteira + aporteMensal + lucroMes;


        if (saldoCarteira >= vlCota) {
            var cotasParaCompra = Math.trunc(saldoCarteira / vlCota)
            cotasPossuidas = cotasPossuidas + cotasParaCompra;
            saldoCarteira = saldoCarteira - (cotasParaCompra * vlCota);

        }        


        lucroMes = cotasPossuidas * dividendo;

        patrimonio = saldoCarteira + (cotasPossuidas * vlCota) + lucroMes;

        arrayResultado.push({
            mesAtual: linhaMes,
            cotasNaCarteira: cotasPossuidas,
            saldoFinal: saldoCarteira.toFixed(2),
            patrimonioAtual: patrimonio.toFixed(2),
            lucroAtual: lucroMes.toFixed(2)
        });
    }

}

function populaTabela() {
    calculaTabela();
    let table = document.querySelector("tbody");


    for (let element of arrayResultado) {
        let row = table.insertRow();
        for (key in element) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text);
        }
    }

};

function limparTela() {
    console.log();
    saldoCarteira = 0;
    cotasPossuidas = 0;
    patrimonio = 0;
    arrayResultado = [];
    let tbody = document.querySelector("tbody");
    tbody.innerHTML = '';
}