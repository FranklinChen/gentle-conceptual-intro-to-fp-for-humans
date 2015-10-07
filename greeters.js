let helloGreeter = function (name) {
    return "Hello, " + name;
};

let texanGreeter = function (name) {
    return "Howdy, " + name;
};

let myGreeters = [helloGreeter, texanGreeter];

for (greeter of myGreeters) {
    console.log(greeter("Franklin"));
}
