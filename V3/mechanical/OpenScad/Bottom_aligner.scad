$fn = 64;

boreDiameter = 8.8;  // pen diameter + clearance
boreRadius = boreDiameter / 2;

baseThickness = 3;
M3holeDia = 3.6;
M3nutDia = 6.6;
baseLen = 18;
baseWid = 28;

barrelHieght = 12;
barrelWallThickness = 1.2;

standoffDia = 8;
standoffThickness = 3;
holderOffsetX = 10;
holderOffsetY = -6;


// PEN HOLDER

difference(){
    //solids
    union(){
        // base
        roundedCube([baseWid, baseLen, baseThickness], center=true, radius=2);

        // barrel
        cylinder(	barrelHieght, r1=boreRadius + barrelWallThickness, 
                    r2=boreRadius + barrelWallThickness );
        
        // standoffs
        //translate([holderOffsetX, holderOffsetY, 0])
        //cylinder( standoffThickness, d=standoffDia);
        //translate([-holderOffsetX, -holderOffsetY, 0])
        //cylinder( standoffThickness, d=standoffDia);        
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
        cylinder( baseThickness * 2, d=M3nutDia);        

        translate([-holderOffsetX,- holderOffsetY, 0])
        cylinder( baseThickness, d=M3holeDia);   
        translate([-holderOffsetX, -holderOffsetY, 2]) rotate([0,0,90])
        cylinder( baseThickness * 2, d=M3nutDia);


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