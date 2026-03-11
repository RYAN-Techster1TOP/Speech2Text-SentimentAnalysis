// Show selected filename

document.querySelector("input[type=file]").addEventListener("change", function(){

    const label = document.querySelector(".file-upload span");

    if(this.files.length > 0){
        label.innerText = "🎧 " + this.files[0].name;
    }

});


// Button loading animation

document.getElementById("uploadForm").addEventListener("submit", function(){

    const btn = document.querySelector(".analyze-btn");

    btn.innerHTML = "Analyzing...";
    btn.style.background = "#888";

});