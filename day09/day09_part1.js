//
// AoC 2020 js solution for day 9
//   Part 1 eXchange-Masking Addition System:
//   Find the first number that
//   isn't valid.
//

let enc_data;
let preamble = 25;

document.getElementById('file').onchange = function () {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = function() {
    	enc_data = this.result.split('\r\n').map(numStr => parseInt(numStr));
    	for (let i = preamble; i < enc_data.length; i++ ) {
    		if (!checkNum(i)) {
    			console.log(enc_data[i]);
    			break;
    		}
    	}
    };
    reader.readAsText(file);
};

function checkNum (pos) {
	for (let j = pos - preamble; j < pos; j++) {
		for (let k = pos - preamble; k < pos; k++) {
			if (j != k && enc_data[j] + enc_data[k] == enc_data[pos]) {
				return true;
			}
		}
	}
	return false;
}