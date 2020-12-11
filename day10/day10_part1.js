//
// AoC 2020 js solution for day 9
//   Part 1 use every adapter in your bag:
//   Find the number of 1-jolt differences multiplied 
//   by the number of 3-jolt differences
//

document.getElementById('file').onchange = function () {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = function() {
    	let adapters = this.result.split('\r\n').map(Number).sort((a, b)=>{return a - b});

        let prev = 0;
        let arr = [0, 0, 0];
        for (let adapter of adapters) {
            arr[adapter-prev-1] += 1;
            prev = adapter;
        }
        console.log(arr[0]*(++arr[2]));
    };
    reader.readAsText(file);
};