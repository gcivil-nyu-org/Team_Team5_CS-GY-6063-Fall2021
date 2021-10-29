//Query All input fields
var form_fields = document.getElementsByTagName("input");
form_fields[1].placeholder = "Redistributor Name";
form_fields[2].placeholder = "Email";
form_fields[3].placeholder = "Username";
form_fields[4].placeholder = "Phone";
form_fields[5].placeholder = "Address";
form_fields[6].placeholder = "Password";
form_fields[7].placeholder = "Confirm Password";

for (var field in form_fields) {
  form_fields[field].className += " form-control";
}
