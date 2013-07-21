var AddressCheck = {
	_geocoder: null,
	_map: null,
	_mapOptions: {
        zoom: 14,
        center: new google.maps.LatLng(-34.397, 150.644),
        mapTypeId: google.maps.MapTypeId.ROADMAP		
	},
	_userMarker: null,
	_infoWindow: new google.maps.InfoWindow(),
	
	getCoordinates: function() {
		return AddressCheck._mapOptions.center;
	},
	
	check: function() {
		AddressCheck.setError('');
		var address = $.trim($('#address').val());
		if (!address) {
			AddressCheck.setError('No address was supplied.');
			return;
		}
		
		// first get the coordinates for that address	
	    if (null == AddressCheck._geocoder) {
	    	AddressCheck._geocoder = new google.maps.Geocoder();
	    }
		AddressCheck._geocoder.geocode( { 'address': address }, function(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				// remember the address coordinates
				AddressCheck._mapOptions.center = results[0].geometry.location;
				
				// initialize the map
				if (null == AddressCheck._map) {
					AddressCheck._map = new google.maps.Map(document.getElementById("map-canvas"), AddressCheck._mapOptions);
				}
				// update the center if the map was already in place
				AddressCheck._map.setCenter(AddressCheck._mapOptions.center);
				
				// initialize the user's marker
				if (null == AddressCheck._userMarker) {
			        AddressCheck._userMarker = new google.maps.Marker({
			            map: AddressCheck._map,
			            position: AddressCheck._mapOptions.center
			        });
			        
			        google.maps.event.addListener(AddressCheck._userMarker, 'click', function() {
		        		AddressCheck._infoWindow.setContent("This is you.");
		        		AddressCheck._infoWindow.open(AddressCheck._map, AddressCheck._userMarker);
			        });
				}
				// update the marker position if the marker was already in place
				AddressCheck._userMarker.setPosition(AddressCheck._mapOptions.center);
		    } 
			else {
		        AddressCheck.setError("Geocode was not successful for the following reason: " + status);
		    }			
		});
	},
	
	setError: function(html) {
		$('#error').html(html);
	},
	
	_handleSuccess: function(data) {
		alert(data);
	},
	
	_handleError: function(data) {
		AddressCheck.setError('There was an error checking the address: ' + data.statusText);
	}
	
		
};


$(function() {
	// register handlers
	$('#submit').click(AddressCheck.check);
});