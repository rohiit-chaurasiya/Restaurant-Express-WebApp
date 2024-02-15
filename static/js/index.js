$(window).on('load',function(){
    $('#check').modal('show');
});

function lettersonly(input) {
   var regex = /[^a-zA-Z\s]/gi;
   input.value=input.value.replace(regex,"");
}

function usernameonly(input) {
   var regex = /[^@-_-0-9a-zA-Z]/gi;
   input.value=input.value.replace(regex,"");
}

function numberonly(input) {
   var regex = /[^0-9]/gi;
   input.value=input.value.replace(regex,"");
}

function menuonly(input) {
   var regex = /[^1-9]/gi;
   input.value=input.value.replace(regex,"");
}

function date(input) {
   var regex = /[^0-9-/]/gi;
   input.value=input.value.replace(regex,"");
}

function addr(input) {
   var regex = /[^,-_-a-zA-Z\s]/gi;
   input.value=input.value.replace(regex,"");
}