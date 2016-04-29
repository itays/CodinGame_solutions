var n = parseInt(readline()); // the number of temperatures to analyse
var temps = readline(); // the n temperatures expressed as integers ranging from -273 to 5526

var sortedTemps = temps.split(' ').sort((a, b) => {
    return Math.abs(a) - Math.abs(b) || b - a
})
var result = sortedTemps[0] || 0;
print(result)