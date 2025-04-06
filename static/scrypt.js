function show_files(target){
    const selectedFiles = document.getElementById('selected-files');
    const files = target.files;
    selectedFiles.innerHTML = '';

    for(const file of files){
        const fileName = file.name;
        const fileItem = document.createElement('p');
        fileItem.textContent = fileName;
        selectedFiles.appendChild(fileItem);
    }
}