const textInput = document.getElementById('searchInput');
const errorMessage = document.getElementById('errorMessage');


const configureBtn = document.getElementById('configureBtn');

textInput.addEventListener('input', function (event) {

});


configureBtn.addEventListener('click', function () {
    const patientId = searchInput.value.trim(); // Get the value of the input field and remove leading/trailing whitespace

    if (patientId) {

        if (/^[0-9]+$/.test(patientId)) {

            fetch(`/patients/id/${patientId}`).then(response => {

                if (!response.ok) {
                    throw Error("network response was not ok ")
                }
                return response.json()
            }).then(response => {
                if (!response.exists) {
                    console.log("patient not found");
                    searchInput.style.border = '1px solid red';
                    errorMessage.textContent = `Patient ID ${patientId} doesn't exist`
                } else {
                    searchInput.style.border = '1px solid green';
                    window.location.href = `/home?patientid=${patientId}`;
                }
            }).catch(err => { console.error(err.message) })

        }
        else {
            searchInput.style.border = '1px solid red';
            errorMessage.textContent = "Enter a valid patient ID"

        }
    } else {
        searchInput.style.border = '1px solid red';
        errorMessage.textContent = "Enter a patient ID"


    }
});





