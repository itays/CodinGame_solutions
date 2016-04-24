<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/


// game loop
while (TRUE)
{
    $mountainIndex = 0;
    $highestMountain = 0;
    
    for ($i = 0; $i < 8; $i++)
    {
        fscanf(STDIN, "%d",
            $mountainH // represents the height of one mountain, from 9 to 0.
        );
        if ($mountainH > $highestMountain) {
            $highestMountain = $mountainH;
            $mountainIndex = $i;
        }
    }

    // Write an action using echo(). DON'T FORGET THE TRAILING \n
    // To debug (equivalent to var_dump): error_log(var_export($var, true));

    echo($mountainIndex."\n"); // The number of the mountain to fire on.
}
?>