//
// AoC 2020 js solution for day 8
//   Part 2 infinite loop:
//   Find the infinite loop
//   and print the value of accumulator
//

document.getElementById('file').onchange = function () {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = function() {
    	let loop_op = this.result.split('\r\n');
    	let operations = this.result.split('\r\n');
    	let operation_pointer = 0;
    	let accumulator = 0;    	

    	let last_operation = "";
    	let last_pointer = 0;
    	let terminated = true;

    	for (let x = 0; x < loop_op.length; x++) {
    		if (loop_op[x].split(" ")[0] == "jmp" || loop_op[x].split(" ")[0] == "nop") {
    			let new_operation = (loop_op[x].split(" ")[0] == "jmp") ? "nop 7" : "jmp " + loop_op[x].split(" ")[1];
    			operations[x] = new_operation;
		    	while ( operation_pointer < operations.length) {
		    		if (operations[operation_pointer][0] == "a") {
		    			accumulator += parseInt(operations[operation_pointer].split(' ')[1]);
		    			operations[operation_pointer] = "." + operations[operation_pointer];
		    			operation_pointer++;
		    		} else if (operations[operation_pointer][0] == "j") {
		    			let val = parseInt(operations[operation_pointer].split(' ')[1]);
		    			operations[operation_pointer] = "." + operations[operation_pointer];
		    			operation_pointer += val;
		    		} else if (operations[operation_pointer][0] == "n") {
		    			operations[operation_pointer] = "." + operations[operation_pointer];
		    			operation_pointer++;
		    		} else {
		    			accumulator = 0;
		    			operation_pointer = 0
		    			terminated = false;
		    			break;
		    		}
		    	}
		    	if (terminated) {
		    		break;
		    	}
    		}
    		terminated = true;
    		operations = this.result.split('\r\n');
    	}
    	console.log(accumulator);
    };
    reader.readAsText(file);
};