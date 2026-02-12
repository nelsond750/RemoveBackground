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

    const response = await fetch("https://console.cloud.google.com/run/services?project=background-remover-487110", {
        method: "POST",
        body:FormData,    
    });


const blob = await response.blob();
const imageUrl = URL.createObjectURL(blob);
resultImage.src = imageUrl;
downloadLink.href = imageUrl;
downloadLink.style.display = "inline";
});