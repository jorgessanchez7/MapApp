var map;
var utah_dem_layer;
var utah_counties_layer;
var snowtel_network_layer;

require([
  "esri/Map",
  "esri/layers/MapImageLayer",
  "esri/views/MapView",
  "esri/layers/FeatureLayer",
  "dojo/domReady!"

  ], function showHide (Map, MapImageLayer, MapView, FeatureLayer) {
	  map = new Map ({
		  basemap: "topo"
	  });

	  snowtel_network_layer = new FeatureLayer ({
		  url: "http://geoserver2.byu.edu/arcgis/rest/services/The_SnowMen_FS/Snotel_Network/FeatureServer/0",
		  outFields: ["*"],
		  popupTemplate: {
			  title: "{Name}",
			  actions:[{
				  id:"snotel",
				  title:"Snotel Station"
			  }],
			  content: [{
				  type: "fields",
				  fieldInfos: [
				    {fieldName: "Name"},
					{fieldName: "Latitude"},
					{fieldName: "Longitude"},
					{fieldName: "Elevation_", label: "Elevation"},
					{fieldName: "ID"},
					{fieldName: "State"},
					{fieldName: "County"},
					{fieldName: "Network"}
				  ]
			  }]
		  }
	  });

	  utah_counties_layer = new FeatureLayer ({
		  url: "http://geoserver2.byu.edu/arcgis/rest/services/The_SnowMen_FS/Utah_Counties/FeatureServer/0",
		  outFields: ["*"],
		  popupTemplate: {
			  title: "{NAME}",
			  actions:[{
				  id:"county",
				  title:"Utah Counties"
			  }],
			  content: [{
				  type: "fields",
				  fieldInfos: [
				    {fieldName: "NAME", label: "Name"},
					{fieldName: "STATEFP", label: "State Code"},
					{fieldName: "COUNTYFP", label: "County Code"},
					{fieldName: "COUNTYNS", label: "ANSI Code"}
				  ]
			  }]
		  }
	  });

	  utah_dem_layer = new MapImageLayer ({
		  url: "http://geoserver2.byu.edu/arcgis/rest/services/The_SnowMen/Utah_DEM/MapServer"
	  });

	  map.layers.add(utah_dem_layer);
	  map.add(utah_counties_layer);
	  map.add(snowtel_network_layer);

	  var view = new MapView ({
		  container: "showMap",
		  map: map,
		  center: [-111.1, 39.1],
		  zoom: 6
	  });

	  view.when(function() {
        view.popup.watch("selectedFeature", function(graphic) {
          if (graphic) {
            // Set the action's visible property to true if the 'website' field value is not null, otherwise set it to false
            graphic.popupTemplate.actions.items[0].visible =
              graphic.attributes.website ? true : false;
          }
        });
      });

  	 }
);

function showHide (){
	utah_dem_layer.visible = false;
	utah_counties_layer.visible = false;
	snowtel_network_layer.visible = false;

	if(document.getElementById("Utah_DEM").checked){
		utah_dem_layer.visible = true;
	}
	if(document.getElementById("Utah_Counties").checked){
		 utah_counties_layer.visible = true;
	}
	if(document.getElementById("Snotel_Stations").checked){
		 snowtel_network_layer.visible = true;
	}
}
