let greeter = function (greeting) {
    let specificGreeter = function (name) {
        // Note the reference to 'greeting'
        return greeting + ", " + name;
    };
    return specificGreeter;
};

let myGreeters = [greeter("Hello"), greeter("Howdy")];

for (greeter of myGreeters) {
    console.log(greeter("Franklin"));
}
