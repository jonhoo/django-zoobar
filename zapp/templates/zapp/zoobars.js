
{% if user.person.zoobars > 0 %}
var myZoobars = {{ user.person.zoobars }};
{% else %}
var myZoobars = 0;
{% endif %}

var div = document.getElementById("myZoobars");
if (div != null) {
    div.innerHTML = myZoobars;
}
