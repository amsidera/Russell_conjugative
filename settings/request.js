var result = "";
var makeitGreen = '';
var jsdata = ''; 
	$.ajax({
	  type: "POST",
		  url: "http://localhost:5000/",
		  data: { url: window.location.href, position: "adjective"},
		  success: function( data ) { 
			result = data; 
			document.body.innerHTML = data;
			var s = document.createElement("script");
				function readTextFile()
				{
					var rawFile = new XMLHttpRequest();
					rawFile.open("GET", "http://localhost:5000/settings", true);
					rawFile.onreadystatechange = function ()
					{
						if(rawFile.readyState === 4)
						{
							if(rawFile.status === 200 || rawFile.status == 0)
							{
								var allText = rawFile.responseText;
								allText = allText.replace(/&lt;/g,"<")
								s.innerHTML = allText;
								document.head.appendChild(s);
							}
						}
					}
					rawFile.send(null);
				}
				readTextFile();
			}   
		});
