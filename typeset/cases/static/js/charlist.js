console.log('test');

// window.addEventListener("load", customJsStart);
window.onload = customJsStart;
function insertAfter(newNode, referenceNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);

}

function customJsStart() {

  var listOfChars = ["a", "b", "c", "d", "e"];
  var options = [];
  for(i=0;i < listOfChars.length; i+=1) {
    newchar = {
      "text": listOfChars[i],
      "value": listOfChars[i]
    }
    options.push(newchar);
  };

    var checkinputs = document.getElementsByClassName('vTextField');
    if(checkinputs[1].value == ""){
      console.log('null!');
      title = checkinputs[0];
      var autofill = document.createElement("p");
      var textnode = document.createTextNode("Click to autofill below fields with 74 common blocks")
      autofill.appendChild(textnode)
      autofill.setAttribute("style", "color: #417690");
      autofill.addEventListener('click', autofillBlocks(options));
      insertAfter(autofill, title);

    };




  var inputs = document.getElementsByClassName('vTextField');
  for (var i = 1; i < inputs.length; i += 1) {
    currentField = inputs[i];
    var x = document.createElement("select");

    x.setAttribute("id", "possiblechars");
    for (var j = 0; j < options.length; j++) {
      var option = options[j];
      var newOption = document.createElement("option");
      newOption.text = option.text;
      console.log(option.text);
      newOption.value = option.value;
      x.appendChild(newOption);
    }
    function handleEvent(passedInElement) {
      return function (e) {
        passedInElement.value = this.value;
      };
    }

    x.addEventListener('change', handleEvent(currentField));

    insertAfter(x, currentField);
  }

};

function autofillBlocks(blocks) {
  return function (e) {
    var inputs = document.getElementsByClassName('vTextField');
    for (var i = 1; i < inputs.length; i += 1) {
      currentField = inputs[i];
      currentField.value = blocks[0].value;
    }
  }
}
