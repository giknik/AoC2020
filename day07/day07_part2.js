//
// AoC 2020 js solution for day 7
//   Part 2 pretty expensive to fly:
//   How many individual bags are 
//   required inside your single shiny gold bag?
//

document.getElementById('file').onchange = function () {
    var file = this.files[0];
    var reader = new FileReader();
    reader.onload = function() {
    	let doc = this.result.split('\n');
    	console.log(countBag("shiny gold", doc));    	    	        
    };
    reader.readAsText(file);
};

function countBag (bagname, doc) {
	let notfound = true;
	for (bag of doc) {
		let bagNum = new Object();
		let splited = bag.match(/\b[\w']+(?:[^\w\n]+[\w']+){0,2}\b/g);
		let first = splited[0].slice(0, -5);
		let x = 0;
		if (first === bagname) {
			notfound = false;
			console.log(bag);
			let last_part = "";
			for (let i = 1; i < splited.length; i++) {
				last_part += splited[i] + " ";
			}
			last_part = last_part.match(/\b[\w']+(?:[^\w\n]+[\w']+){0,1}\b/g);
			for (let i = 0; i < last_part.length - 1; i+=2) {
				if (last_part[i+1] == "other bags") {
					bagNum["other"] = 0;
					break;
				}
				bagNum[last_part[i+1]] = parseInt(last_part[i].slice(-1))
			}

		    for (let it in bagNum) {
			    if (bagNum.hasOwnProperty(it)) {
			        x += bagNum[it] + (bagNum[it] * countBag(it, doc));
			    }
		    }
			return x;
		}
	}
	if (notfound) {
		return 0;
	}
}