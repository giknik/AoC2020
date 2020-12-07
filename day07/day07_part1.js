//
// AoC 2020 js solution for day 7
//   Part 1 issues in luggage processing:
//   Find all the bags, that can 
//   contain your gold shiny bag
//

document.getElementById('file').onchange = function () {
    var file = this.files[0];
    var reader = new FileReader();
    reader.onload = function() {
    	let doc = this.result.split('\n');
    	let bags = new Object();
    	checkRules("shiny gold", doc, bags);
    	console.log(Object.keys(bags).length);    	    	        
    };
    reader.readAsText(file);
};

function checkRules (bagname, doc, bags) {
	for (bag of doc) {
		let splited = bag.match(/\b[\w']+(?:[^\w\n]+[\w']+){0,2}\b/g);
		let first = splited[0].slice(0, -5);
		let last_part = "";
		for (let i = 1; i < splited.length; i++) {
			last_part += splited[i] + " ";
		}
		last_part = last_part.match(/\b[\w']+(?:[^\w\n]+[\w']+){0,1}\b/g);
		for (let i = 1; i < last_part.length; i++) {
			if (last_part[i] === bagname && !bags.hasOwnProperty(first)) {
				bags[first] = 0;
				checkRules(first, doc, bags);
				break;
			} else if (bags.hasOwnProperty(last_part[i])) {
				break;
			}
		}
	}
}