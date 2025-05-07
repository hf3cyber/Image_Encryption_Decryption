# Pixel Swapping Image Encryption & Decryption

## 📌 Overview

This Python script encrypts and decrypts images by swapping pixel positions based on a user-provided seed. It provides a simple yet effective way to scramble images for obfuscation.

# 🚀 Features

Encrypts an image by randomly shuffling pixels.

Decrypts an encrypted image using the same seed.

Uses a reproducible shuffle algorithm for consistent results.

Command-line interface for user-friendly interaction.

# 🛠️ Requirements

Ensure you have Python installed along with the required library:

```
pip install pillow
```

## 📜 Usage

Run the script and follow the interactive menu:

```
python PixelSwapping.py
```

## Menu Options
```
1️⃣ Encrypt an image - Provide an image file path and a seed to scramble the pixels.
2️⃣ Decrypt an image - Use the same seed to restore the original image.
3️⃣ Encrypt and then decrypt - Perform both actions in sequence.
4️⃣ Exit - Close the program.
```


##Example Usage
```
Enter the input image file path: input.jpg
Enter a seed (integer) for encryption/decryption: 1234
```

# 🖥️ How to Use in Kali Linux

Kali Linux comes with Python pre-installed. Follow these steps to use the script:

## 1️⃣ Install Dependencies

```
sudo apt update && sudo apt install python3-pip -y
```
```
pip3 install pillow
```

## 2️⃣ Clone the Repository

```
https://github.com/hf3cyber/Image_Encryption_Decryption.git
```
```
cd Image_Encryption_Decryption
```

## 3️⃣ Create a Python Virtual Environment (Recommended)

It is recommended to use a virtual environment to keep dependencies isolated.

```
python3 -m venv venv
   source venv/bin/activate
   pip install pillow
```

## 4️⃣ Run the Script

```
python3 PixelSwapping.py
```

### 🔹 Improvements & Enhancements

Maintains the original image format (avoiding JPEG compression issues).

Allows users to specify output filenames.

Handles non-integer seed input gracefully.

Supports different image modes (RGB, RGBA, Grayscale).

Uses NumPy for optimized performance in pixel operations.

### 📧 Contact

For questions or improvements, feel free to contribute or open an issue in the repository!

## 👤 Author

GitHub: @hf3cyber

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


