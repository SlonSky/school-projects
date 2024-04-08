var currentMatrix;

var W;

// Init
setOnClick();

function click(a) {
	console.log(a);
	if(this.style.backgroundColor != 'rgb(0, 0, 0)')
		this.style.backgroundColor = 'rgb(0, 0, 0)'; 
	else
		this.style.removeProperty('background-color');
}

function setOnClick() {

	cells = $('#inputTable tr td');

	for(var i = 0; i < cells.length; i++) {
		cells[i].onclick = click;
	}
}

function getUserMatrix() {

	var width = $('#inputTable tr:first-child td').length;
	var height = $('#inputTable tr').length;

	currentMatrix = new Matrix(undefined, width, height);

	for(var i = 0; i < height; i++) {
		for(var j = 0; j < width; j++) {

			if($('#inputTable tr:nth-child('+(i+1)+') td:nth-child('+(j+1)+')').css('backgroundColor') == 'rgb(0, 0, 0)') {
				currentMatrix.set(i, j, 1);
			} else {
				currentMatrix.set(i, j, -1);
			}
		}
	}

	// $('#qwert').css('display', 'hidden');
	// console.log($('#qwert').css('display'));
}

function setUserMatrix(matrix, table) {
	
}

function addRow() {
	
	var columnsAmount = $('#inputTable tr:first-child td').length;

	// inputTable
	$('#inputTable').append('<tr>');
	for(var i = 0; i < columnsAmount; i++){
		$('#inputTable tr:last-child').append('<td>');
	}

	// outputTable
	$('#outputTable').append('<tr>');
	for(var i = 0; i < columnsAmount; i++){
		$('#outputTable tr:last-child').append('<td>');
	}

	setOnClick();
}

function removeRow() {
	$('#inputTable tr:last-child').remove();
	$('#outputTable tr:last-child').remove();
}

function removeColumn() {
	$('#inputTable tr td:last-child').remove();
	$('#outputTable tr td:last-child').remove();
}

function addColumn() {

	var rowsAmount = $('#inputTable tr').length;

	// inputTable
	for(var i = 0; i < rowsAmount + 1; i++){
		$('#inputTable tr:nth-child(' + i + ')').append('<td>');
	}

	// outputTable
	for(var i = 0; i < rowsAmount + 1; i++){
		$('#outputTable tr:nth-child(' + i + ')').append('<td>');
	}

	setOnClick();
}

function clearTables() {

	console.log('clearTables');

	var cells = document.getElementsByTagName('td');
	for (var i = 0; i < cells.length; i++) {
		cells[i].style.removeProperty('background-color');
	}	
}

