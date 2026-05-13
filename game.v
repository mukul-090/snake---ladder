module game(input clk, input [2:0] dice,
            output reg [6:0] p1, p2,
            output reg turn,
            output reg win);

initial begin
    p1 = 0;
    p2 = 0;
    turn = 0;
    win = 0;
end

reg [6:0] next_pos;

always @(posedge clk) begin
    if (!win) begin

        if (turn == 0) begin
            // -------- PLAYER 1 --------
            next_pos = p1 + dice;

            if (next_pos <= 100) begin

                // Ladders
                if (next_pos == 4)  next_pos = 25;
                if (next_pos == 13) next_pos = 46;
                if (next_pos == 35) next_pos = 70;
                if (next_pos == 69) next_pos = 80;


                // Snakes
                if (next_pos == 27) next_pos = 5;
                if (next_pos == 40) next_pos = 3;
                if(next_pos == 86) next_pos = 20;


                p1 <= next_pos;

                if (next_pos >= 100)
                    win <= 1;
            end

            turn <= 1;  // switch turn

        end else begin
            // -------- PLAYER 2 --------
            next_pos = p2 + dice;

            if (next_pos <= 100) begin

                // Ladders
                if (next_pos == 4)  next_pos = 25;
                if (next_pos == 13) next_pos = 46;
                if (next_pos == 35) next_pos = 70;
                if (next_pos == 69) next_pos = 80;

                // Snakes
                if (next_pos == 27) next_pos = 5;
                if (next_pos == 40) next_pos = 3;
                if(next_pos == 86) next_pos = 20;

                p2 <= next_pos;

                if (next_pos >= 100)
                    win <= 1;
            end

            turn <= 0;  // switch turn
        end

    end
end

endmodule