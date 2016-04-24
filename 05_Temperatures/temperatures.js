/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var n = parseInt(readline()); // the number of temperatures to analyse
var temps = readline(); // the n temperatures expressed as integers ranging from -273 to 5526


// Write an action using print()
// To debug: printErr('Debug messages...');

function findTemp(n, temps){
    if (!n) {
        return 0;
    }
    temps = temps.split(" ")
    temps.sort(function(a, b){
        return Math.abs(a) > Math.abs(b) ? 1 : -1;
    });
    
    if (temps[0] < 0) {
        var pos = Math.abs(temps[0]);
        var index = temps.indexOf(String(pos));
        return (index === -1) ? temps[0] : temps[index];
    }
    
    return temps[0];
}

print(findTemp(n, temps));