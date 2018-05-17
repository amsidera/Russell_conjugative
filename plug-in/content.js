chrome.runtime.sendMessage({
	'action': 'submit the form',
	'url': window.location.href,
	'selectedText': window.getSelection().toString(),
	'radio': form.value,
	'select': selectbutton.value
});