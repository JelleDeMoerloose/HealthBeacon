let homescreen = document.getElementById("homescreen")
var url = new URL(window.location.href);
var patientId = Number(url.searchParams.get('patientid'));

homescreen.addEventListener("click", function () {
    navigateTo("home")
});

function navigateTo(link) {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = link;
    var newUrl = urlParts.join('/');
    window.location.href = newUrl + `?patientid=${patientId}`;
}
