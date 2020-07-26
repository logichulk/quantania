function delimit(raw_text)
{
	page = 1;
	lines = raw_text.split("\n");
	page_template = "<div id='${page}' class='step slide' data-x='-1000' data-y='-1500' data-autoplay='10'></div>"
	page_text = "";
	book_text = [];
	
	for(var i = 0; i < lines.length; i++)
	{
		line = lines[i];

		if(line.indexOf('#') == 0) // New chapter
		{
			book_text.push(page_text);
 
			line = "<h3>" + line + "</h3>";
			page_text = line + "<br/>";
		}		
		else
		{
			page_text += "<p>"+ lines[i] + "</p><br/>"
		}
	}

	if(page_text.length > 0)
	{
		book_text.push(page_text);
	}

	return book_text;
}

function arrange(raw_text)
{
	book_text = delimit(raw_text);
	console.log(book_text)
	document.getElementById("bored").innerHTML = book_text[0];
}

jQuery.get('https://logichulk.github.io/books/content/tales_of_quantania.html', 
	function(data) 
	{
	   arrange(data);
	});
