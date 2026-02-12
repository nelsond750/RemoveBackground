const imageInput = document.getElementById("imageIpunt");
const removeBtn = document.getElementById("removebtn");
const resultImage = document.getElementById("resultImage");
const downloadLink = document.getElementById("downloadLink");

removeBtn.addEventListener("click", async() =>{
    const file = imageInput.files[0]

    if(!file){
        return;
    }
    const formaData = new FormData();
    formaData.append("file", file);

    const response = await fetch("https://localhost:8000/remover-bg", {
        method: "POST",
        body:FormData,    
    });


const blob = await response.blob();
const imageUrl = URL.createObjectURL(blob);
resultImage.src = imageUrl;
downloadLink.href = imageUrl;
downloadLink.style.display = "inline";
});