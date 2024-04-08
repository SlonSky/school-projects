/**
 * Created by F5 on 03.11.2015.
 */

var i, j;
var field = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
];
var row, column;
var cells = document.getElementsByTagName('td');
var rows = document.getElementsByTagName('tr');
var gaming = false;
var timeMove = 0;
var timeGame = 0;

function mark0(row, column){
    if(field[row][column] == 1){
        field[row][column] = '0';
        cells[row*4 + column].innerHTML = '0';
    }
}
function putSecondMark(i, j){
    var k = i-1, l = j-1, k_end = i+2, l_end = j+2;
    if(i-1 < 0){
        k = 0;
    }
    if(j-1 <= 0){
        l = 0;
    }
    if(i+2 > 4){
        k_end = 4;
    }
    if(j+2 > 4){
        l_end = 4;
    }
    for(; k < k_end; k++){
        for(; l < l_end; l++){
            if(k == i && l == j){
                continue;
            }
            if(field[k][l] == 1){
                field[k][l] = 'X';
                cells[k*4 + l].innerHTML = 'X';
                return 1;
            }
        }
    }
    return 0;
}
function markX(){
    timeMove = 0;
    // put second mark
    for(i = 0; i < 4; i++){
        for(j = 0; j < 4; j++){
            if(field[i][j] == 'X'){
                if(putSecondMark(i, j)){
                    return;
                }
            }
        }
    }

    // mark center
    if(field[1][1] == 1 || field[1][2] == 1
        || field[2][1] == 1 || field[2][2] == 1){
        do{
            var row = Math.floor(Math.random()*2 + 1);
            var column = Math.floor(Math.random()*2 + 1);
            if(field[row][column] != 1){
                continue;
            }
            field[row][column] = 'X';
            cells[row*4 + column].innerHTML = 'X';
            break;
        }while(1);
    }

}
function checkVictory(){
    var markX = 0, mark0 = 0;

    // horizontal victory check
    for(i = 0; i < 4; i++){
        mark0 = markX = 0;
        for(j = 0; j < 4; j++){
            if(field[i][j] == '0'){
                mark0++;
                if(mark0 == 3){
                    return '0';
                }
            }
            else{
                mark0 = 0;
            }
            if(field[i][j] == 'X'){
                markX++;
                if(markX == 3){
                    return 'X';
                }
            }
            else{
                markX = 0;
            }
        }
    }
    // vertical victory check
    for(i = 0; i < 4; i++){
        mark0 = markX = 0;
        for(j = 0; j < 4; j++){
            if(field[j][i] == '0'){
                mark0++;
                if(mark0 == 3){
                    return '0';
                }
            }
            else{
                mark0 = 0;
            }
            if(field[j][i] == 'X'){
                markX++;
                if(markX == 3){
                    return 'X';
                }
            }
            else{
                markX = 0;
            }
        }
    }

    // diagonal victory check
    for(i = 1; i < 3; i++){
        for(j = 1; j < 3; j++){
            if((field[i][j] == '0')
                && ((field[i-1][j-1] == '0' && field[i+1][j+1] == '0')
                || (field[i-1][j+1] == '0' && field[i+1][j-1] == '0'))){
                return '0';
            }
            if((field[i][j] == 'X')
                && ((field[i-1][j-1] == 'X' && field[i+1][j+1] == 'X')
                || (field[i-1][j+1] == 'X' && field[i+1][j-1] == 'X'))){
                return 'X';
            }
        }
    }
}
for(i = 0; i < cells.length; i++){
    cells[i].onclick = function(){
        column = this.cellIndex;
    };
}
for(i = 0; i < rows.length; i++){
    rows[i].onclick = function(){
        row = this.rowIndex;
        mark0(row, column);
        markX();
        if(checkVictory() == 'X'){
            alert("Компьютер победил.");
            gaming = false;
        }
        else if(checkVictory() == '0'){
            alert("Ты выиграл.");
            gaming = false;
        }
    };
}
document.getElementById("newGame").onclick = function(){
  for(i = 0; i < 4; i++) {
      for (j = 0; j < 4; j++){
        gaming = true;
        timeGame = 0;
        field[i][j] = 1;
        cells[i*4 + j].innerHTML = '';
      }
  }
  alert("Ты ходишь вторым, человек.");
  markX();
};
window.setInterval(function(){
    if(gaming){
        // ++timer;
        ++timeMove;
        // = timer;
        ++timeGame;
        //= timer;
        document.getElementById("moveTime").innerHTML = timeMove;
        document.getElementById("generalTime").innerHTML = timeGame;
    }
}, 1000);
