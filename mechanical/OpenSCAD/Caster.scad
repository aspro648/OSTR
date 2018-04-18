// Original: http://www.thingiverse.com/thing:8959/
// Marble Caster by HipsterLogic

// Modified by 648.ken@gmail.com
// MakersBox.blogspot.com

// Added tapper the top lip to keep it from snagging on things.
// Added recess for screw heads if baseThickness > 3mm
// Added pedistal base so you can adjust platform hieght.


deckHeight = 18.5;    // from chassis bottom to ground, (must be at lease ballDiameter)
ballDiameter = 16.5;    // 7/16" ball bearing = 12.25mm, WAS 16.5  16mm = 5/8" ball bearing
ballTolerance = 0.4;  // play between ball and surface
wallThickness = 2.5;
gapWidth = ballDiameter / 3;
baseThickness = 2.5; // WAS 3


//baseHeight = ballDiameter + wallThickness * 2;
pedistalWidth = ballDiameter + wallThickness * 2;

baseWidth = 30; // distance between mounting holes

M3holeDia = 3.5;
M3nutDia = 6.5;


echo(deckHeight);
baseHeight = deckHeight - ballDiameter / 2;
echo(baseHeight);

module mainShape(){

    // mounting cross-piece
	translate([-baseWidth/2, -wallThickness - M3holeDia / 2, 0]) 
        cube([baseWidth, wallThickness * 2 + M3holeDia, baseThickness]);
	
	// bolt ends
	translate([baseWidth / 2, 0, 0]) 
        cylinder(baseThickness, M3holeDia / 2 + wallThickness, M3holeDia / 2 + wallThickness, $fn=40);
	translate([-baseWidth / 2, 0, 0]) 
        cylinder(baseThickness, M3holeDia / 2 + wallThickness, M3holeDia / 2 + wallThickness, $fn=40);
    

	// main cylindrical body
	translate([0, 0, 0])
        cylinder(baseHeight - 3, pedistalWidth / 2, pedistalWidth / 2, $fn=50);

	difference(){
        // tapper shere at top
		translate([0, 0, baseHeight - 2])
            sphere(pedistalWidth / 2, $fn=50);
                
        // shave the top flat
		translate([0, 0, baseHeight + ballDiameter / 2 - ballDiameter / 5])
            cylinder(25, 25, 25, $fn=50);
        
		// shave the bottom	flat	
		translate([0, 0, -12])
            cylinder(12, 25, 25, $fn=50);
  
	};
}

module cutout(){
    
    // ball hole
	translate([0, 0, baseHeight + ballTolerance]) 
        sphere(ballDiameter / 2 + ballTolerance, $fn=50);
	
    // slot to remove ball
    slotOffset = ballDiameter / 2.5;  // distance below baseHeight to cut slot
    if (baseHeight - slotOffset > baseThickness){
        translate([-gapWidth / 2, -baseWidth / 2, 
                   baseHeight - slotOffset]) 
            cube([gapWidth, baseWidth, ballDiameter]);
        
        }
    else{ // don't cut into base
        translate([-gapWidth / 2, -baseWidth / 2, 
                   baseThickness]) 
            cube([gapWidth, baseWidth, ballDiameter]);        
    }
    
    //trim sides
    translate([-25, ballDiameter / 2 + 0.5, 0]) 
            cube([50, ballDiameter, 50]);      

    translate([-25, -ballDiameter - 0.5, 0]) 
            cube([50, ballDiameter / 2, 50]);    

    if ((baseHeight - ballDiameter / 2) > baseThickness){
         // ball void to save material
        translate([0, 0, baseHeight - ballDiameter - 1]) 
            sphere(ballDiameter / 2, $fn=50);
    }

}

module mountingHoles(){
    // left m3 hole
	translate([baseWidth / 2, 0, 0])
	cylinder(baseThickness + 2, M3holeDia / 2, M3holeDia / 2, $fn=30);

    // countersink
	//translate([baseWidth / 2, 0, 2]) 
    //rotate([0, 0, 30])
	//cylinder(baseThickness + 2, M3holeDia, //M3holeDia, $fn=6);

    // right m3 hole
	translate([-baseWidth / 2, 0, 0]) 
	cylinder(baseThickness + 2, M3holeDia / 2, M3holeDia/2, $fn=30);

    // countersink
	//translate([-baseWidth / 2, 0, 2]) 
    //rotate([0, 0, 30])
	//cylinder(baseThickness + 2, M3holeDia, //M3holeDia, $fn=6);
}


rotate([0, 0, 90])
difference(){
	mainShape();
	cutout();
	mountingHoles();
    
}

// show ball?
//translate([0, 0, baseHeight]) 
//    sphere(ballDiameter/2, $fn=50);