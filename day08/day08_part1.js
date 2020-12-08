//
// AoC 2020 js solution for day 8
//   Part 1 infinite loop:
//   Find the infinite loop
//   and print the value of accumulator
//

document.getElementById('file').onchange = function () {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = async function() {
    	operations = this.result.split('\r\n');
    	let accumulator = 0;
    	let operation_pointer = 0;
    	let val = 0;

    	while ( operation_pointer < operations.length) {
    		if (operations[operation_pointer][0] == "a") {
    			accumulator += parseInt(operations[operation_pointer].split(' ')[1]);
    			operations[operation_pointer] = "." + operations[operation_pointer];
    			operation_pointer++;
    		} else if (operations[operation_pointer][0] == "j") {
    			val = parseInt(operations[operation_pointer].split(' ')[1]);
    			operations[operation_pointer] = "." + operations[operation_pointer];
    			operation_pointer += val;
    		} else if (operations[operation_pointer][0] == "n") {
    			operations[operation_pointer] = "." + operations[operation_pointer];
    			operation_pointer++;
    		} else {
    			break;
    		}
    	}

    	console.log(accumulator);
    };
    reader.readAsText(file);
};