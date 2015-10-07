let greeter = greeting => {
    return name => {
        return greeting + ", " + name;
    };
};

let myGreeters = [greeter("Hello"), greeter("Howdy")];

// ["Hello, Franklin", "Howdy, Franklin"]
let myGreetings =
        myGreeters.map(greeter => greeter("Franklin"));
