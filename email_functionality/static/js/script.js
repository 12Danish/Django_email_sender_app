document.addEventListener('DOMContentLoaded', ()=>
{
   // Selecting specifics from the form and assigning them to variables
   const sendButton = document.getElementById('Send');
   const draftButton = document.getElementById('Draft');
   const myForm = document.getElementById('myform');
   const recipientField = document.querySelector('input[name="recipient"]');
   const statusField = document.querySelector('input[name="status"]');

   // function to disable buttons if recipient field is empty
   function disableButtons(){
       recipientValue = recipientField.value.trim();

       //Checking recipient value

       if(recipientValue){
       sendButton.disabled = false;
       draftButton.disabled = false;
       }
       else{
       sendButton.disabled = true;
       draftButton.disabled = true;
       }
   }

   // Disabling and enabling buttons based on input of recipient
   recipientField.addEventListener('input',disableButtons);

   disableButtons();

   // changing value of status to 'send'
   sendButton.addEventListener('click', ()=>
   {
   statusField.value = 'send';
   myForm.submit();
   }
   );

    // changing value of status to 'draft'
   draftButton.addEventListener('click', ()=>
   {
   statusField.value = 'draft';
   myForm.submit();
   }
   );
}
);