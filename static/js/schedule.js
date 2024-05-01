let homescreen = document.getElementById("homescreen")

homescreen.addEventListener("click", function() {
    var currentUrl = window.location.href; // Get the current URL
    var urlParts = currentUrl.split('/'); // Split the URL into parts
    urlParts[urlParts.length - 1] = 'homescreen.html'; // Replace the last part
    var newUrl = urlParts.join('/'); // Rejoin the URL parts
    window.location.href = newUrl; // Navigate to the new URL
});