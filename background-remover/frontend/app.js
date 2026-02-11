const imageInput = document.getElementById("imgeIpunt");
const removeBtn = document.getElementById("removebtn");
const resuktImage = document.getElementById("resultImage");
const downloadLink = document.getElementById("downloadLink");

removeBtn.addEventListener("click", async() =>{
    const file = imageInput.file[0]

    if(!file){
        return;
    }
    const formaDtat = new FormData();
    formaData.append("file", file);

    const response = await fetch("https://localhost:8000/remover-bg" {
    method: "POST",
    body:FormData,    
    });


const blob = await response.blob();
const imageUrl = URL.createObjectURL(blob);
resuktImage.src = imageUrl;
downloadLink.href = imageUrl;
downloadLink.style.display = "inline";
});