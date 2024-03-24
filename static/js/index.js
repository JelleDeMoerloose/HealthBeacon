const textInput = document.getElementById('searchInput');
const errorMessage = document.getElementById('errorMessage');

const urlParams = new URLSearchParams(window.location.search);
let patiendId =  urlParams.get('patientid');

/*
let patients = []

fetch("http://localhost:5000/patients/all").then(response => response.json()).then(data => {

    patients = data

    

   
})

*/
const configureBtn = document.getElementById('configureBtn');

textInput.addEventListener('input', function(event) {
    
});


configureBtn.addEventListener('click', function() {
    const patientId = searchInput.value.trim(); // Get the value of the input field and remove leading/trailing whitespace
    
    if (patientId) {

        if(/^[0-9]+$/.test(patientId)){
        

        fetch(`http://localhost:5000/patients/id/${patientId}`).then(response => response.json()).then(data => {

        

        if (data.error && data.error === 'Patient not found') {
        
            console.log("patient not found");
            searchInput.style.border = '1px solid red';
            errorMessage.textContent = `Patient ID ${patientId} doesn't exist`
        } else {

            searchInput.style.border = '1px solid green';

        window.location.href = `/chat?patientid=${patientId}`;

           
            console.log(data)
        }


})

        
}
else{
    searchInput.style.border = '1px solid red';
    errorMessage.textContent = "Enter a valid patient ID"

}
    } else {
        searchInput.style.border = '1px solid red';
        errorMessage.textContent = "Enter a patient ID"
       
        
    }
});