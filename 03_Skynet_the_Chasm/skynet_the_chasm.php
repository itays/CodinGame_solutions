<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%d",
    $road // the length of the road before the gap.
);
fscanf(STDIN, "%d",
    $gap // the length of the gap.
);
fscanf(STDIN, "%d",
    $platform // the length of the landing platform.
);

// game loop
while (TRUE)
{
    fscanf(STDIN, "%d",
        $speed // the motorbike's speed.
    );
    fscanf(STDIN, "%d",
        $coordX // the position on the road of the motorbike.
    );
    
    if ($coordX == $road - 1) {
        echo("JUMP\n");
    }
    elseif ($coordX > $road - 1){
        echo("SLOW\n");
    }
    elseif ($speed == $gap + 1){
        echo("WAIT\n");
    }
    elseif ($speed > $gap + 1){
        echo("SLOW\n");
    }
    else {
        echo("SPEED\n");
    }
     
}
?>