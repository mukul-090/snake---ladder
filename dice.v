module dice(input clk, output reg [2:0] dice);

initial dice = 1;

always @(posedge clk)
    dice <= $urandom_range(1, 6); // cleanest way

endmodule