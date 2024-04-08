function learn() {

	getUserMatrix();

	var localW = currentMatrix.toVector().mult(currentMatrix.toVector());

	if(W === undefined) {
		W = new Matrix(undefined, localW.length(), localW.height());
	}

	W = W.add(localW);

	for(var i = 0; i < W.height(); i++) {
		W.set(i, i, 0);
	}
}

function check() {
	
	var outputVector = currentMatrix.toVector();

	
	for(var i = 0; i < (currentMatrix.toVector().toArray().length * 10); i++) {
		var randIndex = getRandomInt(0, currentMatrix.toVector().toArray().length);
		var net = currentMatrix.toVector().multScalar(new Vector(W.column(randIndex)));
		switch(sign(net)) {
			case 1:
			outputVector.set(randIndex, 1);
			break;
			case -1:
			outputVector.set(randIndex, -1);
			break;
			case 0:
			break;
			default:
			break;
		}
	}

	var width = $('#inputTable tr:first-child td').length;
	var height = $('#inputTable tr').length;

	// Clear output table
	for(var i = 0; i < height; i++) {
		for(var j = 0; j < width; j++) {

			$('#inputTable tr:nth-child('+(i+1)+') td:nth-child('+(j+1)+')').css('background-color', '');
		}
	}

	var outputMatrix = outputVector.toMatrix(width, height);

	for(var i = 0; i < height; i++) {
		for(var j = 0; j < width; j++) {

			if(outputMatrix.get(i, j) > 0) {
				$('#outputTable tr:nth-child('+(i+1)+') td:nth-child('+(j+1)+')').css('backgroundColor', 'rgb(0, 0, 0)');
			}
		}
	}
}

function getRandomInt(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}