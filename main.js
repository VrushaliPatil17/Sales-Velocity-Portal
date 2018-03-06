
function check(form)/*function to check userid & password*/
{
	 /*the following code checkes whether the entered userid and password are matching*/
	 if(form.userid.value == "Admin" && form.pswrd.value == "admin")
	  {
	    window.location = 'home.html'/*opens the target page while Id & password matches*/
	  }
	 else
	 {
	   alert("Error Password or Username")/*displays error message*/
	  }
}



function matchSearch()
{

	document.getElementById("cname").innerHTML = "Bank of America"
 		document.getElementById("dispUrl").innerHTML = "www.bankofamerica.com"
 		document.getElementById("matchs").innerHTML = "90"

	/* search comp name, url and domain on database and return the company profile*/
	/*var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      document.getElementById("info").innerHTML =
      this.responseText;
    }
  };

var obj= JSON.parse(responseText);

for (var i = 0; i < 12; i++) 
	{
		if(obj[i].company_name != "Bank of America")
		{
			document.getElementById("people").innerHTML = obj[i].customer_name
 			document.getElementById("pscore").innerHTML = obj[i].score
 			continue;
 		}
 		document.getElementById("cname").innerHTML = obj[i].company_name
 		document.getElementById("cname").innerHTML = obj[i].score

		
 	}



  var chk=document.getElementById("box").value;
  var x = document.getElementById("curl");
  var text = x.value;
  document.getElementById("dispUrl").innerHTML = text;

  xhttp.open("GET", "https://revx-ec72b.appspot.com/test", true);
  xhttp.send();*/

}

