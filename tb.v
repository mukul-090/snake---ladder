module tb;

reg clk;
wire [2:0] dice;
wire [6:0] p1, p2;
wire turn, win;

dice d(clk, dice);
game g(clk, dice, p1, p2, turn, win);

/*Dice Generator
integer seed;

initial begin
    seed = $random;
    $display("Seed = %0d", seed);
    $urandom(seed);
end*/

// Clock
initial begin
    clk = 0;
    forever #20 clk = ~clk;
end

// GAME LOG (VERY IMPORTANT)
initial begin
    $display("---- Snake & Ladder Game Start ----");

    $monitor("Time=%0t | Turn=%0d | Dice=%0d | P1=%0d | P2=%0d | Win=%0d",
              $time, turn, dice, p1, p2, win);
end

// Game Log to File
integer file;

initial begin
    file = $fopen("output.txt", "w");
end

always @(posedge clk) begin
    #1;
    $fwrite(file, "%0t %0d %0d %0d %0d %0d\n",
            $time -1, turn, dice, p1, p2, win);
end

//Snakes and Ladders board
integer f;
initial begin
    
    f = $fopen("board.txt", "w");

    // Ladders
    $fwrite(f, "L 4 25\n");
    $fwrite(f, "L 35 46\n");
    $fwrite(f, "L 69 80\n");

    // Snakes
    $fwrite(f, "S 27 5\n");
    $fwrite(f, "S 40 3\n");
    $fwrite(f, "S 86 20\n");

    $fclose(f);
end


always @(posedge clk) begin
    if (win) begin
        $display("Game Over!");
        $display("Game Log saved to file");
        $fclose(file);
        $finish;
    end
end


endmodule