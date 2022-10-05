import 'style.css';
// Wait for the DOM to be ready
$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='registration']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      name: "required",

      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      password: {
        required: true,
        minlength: 5
      },
      confirmpassword: {
          required : true,
          minlength : 5,
          equalTo : "#password" //for checking both passwords are same or not
      }
    },
    // Specify validation error messages
    messages: {
      name: "Please enter your name",
      email: {
        required: "Please enter your email address",
        email: "Please enter a valid email address"
      },
      password: {
        required: "Please provide a password",
        minlength: "Your password must be consist of at least 5 characters"
      },
      
      confirmpassword : {
          required : "Please Re-enter the password",
          minlength : "Your password must be consist of at least 5 characters",
          equalTo : "Please enter the same password as above"
          }   
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});


