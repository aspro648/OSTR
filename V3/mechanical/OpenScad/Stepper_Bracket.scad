// 28byj 48 Stepper Motor Mount
// https://www.amazon.com/dp/B015RQ97W8


$fn = 64;  // smooth circles

version = "V0.1";

M3holeDia = 3.6;
M3nutDia = 6.5;
thickness = 3;
base_len = 32;   // y axis
base_wid = 21; // x axis


difference(){
    union(){ // SOLIDS
        //base plate
        translate([base_wid/2, 0, 0])
        roundedCube([base_wid, base_len, thickness], center=true);

        //bulkhead
        translate([0, 0, 22.5/2])
        rotate([0, 90, 0])
        roundedCube([22.5, 45, thickness], center=true);

        //fillet
        radius = 5;
        difference(){
            offset = thickness + radius / 2;
            translate([offset, 0, offset])
            cube([radius, base_len, radius], center=true);
            translate([offset + radius/2, 0, offset + radius / 2])
            rotate([90, 90, 0])
            cylinder(h=33, r=radius, center=true);
        }
    }

    union(){ // CUTOUTS
        //bolt holes
        translate([10, 12., 0]) cylinder(10, d=M3holeDia); 
        translate([10, -12., 0]) cylinder(10, d=M3holeDia);
        translate([10, 12., 1.5]) cylinder(10, d=M3nutDia, $fn=6); 
        translate([10, -12., 1.5]) cylinder(10, d=M3nutDia, $fn=6); 

        // stepper
        translate([14.5, 0, 15]) //14.4
        rotate([90, 0, -90])
        stepper();
    }
}


module stepper(){
    height=25;
    tab_width = 8;
    cylinder(h=height, r=14.5, center=true); // stepper body
    translate([17.5,0,0]) cylinder(h=height, r=tab_width/2, center=true); 
    translate([-17.5,0,0]) cylinder(h=height, r=tab_width/2, center=true); 
    translate([-17.5,0,5]) cylinder(h=height+10, d=M3holeDia, center=true); 
    translate([17.5,0,5]) cylinder(h=height+10, d=M3holeDia, center=true); 
    cube([35, tab_width, height], center=true);
    translate([0,-8,5])cylinder(h=height+10, r=5.5, center=true);
    translate([0,10,0]) cube([20, 17, height], center=true);
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