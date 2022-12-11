function register() {

  const email =document.getElementById("email")
  const name = document.getElementById("name")
  const consumerno = document.getElementById("consumerno")
  const password = document.getElementById("password")
  var url = "http://localhost:8000/api/register/"

  var http = new XMLHttpRequest();

  http.open("GET", url+"?"+"email="+email+"&"+"name="+name+"&"+"consumerno="+consumerno+"&"+"password="+password, true);
  http.onreadystatechange = function()
  {
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
          }
    }
  http.send(null);

}
function test(){
  const email = document.getElementById("email").value
  const name = document.getElementById("name").value
  const consumerno = document.getElementById("consumerno").value
  const password = document.getElementById("password").value
  console.log(email,name,consumerno,password)
  var url = "http://localhost:8000/api/register/"
  var http = new XMLHttpRequest();
  http.open("POST", url+"?"+"email="+email+"&"+"name="+name+"&"+"consumerno="+consumerno+"&"+"password="+password, true);

  http.onreadystatechange = function()
  {
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
          }
    }
  http.send(null);
  console.log("mission success")
  console.log(http.response())
}
