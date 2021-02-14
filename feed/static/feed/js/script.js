
function openForm(patch) {
	if(patch == true){
		let source = document.getElementById("big-image").dataset.url;
		let name = document.getElementById("big-name").textContent;
		let caption = document.getElementById("big-caption").textContent;
		name = name.substring(name.search(':')+2,name.length);
		caption = caption.substring(caption.search(':')+2,caption.length);
		document.getElementById("name").value = name;
		document.getElementById("name").style.cursor = "not-allowed";
		document.getElementById("caption").value = caption;
		document.getElementById("url").value = source;
		document.getElementById("name").disabled = true;
		document.getElementById("get_data").textContent = "Make Changes";
	}
	else{
		document.getElementById("big-div").style.display = "none";
		document.getElementById("name").style.cursor = "initial";
	}
	document.getElementById("myForm").style.display = "flex";
}

function closeForm() {
	document.getElementById("name").disabled = false;
	document.getElementById("get_data").textContent = "Post";
	document.getElementById("post-form").reset();
	document.getElementById("myForm").style.display = "none";
	document.getElementById('message').style.display = "none";
}

function closeImage() {
	document.getElementById("big-div").style.display = "none";
}

$(document).ready(function(){
	$.ajax({
		type: "GET",
		url: "memes",
		success: function(response){
			var feed = document.getElementById('feed');
			for (var i=0; i < response.length; i++){
				item = response[i]
				let fig = document.createElement("div");
				let img = document.createElement("img");
				let capt = document.createElement("p");
				let name = document.createElement("p");
				let text = document.createElement("span");
				err = document.createAttribute('onError');
				err.value = "imgError(this);";
				img.setAttributeNode(err);
				img.dataset.url = item.url;
				img.src = item.url;
				capt.className = "caption";
				capt.textContent = item.caption;
				name.textContent = item.name;
				text.appendChild(name);
				text.appendChild(capt);
				fig.appendChild(text);
				fig.appendChild(img);
				click = document.createAttribute('onClick');
				click.value = "openImage(this)";
				fig.setAttributeNode(click);
				fig.id = item.id;
				fig.className = "meme-div";
				feed.appendChild(fig);
			}

		}
	});
});