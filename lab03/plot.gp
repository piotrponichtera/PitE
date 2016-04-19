set term png
set output "altitude.png" 
plot "chart.gp" using 1:4 with lines

set output "velocity_kmh.png"
plot "chart.gp" using 1:3 with lines

set output "velocity_knots.png"
plot "chart.gp" using 1:2 with lines

set output "velocity_altitude.png"
plot "chart.gp" using 1:3 with lines, "chart.gp" using 1:4 with lines
