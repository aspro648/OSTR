// pen holder for plotting robot




// Diameter of pen in mm.
penDiameter = 10.75;  // 10.60

union();

$fn = 64;

barrelDiameter = 15; // don't change or M3 holes shift

penRadius = penDiameter / 2;
barrelHieght = 24 + 2;
barrelWallThickness = 2;
baseThickness = 2.9;
cornerRounding = 2;
M3holeDia = 3.5;
M3nutDia = 6.6;
holeOffset = M3holeDia * 1.2;
baseLen = 15;
//baseWid = penDiameter + 2 * barrelWallThickness + 2;
baseWid = 20;
echo(baseWid);
echo(baseLen);


// servo bracket variables
servoOveralHeight = 34.5;  // 34.5 
servoBodyHeight = 24;
servoBodyWidth = 13;
servoScrewDia = 1.5;
servoScrewOffset = 2;
servoHeightOffset = barrelHieght - 5;
servoFwdOffset = penRadius + barrelWallThickness + baseThickness + 12;

rotate([0, 0, 180])
translate([-6.2, 3, 0])
difference(){
	union(){
		penHolder();
		servoBracket();
	}
    // re-drill the hole covered by servoBracket
	translate([0, 0, 0])
	cylinder(barrelHieght + baseThickness, penRadius, penRadius+0.2);

    translate([-40, -40, -40])
    cube([80, 80, 40]);

    rotate([0, 0, 0])
    union(){
		
		// pen hole
		//
    }
}	



module roundedCube(xdim ,ydim ,zdim, rdim){
	hull(){ // https://youtu.be/gKOkJWiTgAY
		translate([rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
	}
}


module halfRoundedCube(xdim ,ydim ,zdim, rdim){
	hull(){ // only round two sides
		translate([0, rdim, 0]) cube([2, rdim * 2, zdim]);
		translate([xdim-rdim, rdim, 0]) cube([rdim, rdim * 2, zdim]);
		translate([rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
	}
}


module halfRoundedCube2(xdim ,ydim ,zdim, rdim){
	hull(){ // https://youtu.be/gKOkJWiTgAY
		translate([rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, 0, 0]) cube([rdim, rdim * 2, zdim ]);
		translate([rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, ydim-rdim, 0]) cube([zdim, rdim, rdim]);
	}
}


module halfRoundedCube3(xdim ,ydim ,zdim, rdim){
	hull(){ // https://youtu.be/gKOkJWiTgAY
		translate([rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([0, ydim-rdim, 0]) cube([zdim, rdim, rdim]);
		translate([xdim-rdim, ydim-rdim, 0]) cube([zdim, rdim, rdim + 1]);
	}
}



module penHolder(){
	// base plate
    rotate([0, 0, 0])
	difference(){
		translate([	-baseWid / 2, -baseLen / 2, 0])

		// base piece
		//roundedCube(baseWid, baseLen, baseThickness, cornerRounding);
        cube([baseWid, baseLen, baseThickness + 1.5]);

		// pen hole
		//cylinder(baseThickness, penRadius, penRadius);
    };


	// pen barrel
	translate([0, 0, baseThickness])
	difference(){
		// barrel
		cylinder(	barrelHieght, 
					penRadius + barrelWallThickness, 
					penRadius + barrelWallThickness );
		// bore
		//cylinder(barrelHieght, penRadius, penRadius + 0.25);	
	}
}


module servoBracket(){
	// servo bracket face
	//rotate([0, 90, 90]) // (z, z, x) now
	//translate([	-servoHeightOffset, 0, servoFwdOffset])
    translate([-servoFwdOffset, 3, servoHeightOffset])
    rotate([90, 0, 90])

 
	difference(){
		// base 

		union(){

            
			translate([-(   servoBodyWidth + 2 * baseThickness) / 2 -1.5,
						 	-servoOveralHeight / 2 - 6, 0])
			halfRoundedCube(servoBodyWidth + 3 * baseThickness,
							servoOveralHeight + 6, 
                            baseThickness, cornerRounding);         
		}
        
        // cut off underneath
        //translate([-50, -50, -100])
        //cube([100, 100, 100]);
        
        // base holes
		translate([ -(servoBodyWidth + 2 * baseThickness) / 2 + M3holeDia,
					-servoOveralHeight / 2 + 1, 10 / 1.5])
		rotate([90, 0, 0])
		cylinder(baseThickness + 2, d=M3holeDia, d=M3holeDia);

		// body cutout
		translate([-servoBodyWidth / 2, -servoBodyHeight / 2, 0])
		cube([servoBodyWidth, servoBodyHeight , baseThickness + 1]);

		//translate([-servoBodyWidth / 2, 0.6, 0])
		//cube([servoBodyWidth, servoBodyHeight / 2 - 0.6, baseThickness + 1]);

		// vertical screw holes
		translate([0, -servoBodyHeight / 2 - servoScrewOffset, 0])
		cylinder(baseThickness + 1, servoScrewDia / 2, servoScrewDia / 2);
		translate([0, servoBodyHeight / 2 + servoScrewOffset, 0])
		cylinder(baseThickness + 1, servoScrewDia / 2, servoScrewDia / 2);
        

	}


}





