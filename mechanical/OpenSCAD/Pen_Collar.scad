// pen holder for plotting robot

$fn = 64;

// holder variables
penDiameter = 10; // 12.5mm works with Sharpie Fine
                  // 11.75 for Visa-vis
                  // 10 mm for Crayola Washables
penRadius = penDiameter / 2;
barrelHieght = 10;
barrelWallThickness = 3;
baseThickness = 3;
cornerRounding = 2;

hat_thickness = 1.2;

hatDiameter = 26;
slice = 2;


module penHolder(){

	difference(){
		//// lip
        cylinder(hat_thickness, hatDiameter / 2, hatDiameter / 2);
        
        // pen hole
        cylinder(baseThickness, penRadius, penRadius);
        

        // expansion slice
        translate([ -slice / 2, 0, 0])
        cube([  slice, hatDiameter, barrelHieght]); 
	}

	// pen barrel
	difference(){
        // barrel

        barrel();

		// bore
		cylinder(   barrelHieght * 2, penRadius, penRadius);

        
        // expansion slice
        translate([ -slice / 2, 0, 0])
        cube([  slice, hatDiameter * 2, hatDiameter * 2]);   
	};  
}

module barrel()
        union(){{
		cylinder(	barrelHieght, 
					penRadius + hat_thickness, 
					penRadius + hat_thickness);


        rotate_extrude($fn=200)
        //rotate([90, 0, 0])
        translate([-penRadius - 2 * hat_thickness, hat_thickness, 0])
        polygon(points=[[2,2], [2,0], [0,0]]);
        }
    }
//barrel();
penHolder();





