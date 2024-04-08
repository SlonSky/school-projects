var rates = {
    USD:22.28,
    EUR:25.20,
    RUB:0.36,
    GBP:34.46,
    CHF:23.15,
    CAD:16.98,
    JPY:0.19,
    UAH:1,
    PLN:5.88,
    AUD:16.06
};
function convert(){
    var sumIn = document.getElementById("input").value;
    if(!isNaN(Number(sumIn))){
        var currencyIn = document.getElementById("inVal").value;
        var currencyOut = document.getElementById("outVal").value;
        var sumOut = sumIn * (rates[currencyIn]/rates[currencyOut]);
        document.getElementById("output").setAttribute("value", sumOut.toFixed(2));
    }
}