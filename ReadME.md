<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Cryptography</title>
    <link rel="icon" href="./assets/icons/rubik.ico" type="image/x-icon">
    <link rel="stylesheet" href="./css/style.css"/>
    <link rel="stylesheet" href="https://pyscript.net/releases/2023.11.1/core.css" />
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Header section -->
    <header style="background-color: rgb(123 237 131);" class="heading">
        <div class="row-container">
            <img src="./assets/icons/rubik.ico" alt="Rubik's Icon" width="50px" height="50px"/>
            <h1><a href="https://www.hindawi.com/journals/jece/2012/173931/" target="_blank">Image Cryptography</a></h1>
            <img src="./assets/icons/rubik.ico" alt="Rubik's Icon" width="50px" height="50px"/>
        </div>
        
    </header>
    
    <!-- Navigation bar for encryption & decryption -->
    <nav class="navbar">
        <div class="row-container">
            <button class="button" id="encrypt-nav-item">Encryption</button>
            <button class="button" id="decrypt-nav-item">Decryption</button>
        </div>
    </nav>

    <!-- Main content area -->
    <div class="grid-container">
        <h2 class="grid-item input-img-heading">Input Image</h2>
        <h2 class="grid-item output-img-heading">Output Image</h2>
        <button id="transform-img-btn" class="grid-item action-btn button">Encrypt</button>
        <img class="grid-item input-img" id="input-img" src="./assets/imgs/placeholder.png" alt="Input Image">
        <img class="grid-item output-img" id="output-img" src="./assets/imgs/placeholder.png" alt="Output Image">
        <div class="grid-item img-uploader" id="img-uploader">
            <button id="img-uploader-btn" class="button">Upload Image</button>
            <input type="file" accept=".png" id="img-input" onchange="previewImage(event, 'input-img')" style="display: none;">
        </div>
        <div style="display: none;" class="grid-item img-key-uploader" id="img-key-uploader">
            <button id="encrypted-img-uploader-btn" class="button">Upload Image</button>
            <button id="key-uploader-btn" class="button">Upload Key</button>
            <input type="file" id="encrypted-img-input" style="display: none;" accept=".png" onchange="previewImage(event, 'input-img')">
            <input type="file" id="key-input" style="display: none;" accept=".txt" onchange="previewText(event, 'crypto-key')">
        </div>
        <div class="grid-item download-btns" id="img-key-downloader">
            <button class="button" onclick="downloadKey('crypto-key', 'key.txt')">Download Key</button>
            <button class="button" onclick="downloadImage('output-img', 'modified.png')">Download Image</button>
        </div>
    </div>
    <div style="display: none;" id="crypto-key"></div>
    <hr/>

    <script src="https://pyscript.net/releases/2023.11.1/core.js"></script>
    <script src="./js/script.js"></script>
    <script type="py" src="./pyscript/image_crypto.py" config="./pyscript/pyscript.toml"></script>


</html>

  
