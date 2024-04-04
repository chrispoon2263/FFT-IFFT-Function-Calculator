// Register Event Handlers Upon loading webpage
window.addEventListener("DOMContentLoaded", loadHandler)

// Load Handler
function loadHandler(){
    document.getElementById('randomize_button').addEventListener('click', random_button_handler);
}

// Random button Handler
function random_button_handler() {
    let f_input = document.getElementById("f_input_value");
    let g_input = document.getElementById("g_input_value");
        fetch('/proxyEndpoint')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            f_input.value = data['input_1']
            g_input.value = data['input_2']
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

