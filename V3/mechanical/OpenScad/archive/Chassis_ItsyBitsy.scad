$fn = 32;  // smooth circles

board = "RP2040";
version = "V0.0";

baseThickness = 2.4;
cornerRounding = 8;
railOffset = 12;     // from CL
M3holeDia = 3.5;
M3nutDia = 6.5;
holeOffset = M3holeDia * 1.2;

chassis_wid = 72;  // x   was 82
chassis_len = 112; // y  was 142
plateOffsetY = 8;  // giving up on symetry

casterOffset = 9;  // from edge

standoffDia = 7;
standoffThickness = 4.8;
standoffHoleDia = 2.5;
holderOffsetX = 10; 
holderOffsetY = 0;

backBatteryOffset = 31;
frontBatteryOffset = 31;
//frontBatteryOffset = backBatteryOffset + plateOffsetY - 2;
//batteryOffset = 15 + 10;  // from CL

xArduinoOffset = 17;
yArduinoOffset = -chassis_len / 2 + standoffDia / 2;

penHoleDiameter = 12.0;
penHoleRadius = penHoleDiameter / 2;

railWidth = 4;
cutout_len = 45;
cutout_wid = 15;

stepperBoardX = 26.5; // distance between mounting holes CL
stepperBoardY = 29.5;

itsyX = 36.5;
itsyY = 18.5; 
itsyOffsetY = 36;  //from CL
itsyOffsetX = -10;


