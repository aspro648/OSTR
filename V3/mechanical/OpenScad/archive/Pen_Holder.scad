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
servoScrewDia = 1.5;
servoScrewOffset = 14; // from CL of body

servoBracketOffsetX = -9;
servoBracketOffsetY = 22;
servoBracketOffsetZ = servoBracketHeight / 2;
supportThickness = 1;

standoffDia = 8;
standoffThickness = 4;
holderOffsetX = 10;
holderOffsetY = 0;

echo(servoBracketOffsetZ);


// PEN HOLDER
difference(){
    //solids
    union(){
        // base
        roundedCube([baseWid, baseLen, baseThickness], center=true, radius=2);
        // servo support        
        translate([0, -8, 0])
        roundedCube([baseWid, baseThickness+1, barrelHieght], center=true, radius=2);  
        // small bumpers
        rotate([90,0,0])
        translate([0, barrelHieght - 7,6.5, ])
        roundedCube([baseWid +1, baseThickness+1, 3], center=true, radius=2); 
        
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
        translate([8, 18.5, 6])        
        #roundedCube([7, 20, 8], center=true, radius=2); 
        rotate([90,0,0])
        translate([-8, 18.5, 6])        
        roundedCube([7, 20, 8], center=true, radius=2);
    }
}


// SERVO BRACKET
translate([servoBracketOffsetX, servoBracketOffsetY, servoBracketOffsetZ]){
   rotate([-90, 0, 90]){
        difference(){
            //solids
            union(){
                //bracket
                roundedCube([servoBracketWidth, servoBracketHeight, baseThickness], center=true, radius=2);
//                translate([-(servoBracketOffsetY - boreRadius), -(servoBracketHeight - servoBodyHeight) / 2, 0])
                //support
                tempZ = -9;
                //translate([-servoBracketOffsetX - servoBracketWidth - 2, tempZ, 0])

                // these are way too empirical
                translate([-servoBracketWidth/2+3, (servoBracketHeight - barrelHieght)/2, baseThickness/2])
                rotate([0,0,0])                
                cube([servoBracketWidth-5, barrelHieght, baseThickness], center=true);
                
                rotate([90,0,0]){
                // these are way too empirical
                translate([-servoBracketOffsetY+3,servoBracketOffsetX+6.25,-5])
                rotate([0,0,-30])
                #cube([baseThickness, servoBracketWidth/2,barrelHieght], center=true); }
  
                  // bevel
                translate([-servoBracketWidth/2+1, -servoBracketHeight/2+10, baseThickness/2])
                rotate([0, 0, 45])
                cube([4, 4, baseThickness], center=true);              
                
                }

            //cutouts
            union(){    // servo cutouts
                translate([0, -2, 0]){
                    // body
                    //cube([servoBodyWidth, servoBodyHeight, baseThickness * 4], center=true);
                    
                    // janky supports inside body cutout
                    translate([-servoBodyWidth/ 4, servoBodyHeight / 4,0])
                    cube([servoBodyWidth/ 2 - supportThickness, servoBodyHeight / 2 - supportThickness, baseThickness * 4], center=true);
                    translate([servoBodyWidth/ 4, servoBodyHeight / 4,0])
                    cube([servoBodyWidth/ 2 - supportThickness, servoBodyHeight / 2 - supportThickness, baseThickness * 4], center=true);
                    translate([servoBodyWidth/ 4, -servoBodyHeight / 4,0])
                    cube([servoBodyWidth/ 2 - supportThickness, servoBodyHeight / 2 - supportThickness, baseThickness * 4], center=true);
                    translate([-servoBodyWidth/ 4, -servoBodyHeight / 4,0])
                    cube([servoBodyWidth/ 2 - supportThickness, servoBodyHeight / 2 - supportThickness, baseThickness * 4], center=true);
                    
                    // vertical screw holes
                    translate([0, -servoScrewOffset, -1])
                    cylinder(baseThickness + 2, servoScrewDia / 2, servoScrewDia / 2);
                    translate([0, servoScrewOffset, 0])
                    cylinder(baseThickness + 1, servoScrewDia / 2, servoScrewDia / 2);
                }
                
                // corner cut
                translate([servoBracketWidth/2, servoBracketHeight/2 +2.5, baseThickness/2])
                rotate([0, 0, 45])
               #cube([servoBracketWidth / 1.5, servoBracketWidth/ 1.5, baseThickness], center=true);

                //bore cut to remove support overlap
                rotate([90,0,0])
                translate([-servoBracketOffsetY,servoBracketOffsetX,-servoBracketHeight/2 -baseThickness])
                cylinder(barrelHieght + 5, boreRadius, boreRadius); 

                // pen hat cutout
                //rotate([90,0,0])
                //translate([-servoBracketOffsetY,servoBracketOffsetX,10])
                //cylinder(20, 12, 12); 
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