//
// AoC 2020 js solution for day 6
//   Part 2 check answers:
//   Count the answers on which every
//   member answered yes of each group
//   and print their sum.
//

document.getElementById('file').onchange = function () {
    var file = this.files[0];
    var reader = new FileReader();
    let arr = [];

    reader.onload = function() {
    	let doc = this.result.split('\n');
    	let answers = new Set();
        var c = 0;
    	for (group of doc) {
            let person = new Set();
    		if (group.length > 1) {
    			var i = group.length;
	    		while (i--) {
	    		 	person.add(group[i]);
                    if (c == 0) {
                        answers = person;
                    }
	    		}
                c++;
                answers = intersection(answers, person);
    		} else {
                c = 0;
    			arr.push(answers.size - 1);
    			answers = new Set();
    		}
    	}
    	console.log(arr.reduce((a,b) => a + b, 0));    	        
    };

    reader.readAsText(file);
}

function intersection(setA, setB) {
    let _intersection = new Set()
    for (let elem of setB) {
        if (setA.has(elem)) {
            _intersection.add(elem)
        }
    }
    return _intersection
}