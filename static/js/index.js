const textInput = document.getElementById('searchInput');


textInput.addEventListener('input', function(event) {
    // This function will be called every time the input value changes
    console.log('Input value changed:', event.target.value);
    // You can perform any action you want here
});
