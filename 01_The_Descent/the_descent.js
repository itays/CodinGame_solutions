// game loop
while (true) {
    var mountainIndex = 0;
    var highestMountain = 0;
    for (var i = 0; i < 8; i++) {
        var mountainH = parseInt(readline()); // represents the height of one mountain, from 9 to 0.
        if (mountainH > highestMountain) {
            highestMountain = mountainH;
            mountainIndex = i;
        }
    }

    print(mountainIndex);
}