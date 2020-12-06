//
// AoC 2020 js solution for day 6
//   Part 1 check answers:
//   Count all the answers of each group
//   and print their sum.
//

document.getElementById('file').onchange = function () {
    var file = this.files[0];
    var reader = new FileReader();
    let arr = [];

    reader.onload = function() {
    	let doc = this.result.split('\n');
    	let answers = new Set();
    	for (group of doc) {
    		if (group.length > 1) {
    			var i = group.length;
	    		while (i--) {
	    		 	answers.add(group[i]);
	    		}
    		} else {
    			arr.push(answers.size - 1);
    			answers = new Set();
    		}
    	}
    	console.log(arr.reduce((a,b) => a + b, 0));    	        
    };

    reader.readAsText(file);
}