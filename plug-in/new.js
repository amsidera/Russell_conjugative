function mytoggle2(element,top){
	var button = document.getElementById(top).getElementsByTagName('button');
	var second = document.getElementById(top).getElementsByTagName('div');
	var dropdowns = second[0].getElementsByTagName('a');
	var i;
	if (dropdowns[dropdowns.length-1].id == 'last'+top){
		var x = '(' + button[0].innerHTML;
		for (i = 0; i < dropdowns.length-1; i++) {
			  var openDropdown = dropdowns[i];
			  openDropdown.style.display = 'none';
			  x = x + '/' + openDropdown.innerHTML;
		  }
		 x = x+ ')';
		button[0].innerHTML = x;
		element.id = 'bottom'+top;
		element.innerHTML = 'Back';
	}
	else{
		for (i = 0; i < dropdowns.length-1; i++) {
		  var openDropdown = dropdowns[i];
		  openDropdown.style.display = 'block';
		}
		var res = button[0].innerHTML.split("/");
		var finale = res[0].replace('(', '');
		button[0].innerHTML = finale;
		element.innerHTML = 'All';
		element.id = 'last'+top;
	}
}

function mytoggle(element, value) {
	var word_old = value.innerHTML;
	if (word_old[0] != '('){
	value.innerHTML = element.innerHTML;
	element.innerHTML = word_old;
	}
	}
function iitbutton(elem) {
	var x = 'text' + elem;
	document.getElementById(x).classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

	var dropdowns = document.getElementsByClassName("dropdown-content");
	var i;
	for (i = 0; i < dropdowns.length; i++) {
	  var openDropdown = dropdowns[i];
	  if (openDropdown.classList.contains('show')) {
		openDropdown.classList.remove('show');
	  }
	}
  }
}
function myFunction() {
	var x = document.getElementById("desplegar");
	if (x.style.display === "none") {
		x.style.display = "block";
	} else {
		x.style.display = "none";
	}
}
function handleBtnClick(event) {
  toggleButton(event.target);
}

function handleBtnKeyPress(event) {
  // Check to see if space or enter were pressed
  if (event.key === " " || event.key === "Enter") {
	// Prevent the default action to stop scrolling when space is pressed
	event.preventDefault();
	toggleButton(event.target);
  }
}

function toggleButton(element) {
  // Check to see if the button is pressed
  var pressed = (element.getAttribute("aria-pressed") === "true");
  // Change aria-pressed to the opposite state
  element.setAttribute("aria-pressed", !pressed);
}
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
	output.innerHTML = this.value;
}