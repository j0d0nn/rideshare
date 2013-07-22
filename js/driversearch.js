var DriverSearch = {
	
	findNearbyDrivers: function(latlng, map) {
		this._map = map;
		var mapBounds = map.getBounds();
		$.ajax({
			url: 'finddriver',
			data: {
				'nelat': mapBounds.getNorthEast().lat(),
				'nelong': mapBounds.getNorthEast().lng(),
				'swlat': mapBounds.getSouthWest().lat(),
				'swlong': mapBounds.getSouthWest().lng()
			},
			success: DriverSearch.pinDrivers,
			error: DriverSearch.error
		});
	},

	pinDrivers: function(data) {
		
		// we're not going to bother blowing away the old markers; messes with the overlays
		var markerImage = new google.maps.MarkerImage("/img/car_icon.png");
		for (var i = 0, ilen = data.length; i < ilen; ++i) {
			var driver = data[i];
			var latlng = new google.maps.LatLng(driver.lat, driver.lng);
	        var marker = new google.maps.Marker({
	            map: AddressCheck._map,
	            position: latlng,
	            icon: markerImage
	        });
	        
	        var message = '\
	        	<div class="driverdesc">\
	        		<div class="seatcount">This driver has ' + driver.seats + (driver.seats > 1 ? " seats" : " seat") + ' available.</div>\
	        		<div class="contact">To request a ride, email <a href="mailto:' + driver.email + '">' + driver.email + '</a></div>\
	        	</div>';
	        google.maps.event.addListener(marker, 'click', (function(marker, message) {
	            return function() {
	            	AddressCheck._infoWindow.setContent(message);
	            	AddressCheck._infoWindow.open(AddressCheck._map, marker);
	            }
	        })(marker, message));
		}
	},
	
	error: function(data) {
		AddressCheck.setError("The driver search failed: " + data.statusText);
	}
};