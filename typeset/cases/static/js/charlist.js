console.log('test');

// window.addEventListener("load", customJsStart);
window.onload = customJsStart;
function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function customJsStart(){ 

    var options =
[
  {
    "text"  : "a",
    "value" : "a"
  },
  {
    "text"     : "ñ",
    "value"    : "ñ",
    "selected" : true
  },
  {
    "text"  : "Z",
    "value" : "Z"
  }
];


var inputs = document.getElementsByClassName('vTextField');
for (var i = 1; i < inputs.length; i += 1) {
    currentField = inputs[i];
    var x = document.createElement("select"); 
    
    x.setAttribute("id", "possiblechars");
    for(var j = 0; j < options.length; j++){
        var option = options[j];
        var newOption = document.createElement("option");
        newOption.text = option.text;
        console.log(option.text);
        newOption.value = option.value;
        x.appendChild(newOption);
      }
      function handleEvent(passedInElement) {
        return function(e) {
            passedInElement.value = this.value;
        };
    }
    
    x.addEventListener('change', handleEvent(currentField));

    insertAfter(x, currentField);
}

};


