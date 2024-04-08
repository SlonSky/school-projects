

function sign(val) {
	var res = 0;
	if(val < 0) {
		res = -1;
	} else if (val > 0) {
		res = 1;
	}
	return res;
}

function Matrix(array, width, height) {

	var _matrix;
	if(array !== undefined) {
		_matrix = array;
	} else {
		_matrix = [];
		for(var i = 0; i < height; i++) {
			var row = [];
			for(var j = 0; j < width; j++) {
				row[j] = 0;
			}
			_matrix[i] = row;
		}
	}


	this.add = function(mat) {
		var res = new Matrix(undefined, mat.length(), mat.height());

		for(var i = 0; i < this.height(); i++) {
			for(var j = 0; j <  this.length(); j++) {
				res.set(i, j, (_matrix[i][j] + mat.get(i,j)));
			}
		}
		return res;
	};

	this.column = function(n) {
		var res = [];
		for(var i = 0; i < this.height(); i++) {
			res[i] = _matrix[i][n];
		}
		return res;
	};

	this.transposed = function() {
		var res = [];
		for(var i = 0; i < this.length(); i++) {
			res[i] = this.column(i);
			
		}
		return new Matrix(res);
	};

	this.set = function(i, j, val) {
		_matrix[i][j] = val;
	};

	this.get = function(i, j) {
		return _matrix[i][j];
	};

	this.toVector = function() {
		var res = [];
		var n = 0;
		for(var i = 0; i < this.length(); i++) {
			for(var j = 0; j < this.height(); j++, n++) {
				res[n] = _matrix[j][i];
			}
		}
		return new Vector(res);
	};

	this.height = function() {
		return _matrix.length;

	};

	this.length = function() {
		return _matrix[0].length;
	};
}

function Vector(array, length) {
	var _vector;
	{
		if(length === undefined) {
			_vector = array;
		} else {
			_vector = [];
			for (var i = 0; i < length; i++) {
				_vector[i] = 0;
			}
		}	
	}

	this.set = function(i, val) {
		_vector[i] = val;
	};

	this.get = function(i) {
		return _vector[i];
	};

	this.mult = function(vec) {
		var res = new Matrix(undefined, _vector.length, vec.length());
		for (var i = 0; i < _vector.length; i++) {
			for (var j = 0; j < vec.length(); j++) {
				res.set(j, i, (_vector[i] * vec.get(j)));
			}
		}
		return res;
	};

	this.multScalar = function(vec) {
		var res = 0;
		for (var i = 0; i < _vector.length; i++) {
			res += _vector[i] * vec.get(i);
		}
		return res;
	};
	
	this.toMatrix = function(width, height) {
		var res = new Matrix(undefined, width, height);
		var n = 0;
		for(var i = 0; i < width; i++) {
			for(var j = 0; j < height; j++, n++) {
				res.set(j,i, _vector[n]);
			}
		}
		return res;
	};

	this.toArray = function() {
		return _vector;
	};

	this.length = function() {
		return _vector.length;
	}
	
}

function showMat(matrix) {
	for (var i = 0; i < matrix.height(); i++) {
		var row = '';
		for(var j = 0; j < matrix.length(); j++) {
			row += matrix.get(i,j) + ' ';
		}
		console.log(row);
	}
}
