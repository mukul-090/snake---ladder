vlog dice.v game.v tb.v
vsim -sv_seed random work.tb
add wave *
run -all