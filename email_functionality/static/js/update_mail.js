document.addEventListener('DOMContentLoaded', () =>{
    const recipientField = document.querySelector('input[name="recipient"]');
    disableField(recipientField);
})

function disableField(field){
    field.disabled = true;
}