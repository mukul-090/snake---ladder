/*module dice(input clk, output reg [2:0] dice);

initial dice = 1;

always @(posedge clk)
    //dice <= (dice % 6) + 1;
    dice <= ($urandom % 6 + 6) % 6 + 1;

endmodule*/
module dice(input clk, output reg [2:0] dice);

initial dice = 1;

always @(posedge clk)
    dice <= $urandom_range(1, 6); // cleanest way

endmodule