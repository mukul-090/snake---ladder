@echo off
cd /d "E:\VScode files\Verilog\Snake_&_ladder"

echo Running simulation...
vsim -c -do run.do

echo Opening waveform viewer...
start vsim -view vsim.wlf -do view_wave.do
timeout /t 10 >nul

echo Launching game...
"C:\msys64\ucrt64\bin\python.exe" "snake_ladder_play.py"

pause