const textInput = document.getElementById('searchInput');
const errorMessage = document.getElementById('errorMessage');

/*
let patients = []

fetch("http://localhost:5000/patients/all").then(response => response.json()).then(data => {

    patients = data

    

   
})

*/
const configureBtn = document.getElementById('configureBtn');

textInput.addEventListener('input', function (event) {

});


configureBtn.addEventListener('click', function () {
    const patientId = searchInput.value.trim(); // Get the value of the input field and remove leading/trailing whitespace

    if (patientId) {

        if (/^[0-9]+$/.test(patientId)) {


            fetch(`/patients/id/${patientId}`).then(response => response.json()).then(data => {



                if (data.error && data.error === 'Patient not found') {

                    console.log("patient not found");
                    searchInput.style.border = '1px solid red';
                    errorMessage.textContent = `Patient ID ${patientId} doesn't exist`
                } else {

                    searchInput.style.border = '1px solid green';

                    window.location.href = `/home?patientid=${patientId}`;


                    console.log(data)
                }


            })


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