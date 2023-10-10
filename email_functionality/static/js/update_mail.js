
document.addEventListener('DOMContentLoaded', () => {
    // Getting the recipient field and storing it in a variable
    const recipientField = document.querySelector('input[name="recipient"]');
    // calling disableField function to make it recipient field as only readable so user cant change it
    disableField(recipientField);
})

function disableField(field){
    // Setting the read only property to true so that user cant edit this
    field.readOnly = true;
}