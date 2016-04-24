<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

fscanf(STDIN, "%d %d %d %d",
    $lightX, // the X position of the light of power
    $lightY, // the Y position of the light of power
    $initialTX, // Thor's starting X position
    $initialTY // Thor's starting Y position
);

// game loop
while (TRUE)
{
    fscanf(STDIN, "%d",
        $remainingTurns // The remaining amount of turns Thor can move. Do not remove this line.
    );
    $x = "";
    $y = "";
    if ($initialTY > $lightY) {
        $y = "N";
        $initialTY--;
    }
    elseif($initialTY < $lightY){
        $y = "S";
        $initialTY++;
    }
    if ($initialTX > $lightX){
        $x = "W";
        $initialTX--;
    }
    elseif($initialTX < $lightX){
        $x = "E";
        $initialTX++;
    }
    echo("$y$x\n");
}
?>