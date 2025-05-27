const student = {
  name: "John",
  surname: "Doe",
  academy: "Web Development",
  city: "New York",
  role: "Student",
  favColor: "Blue",
  printFullName: function() {
    console.log(this.name + " " + this.surname);
  },
  printFavColor: function() {
    console.log(this.favColor);
  }
};

console.log(student);
console.log(student.city);
student.printFullName();
student.printFavColor();
student.city = "San Francisco";
console.log(student.city);
