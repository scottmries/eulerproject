var fs = require('fs');

let data

fs.readFile('./data/p82.txt', 'utf8', function(err, fileData) {  
    console.log(this)
    if (err) throw err;
    data = fileData
    dataCallback()
});

let dataCallback = function() {
    let matrix = {}
    let rows = data.split("\n")
    rows.forEach(function(row, y) {
        let outerY = y
        row.split(',').forEach(function(column, x) {
            console.log(x, ", ", y, ": ", column)
            if(!matrix[x]) { matrix[x] = {}}
            matrix[x][outerY] = parseInt(column)
        })
    })
    rows.forEach(function(_, index) {
        findSumsFrom(0, index, null, 0, matrix)
    })
    console.log(leastSum)
}

let leastSum = null
let findSumsFrom = (x, y, prevY, prevSum, matrix) => {
    let sum = prevSum + matrix[x][y]
    if(x === 79) {
        testSum(sum)        
        return false
    }
    findSumsFrom(x + 1, y, y, sum, matrix)
    if(y < 79 && prevY !== y + 1) {
        findSumsFrom(x, y + 1, y, sum, matrix)
    }
    if(y > 0 && prevY !== y - 1) {
        findSumsFrom(x, y - 1, y, sum, matrix)
    }
}

function testSum(sum) {
    if(!leastSum || sum < leastSum) {
        leastSum = sum
    }
    console.log('least sum', leastSum, 'sum', sum)
}