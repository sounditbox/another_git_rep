function myFunc(){
    document.getElementById("toChange").innerHTML = "Hello Dolly.";
};

const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
