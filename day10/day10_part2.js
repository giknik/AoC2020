//
// AoC 2020 js solution for day 9
//   Part 2 diffrent arrangements:
//   What is the total number of distinct ways you can arrange 
//   the adapters to connect the charging outlet to your device?
//

document.getElementById('file').onchange = function () {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = function() {
    	let adapters = this.result.split('\r\n').map(Number).sort((a, b)=>{return b - a});
        adapters.push(0);
        
        let hashTable = new Object();
        for (let adapter of adapters) {
            hashTable[adapter.toString()] = 0;
            for (let i = 1; i < 4; i++) {
                if (adapters.includes(adapter - i)) {
                    hashTable[adapter.toString()]++;
                }
            }
        }

        let arr = [];
        let tmp = [];
        for (let a in adapters) {
            if (hashTable[adapters[a].toString()] > 1 ) {
                tmp.push(hashTable[adapters[a].toString()]);
            } else {
                if (tmp.length > 0) {
                    tmp = tmp.reduce((a, b) => a + b);
                    if (tmp > 2) {
                        arr.push(tmp - 1);
                    } else {
                        arr.push(tmp)
                    }                    
                    tmp = [];
                }
            }
        }
        console.log(arr.reduce((a, b) => a*b));
    };
    reader.readAsText(file);
};