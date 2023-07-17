// OpenScad version 2021.01 

$fn = 32;  // smooth circles

board = "BBoard";
version = "V0.5";

baseThickness = 2.4;
railOffset = 12;     // from CL
M3holeDia = 3.7;
M3nutDia = 6.4;
holeOffset = M3holeDia * 1.2;

chassis_wid = 92;  // x   was 82
chassis_len = 114; // y  was 142
plateOffsetY = 0;  // giving up on symetry

casterOffset = 6;  // from edge

standoffDia = 7;
smallStandoffDia = 5;
standoffHeight = baseThickness + 1.5;
insertHeight = baseThickness + 1;
standoffHoleDia = 2.3; //2-28 thread forming 
holderOffsetX = 10; 
holderOffsetY = 6;

batteryOffsetY = 25;  //from CL
frontBatteryOffset = 25;
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
stepperBoardXoffset = chassis_wid / 2 - stepperBoardX/2 -6; // from edge
stepperBoardYoffset = chassis_len / 2 - stepperBoardY / 2 - standoffDia + plateOffsetY+3;

itsyX = 36.5;
itsyY = 18.5; 
itsyOffsetY = 36;  //from CL
itsyOffsetX = -10;

breadBoardWidth = 82;


difference(){
    union(){ // solids
        // chassis plate
        translate([0, plateOffsetY, baseThickness/2])
        roundedCube([chassis_wid, chassis_len, baseThickness], center=true, radius=4);
            
        //itsy bitsy holder
        //translate([-itsyOffsetX, -itsyOffsetY, 0])
        //roundedCube([itsyX + 4, itsyY + 4, 6], center=true, radius=1);  

        // arduino standoffs
        //translate([xArduinoOffset, yArduinoOffset, 0]) Arduino(standoffDia);
        
        // RP2040 standoffs
         //translate([0, -chassis_len/2+plateOffsetY+9, 0]) RP2040(standoffDia);
        
        // breaboard support plates
        translate([0, -38, standoffHeight/2])
        #cube([breadBoardWidth, 38, standoffHeight], center=true);
               
        // rails
        /*
        translate([railOffset, chassis_len / 2 - (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 + plateOffsetY, 4, 1);

        translate([-railOffset, chassis_len / 2 - (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 + plateOffsetY, 4, 1);

        translate([railOffset, -chassis_len / 2 + (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2 , 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 - plateOffsetY, 4, 1);

        translate([-railOffset, -chassis_len / 2 + (chassis_len / 2 - 15.75)/2 + plateOffsetY / 2, 0]) roundedCube(railWidth, chassis_len / 2 - 15.75 - plateOffsetY, 4, 1);
        */    

        // stepper board standoffs
        translate([-stepperBoardXoffset, stepperBoardYoffset, 0]) stepperBoard(smallStandoffDia);
        translate([stepperBoardXoffset, stepperBoardYoffset, 0]) stepperBoard(smallStandoffDia);

        // caster standoffs
        translate([0, -(chassis_len / 2 - casterOffset  + plateOffsetY), 0])
        caster(standoffDia + 1);
        
        // battery standoffs
        translate([0, -batteryOffsetY, 0])
        battery(standoffDia + 1);
        translate([0, batteryOffsetY, 0])
        battery(standoffDia + 1);
    }


    union() { // holes
        // Arduino mount holes
        //translate([xArduinoOffset, yArduinoOffset, 0]) Arduino(standoffHoleDia);  

        // RP2040 standoffs
         //translate([0, -chassis_len/2+plateOffsetY+9, 0]) RP2040(standoffHoleDia);
        
        // stepperBoard
        translate([-stepperBoardXoffset, stepperBoardYoffset, 0]) stepperBoard(standoffHoleDia);
        translate([stepperBoardXoffset, stepperBoardYoffset, 0]) stepperBoard(standoffHoleDia);   
           
        // center pen hole
        cylinder(baseThickness, penHoleRadius, penHoleRadius); 
     
        // pen holder 
        translate([-holderOffsetX, -holderOffsetY, 0])
        cylinder(baseThickness, d=M3holeDia);     // lower left
        translate([holderOffsetX, holderOffsetY, 0])
        cylinder(baseThickness, d=M3holeDia);      // upper right
        
        // stepper bracket holes
        bracketOffset = 10;
        translate([-chassis_wid / 2 + bracketOffset, 0, 0])
        stepperBracketHoles(M3holeDia);
        translate([chassis_wid / 2 - bracketOffset, 0, 0])
        stepperBracketHoles(M3holeDia);
               
        // wire cutouts

        cutoutOffsetX = 58 / 2;         // from CL
        cutoutOffsetY = batteryOffsetY - 10; // from CL
        cutoutX = 4;
        cutoutY = 8;
        cutoutZ = 5;

        translate([-cutoutOffsetX, cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 

        translate([-cutoutOffsetX, -cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 
        
        translate([cutoutOffsetX, cutoutOffsetY, 0])
        cube([cutoutX, cutoutY, cutoutZ], center=true); 

        translate([cutoutOffsetX, -cutoutOffsetY, 0])
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
        translate([0, -(chassis_len / 2 - casterOffset + plateOffsetY), 0])
        caster(M3holeDia);
        
        // caster nuts    
        translate([0, -(chassis_len / 2 - casterOffset + plateOffsetY), baseThickness - 1])
        caster(M3nutDia, sides=6); 
        
        // battery holes
        translate([0, -batteryOffsetY, 0])
        battery(M3holeDia);
        translate([0, batteryOffsetY, 0])
        battery(M3holeDia);
        
        // battery nuts
        translate([0, -batteryOffsetY, baseThickness - 1])
        battery(M3nutDia, sides=6);
        translate([0, batteryOffsetY, baseThickness - 1])
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
        translate([-chassis_wid/2+3, 2, -0.3])
        linear_extrude(10)
        text(board, size = 5, font="Arial:style=Bold");
        rotate([0, 180, 0])
        translate([-chassis_wid/2+3, -6, -0.3])
        linear_extrude(10)
        text(version, size = 5, font="Arial:style=Bold");
    }
}



module battery(dia, sides=64, z=0){
    color("red"){
        if (sides==6){ // extend cut upward
            rotate([0, 0, 0])
            translate([0, 7.5, z])
            rotate([0, 0, 30])
            cylinder(10, d=dia, $fn=sides);  
            translate([0, -7.5, z])
            rotate([0, 0, 30])
            cylinder(10, d=dia, $fn=sides);
        }
        else {
            translate([0, 7.5, z])
            cylinder(insertHeight, d=dia, $fn=sides);  
            translate([0, -7.5, z])
            cylinder(insertHeight, d=dia, $fn=sides);    
        }
    }
}


module caster(dia, sides=64){
    color("darkblue"){
        translate([-15, 0, 0])
        cylinder(insertHeight, d=dia, $fn=sides);     
        translate([15, 0, 0])
        cylinder(insertHeight, d=dia, $fn=sides); 
    }
}


module stepperBoard(dia){ // centered symetrically
    translate([-stepperBoardX/2, -stepperBoardX/2, 0])
    color("blue"){ // lower left (0,0 reference)
        cylinder(standoffHeight, dia / 2, dia / 2);    
        translate([0, stepperBoardY, 0])                // upper left
        cylinder(standoffHeight, dia / 2, dia / 2);
        translate([stepperBoardX, stepperBoardY, 0])    // upper right
        cylinder(standoffHeight, dia / 2, dia / 2);
        translate([stepperBoardX, 0, 0])                // lower right
        cylinder(standoffHeight, dia / 2, dia / 2);
    }
}


module stepperBracketHoles(dia){
    translate([0, 11.8, 0])cylinder(baseThickness, d=dia); 
    translate([0, -11.8, 0])cylinder(baseThickness, d=dia); 
}


module Arduino(dia){
    color("lightblue"){
        // lower right USB (0,0 reference)
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([-50.8, 15.2, 0])         // lower left
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([-50.8, 43.1, 0])         // upper left
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([1.3, 48.2, 0])         // upper right
        cylinder(standoffHeight, dia / 2, dia / 2);
    }
}


module RP2040(dia){
    color("lightblue"){
        // symetrical, from CL
        RPwidth = 47.0;
        RPheight = 11.4;

        translate([-RPwidth/2, -RPheight/2, 0])    
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([-RPwidth/2, RPheight/2, 0])          
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([RPwidth/2, RPheight/2, 0])         
        cylinder(standoffHeight, dia / 2, dia / 2);

        translate([RPwidth/2, -RPheight/2, 0])      
        cylinder(standoffHeight, dia / 2, dia / 2);
    }
}



module roundedCube(dims, radius=2, center=false){
    // attempt at replicated cube, but with rounded edges from
    // https://youtu.be/gKOkJWiTgAY
    xdim =dims[0];
    ydim =dims[1];
    zdim =dims[2];
    
    if (center) {
        translate([-xdim/2, -ydim/2, -zdim/2]){
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
