// // // Add your JavaScript logic here
// // function calculate() {
// //     const firstNo = parseFloat(document.getElementById('firstNo').value);
// //     const secondNo = parseFloat(document.getElementById('secondNo').value);
// //     // const result = firstNo * secondNo;
// //     // alert(`Result: ${result}`);
// // }


// // Register Event Handlers Upon loading webpage
// window.addEventListener("DOMContentLoaded", loadHandler)

// // Load Handler
// function loadHandler(){
//     let calculate_button = document.getElementById("calculate_button");
//     calculate_button.addEventListener("click", calculate_handler);
// }

// function wrapMathJax(math_input, function_name){
//     let output = "";
//     if (function_name === "f"){
//         output = output.concat("f(x) = ");
//     } else if (function_name === "g"){
//         output = output.concat("g(x) = ");
//     } else{
//         output = output.concat("h(x) = ");
//     }

//     return output.concat(math_input)

// }

// function calculate_handler(){
//     console.log("button clicked");
//     document.getElementById("hide_elements_container").style.display = "block";
//     document.getElementById("hide_elements_container").style.visibility = "visible";
//     convert();
// }

// function convert() {
//     //  Get the TeX input
//     let input_f = wrapMathJax(document.getElementById('f_input_value').value.trim(), "f");
//     let input_g = wrapMathJax(document.getElementById('g_input_value').value.trim(), "g");

//     //  Disable the display and render buttons until MathJax is done
//     let display_f = document.getElementById("f_input_value");
//     let display_g = document.getElementById("g_input_value");
//     let button_f = document.getElementById("calculate_button");
//     let button_g = document.getElementById("calculate_button");
//     button_f.disabled = display_f.disabled = true;

//     // Output for function1
//     let output_f = document.getElementById('function1');
//     output_f.innerHTML = '';
//     MathJax.texReset();
//     let options_f = MathJax.getMetricsFor(output_f);
    
//     MathJax.tex2chtmlPromise(input_f, options_f).then(function (node) {
//       output_f.appendChild(node);
//       MathJax.startup.document.clear();
//       MathJax.startup.document.updateDocument();
//     }).catch(function (err) {
//       output_f.appendChild(document.createElement('pre')).appendChild(document.createTextNode(err.message));
//     }).then(function () {
//       button_f.disabled = display_f.disabled = false;
//     });

    
//     // Output for function2
//     let output_g = document.getElementById('function2');
//     output_g.innerHTML = '';
//     MathJax.texReset();
//     let options_g = MathJax.getMetricsFor(output_f);

//     MathJax.tex2chtmlPromise(input_g, options_g).then(function (node) {
//         output_g.appendChild(node);
//         MathJax.startup.document.clear();
//         MathJax.startup.document.updateDocument();
//       }).catch(function (err) {
//         output_g.appendChild(document.createElement('pre')).appendChild(document.createTextNode(err.message));
//       }).then(function () {
//         button_g.disabled = display_g.disabled = false;
//       });
//   }
