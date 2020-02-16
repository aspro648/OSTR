;Generated with Cura_SteamEngine 15.01
;START G CODE
G21 ; set units to millimeters
M107
M355 S1 C3 ; turn led blue
M104 S230 ; set temperature
G28 X0 Y0 Z0
G29
M109 S230 ; wait for temperature to be reached

M355 S1 C0 ; LED white

; -- Ken stuff
;G1 X142.5 Y10 Z0; move to corner
;G92 E0 ;zero the extruded length
;G1 E10 F120; extrude 5mm
;G1 E9; small retract, as default for layer change
G92 E0 ;zero the extruded length

;G0 F4200 X80.000 Y20.00

; -- End Ken stuff
;Layer count: 1
;LAYER:0
M107
G0 F9000 X1.780 Y1.780 Z0.300
;TYPE:SKIRT
G1 F1440 X148.220 Y1.780 E7.23286
G1 X148.220 Y148.220 E14.46572
G1 X1.780 Y148.220 E21.69859
G1 X1.780 Y1.780 E28.93145
G1 F2400 E25.43145
G1 Z0.403
G0 F9000 X5.220 Y5.220
;TYPE:WALL-OUTER
G1 Z0.300
G1 F2400 E28.93145
G1 F1440 X144.780 Y5.220 E35.82450
G1 X144.780 Y144.780 E42.71755
G1 X5.220 Y144.780 E49.61060
G1 X5.220 Y5.220 E56.50365
G0 F9000 X5.277 Y5.277
G1 F1440 X5.277 Y144.722 E63.39102
G1 X144.722 Y144.722 E70.27839
G1 X144.722 Y5.277 E77.16576
G1 X5.277 Y5.277 E84.05313
G1 F2400 E80.55313
G1 Z0.403
G0 F9000 X5.277 Y5.277 Z5.300
;END G CODE
; Default end code
;G1 X0 Y0 Z130 ; Get extruder out of way.
M104 T0 S200
G28 X0 Y0 Uncomment to use!
M107 ; Turn off fan
M355 S0; Turn off LED
; Disable all extruder
G91 ; Relative positioning
T0
G1 E-1 ; Reduce filament pressure
M104 T0 S0
G90 ; Absolute positioning
G92 E0 ; Reset extruder position
M140 S0 ; Disable heated bed
M84 ; Turn steppers off