difference(){
    union(){ // solids
        // chassis plate
        translate([0, plateOffsetY, 0])
        roundedCube([chassis_wid, chassis_len, baseThickness], center=true, radius=8);
            
        //itsy bitsy holder
        //translate([-itsyOffsetX, -itsyOffsetY, 0])
        //roundedCube([itsyX + 4, itsyY + 4, 6], center=true, radius=1);  

        // arduino standoffs
        //translate([xArduinoOffset, yArduinoOffset, 0]) Arduino(standoffDia);
        
        // RP2040 standoffs
         translate([0, -chassis_len/2+plateOffsetY+17, 0]) RP2040(standoffDia);
        
        
        // rails
        /*
        translate([railOffset, chassis_len / 2 - (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 + plateOffsetY, 4, 1);

        translate([-railOffset, chassis_len / 2 - (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 + plateOffsetY, 4, 1);

        translate([railOffset, -chassis_len / 2 + (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2 , 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 - plateOffsetY, 4, 1);

        translate([-railOffset, -chassis_len / 2 + (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 - plateOffsetY, 4, 1);
        */    

        // stepper board standoffs
        translate([-17, chassis_len / 2 - stepperBoardY / 2 - standoffDia + plateOffsetY, 0]) stepperBoard(standoffDia);
        translate([17, chassis_len / 2 - stepperBoardY / 2 - standoffDia + plateOffsetY, 0]) stepperBoard(standoffDia);

        // caster standoffs
        translate([0, chassis_len / 2 - casterOffset  + plateOffsetY, 0])
        caster(standoffDia + 1);
        
        // battery standoffs
        translate([0, -backBatteryOffset, 0])
        battery(standoffDia + 1);
        translate([0, frontBatteryOffset, 0])
        battery(standoffDia + 1);
    }


    union() { // holes
        // Arduino mount holes
        //translate([xArduinoOffset, yArduinoOffset, 0]) Arduino(standoffHoleDia);  

        // RP2040 standoffs
         translate([0, -chassis_len/2+plateOffsetY+17, 0]) RP2040(standoffHoleDia);
        
        // stepperBoard
        translate([-17, chassis_len / 2 - stepperBoardY / 2 - standoffDia + plateOffsetY, 0]) stepperBoard(standoffHoleDia);
        translate([17, chassis_len / 2 - stepperBoardY / 2 - standoffDia + plateOffsetY, 0]) stepperBoard(standoffHoleDia);   
           
        // center pen hole
        cylinder(baseThickness, penHoleRadius, penHoleRadius); 
     
        // pen holder 
        translate([-holderOffsetX, -holderOffsetY, 0])
        cylinder(baseThickness, d=M3holeDia);     // lower left
        translate([holderOffsetX, holderOffsetY, 0])
        cylinder(baseThickness, d=M3holeDia);      // upper right
        
        // stepper bracket holes
        bracketOffset = 9.5;
        translate([-chassis_wid / 2 + bracketOffset, 0, 0])
        stepperBracketHoles(M3holeDia);
        translate([chassis_wid / 2 - bracketOffset, 0, 0])
        stepperBracketHoles(M3holeDia);
               
        // wire cutouts
        CL = chassis_wid / 2;
        cutoutOffsetX = 5;  // from edge
        cutoutOffsetY = 20; // from CL
        cutoutX = M3holeDia;
        cutoutY = M3holeDia * 2;
        cutoutZ = 10;

        translate([CL - cutoutOffsetX, cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 

        translate([CL - cutoutOffsetX, -cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 
        
        translate([-CL + cutoutOffsetX, cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 

        translate([-CL + cutoutOffsetX, -cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 

        /*
        translate([chassis_wid / 2 - battertyCuttoutOffset - M3holeDia, -backBatteryOffset, 0])
        cube([M3holeDia, M3holeDia * 2, baseThickness, ]); 
        translate([-chassis_wid / 2 + battertyCuttoutOffset, backBatteryOffset - M3holeDia * 2, 0])
        cube([M3holeDia, M3holeDia * 2, baseThickness, ]); 
        translate([chassis_wid / 2 - battertyCuttoutOffset - M3holeDia, backBatteryOffset - M3holeDia * 2, 0])
        cube([M3holeDia, M3holeDia * 2, baseThickness, ]); 
        */

        //translate([railOffset - railWidth * 1.5, 0, 0])
        
        //cube([M3holeDia, M3holeDia * 2, baseThickness, ]); 
        
        // caster mount holse
        translate([0, chassis_len / 2 - casterOffset + plateOffsetY, 0])
        caster(M3holeDia);
        
        // caster nuts    
        translate([0, chassis_len / 2 - casterOffset + plateOffsetY, baseThickness - 1])
        caster(M3nutDia, sides=6); 
        
        // battery holes
        translate([0, -backBatteryOffset, 0])
        battery(M3holeDia);
        translate([0, frontBatteryOffset, 0])
        battery(M3holeDia);
        
        // battery nuts
        translate([0, -backBatteryOffset, baseThickness - 1])
        battery(M3nutDia, sides=6);
        translate([0, frontBatteryOffset, baseThickness - 1])
        battery(M3nutDia, sides=6);

        /*
        //itsy bitsyv cutouts
        translate([-itsyOffsetX, -itsyOffsetY, 4]){
            roundedCube([itsyX, itsyY, 10], radius=1, center=true);
            roundedCube([itsyX + 8, itsyY - 8, 6], radius=1, center=true);  // usb cutout
        }
        translate([-itsyOffsetX, -itsyOffsetY, 3])
        roundedCube([itsyX - 4, itsyY - 4, 10], radius=1, center=true);
        */
        
        //version cutout
        rotate([0, 180, 0])
        translate([-chassis_wid/2+5, 1, -0.3])
        linear_extrude(10)
        text(board, size = 4, font="Arial:style=Bold");
        rotate([0, 180, 0])
        translate([-chassis_wid/2+5, -5, -0.3])
        linear_extrude(10)
        text(version, size = 4, font="Arial:style=Bold");
    }
}



module battery(dia, sides=64, z=0){
    color("red"){
        if (sides==6){ // extend cut upward
            translate([0, 7.5, z])
            cylinder(10, d=dia, $fn=sides);  
            translate([0, -7.5, z])
            cylinder(10, d=dia, $fn=sides);
        }
        else {
            translate([0, 7.5, z])
            cylinder(standoffThickness - 1, d=dia, $fn=sides);  
            translate([0, -7.5, z])
            cylinder(standoffThickness - 1, d=dia, $fn=sides);    
        }
    }
}


module caster(dia, sides=64){
    color("darkblue"){
        translate([-15, 0, 0])
        cylinder(standoffThickness - 1, d=dia, $fn=sides);     
        translate([15, 0, 0])
        cylinder(standoffThickness - 1, d=dia, $fn=sides); 
    }
}


module stepperBoard(dia){ // centered symetrically
    translate([-stepperBoardX/2, -stepperBoardX/2, 0])
    color("blue"){ // lower left (0,0 reference)
        cylinder(standoffThickness, dia / 2, dia / 2);    
        translate([0, stepperBoardY, 0])                // upper left
        cylinder(standoffThickness, dia / 2, dia / 2);
        translate([stepperBoardX, stepperBoardY, 0])    // upper right
        cylinder(standoffThickness, dia / 2, dia / 2);
        translate([stepperBoardX, 0, 0])                // lower right
        cylinder(standoffThickness, dia / 2, dia / 2);
    }
}


module stepperBracketHoles(dia){
    translate([0, 11.8, 0])cylinder(baseThickness, d=dia); 
    translate([0, -11.8, 0])cylinder(baseThickness, d=dia); 
}


module Arduino(dia){
    color("lightblue"){
        // lower right USB (0,0 reference)
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([-50.8, 15.2, 0])         // lower left
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([-50.8, 43.1, 0])         // upper left
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([1.3, 48.2, 0])         // upper right
        cylinder(standoffThickness, dia / 2, dia / 2);
    }
}



module RP2040(dia){
    color("lightblue"){
        // symetrical, from CL
        RPwidth = 47.0;
        RPheight = 11.4;

        translate([-RPwidth/2, -RPheight/2, 0])    
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([-RPwidth/2, RPheight/2, 0])          
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([RPwidth/2, RPheight/2, 0])         
        cylinder(standoffThickness, dia / 2, dia / 2);

        translate([RPwidth/2, -RPheight/2, 0])      
        cylinder(standoffThickness, dia / 2, dia / 2);
    }
}



module roundedCube(dims, radius=2, center=false){
    // attempt at replicated cube, but with rounded edges from
    // https://youtu.be/gKOkJWiTgAY
    xdim =dims[0];
    ydim =dims[1];
    zdim =dims[2];
    
    if (center) {
        translate([-xdim/2, -ydim/2, 0]){
            hull(){ 
                translate([radius, radius, 0]) cylinder(zdim, radius, radius);
                translate([xdim-radius, radius, 0]) cylinder(zdim, radius, radius);
                translate([radius, ydim-radius, 0]) cylinder(zdim, radius, radius);
                translate([xdim-radius, ydim-radius, 0]) cylinder(zdim, radius, radius);
            }
        }
    }
    else{
        hull(){ // https://youtu.be/gKOkJWiTgAY
            translate([radius, radius, 0]) cylinder(zdim, radius, radius);
            translate([xdim-radius, radius, 0]) cylinder(zdim, radius, radius);
            translate([radius, ydim-radius, 0]) cylinder(zdim, radius, radius);
            translate([xdim-radius, ydim-radius, 0]) cylinder(zdim, radius, radius);
        }
    }
}
