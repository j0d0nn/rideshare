var GiveRide = {
	
	confirm: function() {
		$('#formdata').hide();
		$('#confirmdata').show();
		var seats = $('#seats').val();
		$('#summary').html('<h1>OK, we\'ll jot you down for ' + seats + ' available ' + (seats > 1 ? 'seats' : 'seat') + ' at the location below.  Cool?</h1> \
				<input type="button" id="save" value="Cool" onclick="GiveRide.save()" /> \
				<input type="button" id="back" value="Not cool" onclick="GiveRide.revert()" />');
	},
	
	revert: function() {
		$('#formdata').show();
		$('#confirmdata').hide();
	},
	
	save: function() {
		var seats = $('#seats').val();
		var latlng = AddressCheck.getCoordinates();
		
		$.ajax({
			url: 'savedriver',
			data: {
				'lat': latlng.lat(),
				'long': latlng.lng(),
				'seats': seats
			},
			success: GiveRide.saveMessage,
			error: GiveRide.errorMessage
		});
	},
	
	saveMessage: function(data) {
		AddressCheck.setError('All set!  Thanks for your willingness to serve!');
	},
	
	errorMessage: function(data) {
		AddressCheck.setError('There was an error saving your information: ' + data.statusText);
	}
};

$(function() {
	// register handlers
	$('#submit').click(GiveRide.confirm);
});