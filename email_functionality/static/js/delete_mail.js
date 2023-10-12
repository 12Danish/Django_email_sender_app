document.addEventListener('DOMContentLoaded', ()=>{

   // Assigning the delete button to a variable
   const deleteButton = document.getElementById('delete_button');
   // Getting the id of the mail clicked
   const mail_url = document.getElementById('delete').getAttribute('data-mail-url');
   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
   deleteButton.addEventListener('click', ()=>{
      // Ask for confirmation
      const confirmDelete = confirm('Are you sure you want to delete?');
      if(confirmDelete){
         //If user confirms delete action send an ajax request to the server
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
   mode : 'same-origin',
   // If the operation is successful displaying this msg
   success : (response)=> {
      alert(response.message);
      window.location.href = response.redirect_url;
   },
   // If the operation is unsuccessful then displaying this
   error: (jqXHR, textStatus, errorThrown) => {
      alert("Error: " + textStatus + " - " + errorThrown);
      alert(jqXHR.responseText);
  }     
 })
}
