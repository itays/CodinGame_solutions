var inputs = readline().split(' ');
var LX = parseInt(inputs[0]); // the X position of the light of power
var LY = parseInt(inputs[1]); // the Y position of the light of power
var TX = parseInt(inputs[2]); // Thor's starting X position
var TY = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
    var remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.
    var x = "", y = "";
    if (TY > LY) {
        y = "N";
        TY--;
    }
    else if (TY < LY){
        y = "S";
        TY++;
    }
    
    if (TX > LX) {
        x = "W";
        TX--;
    }
    else if(TX < LX){
        x = "E";
        TX++;
    }
    
    print(y+""+x);
}