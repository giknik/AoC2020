//
// AoC 2020 js solution for day 9
//   Part 2 eXchange-Masking Addition System:
//   Find the smallest and largest number from a contiguous
//   set that sums to the invalid number from part 1.
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
    			contiguousSet(enc_data[i]);
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

function contiguousSet (invalid) {
    let len = enc_data.length; 
    for (let i = 0; i < len; i++) {
        let curr_val = enc_data[i];
        for (let j = i + 1; j <= len; j++) {
            if (curr_val == invalid && j-i > 1) {
                let set = enc_data.slice(i, j);
                let res = Math.max(...set) + Math.min(...set);
                console.log(res);
                return;
            }
            if (curr_val > invalid || j == len) {
                break;
            }
            curr_val += enc_data[j];
        }
    }
    return;
}