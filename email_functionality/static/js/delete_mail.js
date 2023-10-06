document.addEventListener('DOMContentLoaded', ()=>{

   // Assigning the delete button to a variable
   const deleteButton = document.getElementById('delete_button');
   // Getting the id of the mail clicked
   var mail_url = document.getElementById('delete').getAttribute('data-mail-url');

   deleteButton.addEventListener('click', ()=>{
      // Ask for confirmation
      const confirmDelete = confirm('Are you sure you want to delete?');
      if(confirmDelete){
         //If user confirms delete action send an ajax request to the server
         const csrfToken = document.querySelector('#csrfToken').value
         deleteMail(mail_url, csrfToken)
      }

   })

})


// This function sends an asynchronous request to the server to delete the mail
function deleteMail(mail_url, csrfToken){
   $.ajax({
   // Http request is of type 'Delete'
   type:'POST',
   // Setting the mail url
   url: mail_url,
   headers : {'X-CSRFToken': csrfToken},

   // If the operation is successful displaying this msg
   success : ()=> {
      alert('Mail was deleted successfully');
   },
   // If the operation is unsuccessful then displaying this
   error : ()=> {
      alert('Error with deleting mail');
   }  
 })
}
