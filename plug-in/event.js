// callback function
	// Inject the content script into the current page

$('#polarity input').on('change', function() {
   myRadio =($('input[name="polarity"]:checked', '#polarity').val());
   var makeItGreen = 'var form = document.createElement("radiobutton"); form.value='+myRadio+';';
	chrome.tabs.executeScript({code: makeItGreen});
});

$('#selection').on('change', function() {
conceptName = $('#selection').find(":selected").val();
var makeIt = 'var selectbutton = document.createElement("selectbutton"); selectbutton.value='+conceptName+';';
chrome.tabs.executeScript({code: makeIt});
});
document.getElementById("form").addEventListener('click', () => {
	// Inject the content script into the current page
	chrome.tabs.executeScript(null, { file: 'content.js'});
});

// Perform the callback when a message is received from the content script
chrome.runtime.onMessage.addListener(function(message){
	if (message.action == 'submit the form'){
		chrome.tabs.executeScript(null, {file: 'request.js'});
	}
});

var context = "Russelll";
var title = "Plug-in NLP";
//var id = chrome.contextMenus.create({"title": title, "contexts": [context], "onclick": onItemClick});