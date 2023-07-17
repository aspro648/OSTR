$fn = 64;

boreDiameter = 11.5;  // pen diameter + clearance
boreRadius = boreDiameter / 2;

baseThickness = 3;
M3holeDia = 3.6;
M3nutDia = 6.5;
baseLen = 20;
baseWid = 28;

barrelHieght = 30;
barrelWallThickness = 1.2;


// servo bracket variables
servoBracketHeight = 40;
servoBracketWidth = 23;
servoBodyHeight = 24.5;
servoBodyWidth = 13.5;
servoScrewDia = 2;
servoScrewOffset = 14; // from CL of body

servoBracketOffsetX = 0;
servoBracketOffsetY = 21;
servoBracketOffsetZ = 25;
supportThickness = 1;

standoffDia = 8;
standoffThickness = 4;
holderOffsetX = 10;
holderOffsetY = 6;

batteryOffsetY = 17.5;  //from CL

echo(servoBracketOffsetZ);


// PEN HOLDER
rotate([0, 0, 0]) 
difference(){
    //solids
    union(){
        // base
        tempOffset = 10;
        translate([0, tempOffset/2, 0,])
        roundedCube([baseWid, baseLen + tempOffset, baseThickness], center=true, radius=2);

        // stepper support        
        translate([0, 0, 0])
        roundedCube([baseWid + 20, 4, barrelHieght], center=true, radius=1);  
        // small bumpers
        rotate([90,0,0])
        translate([0, barrelHieght - 3, - baseThickness /2])
        roundedCube([baseWid + 21, baseThickness, 3], center=true, radius=2); 

        // survo support        
        translate([-8, 0, 0])
        cube([baseThickness, 38, servoBracketOffsetZ - servoBodyWidth/2 + 0.5], center=false);  
        
        // barrel
        cylinder(	barrelHieght, r1=boreRadius + barrelWallThickness, 
                    r2=boreRadius + barrelWallThickness );
        
        // standoffs
        translate([holderOffsetX, holderOffsetY, 0])
        cylinder( standoffThickness, d=standoffDia);
        translate([-holderOffsetX, -holderOffsetY, 0])
        cylinder( standoffThickness, d=standoffDia);        
    }

    //cutouts
    union(){
        // bore
        cylinder(barrelHieght + 1, boreRadius, boreRadius);        
        
        //mount holes
        hole_offset = 5;
        translate([holderOffsetX, holderOffsetY, 0])
        cylinder( baseThickness, d=M3holeDia);
        translate([holderOffsetX, holderOffsetY, 2])  rotate([0,0,90])      
        cylinder( baseThickness * 2, d=M3nutDia, $fn=6);        

        translate([-holderOffsetX,- holderOffsetY, 0])
        cylinder( baseThickness, d=M3holeDia);   
        translate([-holderOffsetX, -holderOffsetY, 2]) rotate([0,0,90])
        cylinder( baseThickness * 2, d=M3nutDia, $fn=6);

        //servo support wire cutouts
        rotate([90,0,0])
        translate([15, 16, -4])        
        roundedCube([7, 20, 8], center=true, radius=2); 
        rotate([90,0,0])
        translate([-15, 16, -4])        
        roundedCube([7, 20, 8], center=true, radius=2);
        
        //battery standoff clearance
        translate([0, batteryOffsetY, 0])
        cylinder( standoffThickness+1, d=standoffDia+1);
        
        // barrel trim for servo horn
        //translate([0, boreRadius * 2-.5, barrelHieght])
        //cube([10, 10, 20], center=true);
    }
}


// SERVO BRACKET
//translate([servoBracketOffsetX, servoBracketOffsetY, servoBracketOffsetZ]){


translate([servoBracketOffsetX, servoBracketOffsetY, servoBracketOffsetZ]){rotate([90, 0, 0]){   //[-90, 0, 90]
        difference(){
            //solids
            union(){
                //bracket
                roundedCube([servoBracketHeight, servoBracketWidth, baseThickness], center=true, radius=2);

                translate([0, -servoBracketOffsetZ/2-1, baseThickness/2])
                cube([servoBracketHeight, servoBracketWidth, baseThickness], center=true);
                
                // strengthening beams
                rotate([90, 0, 0])
                translate([servoBracketWidth - 6, 3, -10])
                cylinder(35, 2., 2., center=false);                

                rotate([90, 0, 0])
                translate([-servoBracketWidth + 6, 3, -10])
                cylinder(35, 2., 2., center=false);
                
//                translate([-(servoBracketOffsetY - boreRadius), -(servoBracketHeight - servoBodyHeight) / 2, 0])
                //support

                //translate([-servoBracketOffsetX - servoBracketWidth - 2, tempZ, 0])

                /*
                // these are way too empirical
                translate([-servoBracketWidth/2+2.9, (servoBracketHeight - barrelHieght)/2, baseThickness/2])
                rotate([0,0,0])                
                #cube([servoBracketWidth-8, barrelHieght, baseThickness], center=true);
                
                rotate([90,0,0]){
                // these are way too empirical
                translate([-servoBracketOffsetY+3,servoBracketOffsetX+6.25,-5])
                rotate([0,0,-30])
                #cube([baseThickness, servoBracketWidth/2 -6.85,barrelHieght], center=true); }
                */
                
                }

            //cutouts
            union(){    // servo cutouts
                translate([0, 0, 0]){
                    // body
                    //cube([servoBodyWidth, servoBodyHeight, baseThickness * 4], center=true);
                    
                    // janky supports inside body cutout
                    tempX = servoBodyHeight / 3 - supportThickness;
                    tempY = servoBodyWidth/ 2 - supportThickness;
                    tempZ = baseThickness * 2;
                    translate([servoBodyHeight / 3,-servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);
                    translate([servoBodyHeight / 3,servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);
                    translate([-servoBodyHeight / 3,servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);
                    translate([-servoBodyHeight / 3, -servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);                
                    translate([0, -servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);
                    translate([0, servoBodyWidth/ 4, 2])
                    cube([tempX, tempY, tempZ], center=true);
                    
                    // vertical screw holes
                    translate([-servoScrewOffset, 0,  -1])
                    #cylinder(baseThickness + 4, servoScrewDia / 2, servoScrewDia / 2);
                    translate([servoScrewOffset, 0, -1])
                    cylinder(baseThickness + 4, servoScrewDia / 2, servoScrewDia / 2);

                    //battery standoff clearance
                    rotate([90,0,0])
                    translate([0, 3.5, servoBracketOffsetZ-standoffThickness])
                    cylinder( standoffThickness+1, d=standoffDia+1);

                }
                
                /*
                // corner cut
                translate([servoBracketWidth/2, servoBracketHeight/2 +2.5, baseThickness/2])
                rotate([0, 0, 45])
               #cube([servoBracketWidth / 1.5, servoBracketWidth/ 1.5, baseThickness], center=true);
                */
                
                /*
                //bore cut to remove support overlap
                rotate([90,0,0])
                translate([-servoBracketOffsetY,servoBracketOffsetX,-servoBracketHeight/2 -baseThickness])
                cylinder(barrelHieght + 5, boreRadius, boreRadius); 
                */

                /*
                // pen hat cutout
                rotate([90,0,0])
                translate([-servoBracketOffsetY,servoBracketOffsetX,10])
                #cylinder(4, 12, 12); 
                */
            }
        }
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


module OldroundedCube(xdim ,ydim ,zdim, rdim){
    translate([-xdim/2, -ydim/2, 0])
	hull(){ // https://youtu.be/gKOkJWiTgAY
		translate([rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
	}
}