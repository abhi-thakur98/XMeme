
function openForm() {
	document.getElementById("myForm").style.display = "flex";
}

function closeForm() {
	document.getElementById("post-form").reset();
	document.getElementById("myForm").style.display = "none";
	document.getElementById('message').style.display = "none";
}

$(document).ready(function(){
	$.ajax({
		type: "GET",
		url: "memes",
		success: function(response){
			console.log('Result');
			console.log(response);
			var feed = document.getElementById('feed');
			for (var i=0; i < response.length; i++){
				item = response[i]
				let fig = document.createElement("div");
				let img = document.createElement("img");
				let capt = document.createElement("p");
				let name = document.createElement("p");
				err = document.createAttribute('onError');
				err.value = "imgError(this);";
				img.setAttributeNode(err);
				img.src = item.url;
				capt.textContent = item.caption;
				name.textContent = item.name;
				fig.appendChild(name);
				fig.appendChild(capt);
				fig.appendChild(img);
				feed.appendChild(fig);
			}

		}
	});
});