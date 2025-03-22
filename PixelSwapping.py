from PIL import Image
import random
import os

def swap_pixels(pixels, swap_map):
    """Rearrange pixels based on the swap map."""
    return [pixels[i] for i in swap_map]

def generate_swap_map(size, seed):
    """Generate a reproducible swap map based on a given seed."""
    random.seed(seed)
    swap_map = list(range(size))
    random.shuffle(swap_map)
    return swap_map

def encrypt_image(input_path, output_path, seed):
    """Encrypt an image by swapping its pixels."""
    try:
        image = Image.open(input_path)
        pixels = list(image.getdata())
        swap_map = generate_swap_map(len(pixels), seed)
        encrypted_pixels = swap_pixels(pixels, swap_map)

        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save(output_path)

        print(f"✅ Encryption successful! Encrypted image saved as: {output_path}")
        return swap_map
    except Exception as e:
        print(f"❌ Error during encryption: {e}")

def decrypt_image(input_path, output_path, seed):
    """Decrypt an image by reversing the pixel swaps."""
    try:
        image = Image.open(input_path)
        encrypted_pixels = list(image.getdata())
        swap_map = generate_swap_map(len(encrypted_pixels), seed)

        reverse_swap_map = sorted(range(len(swap_map)), key=lambda x: swap_map[x])
        decrypted_pixels = swap_pixels(encrypted_pixels, reverse_swap_map)

        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_path)

        print(f"✅ Decryption successful! Decrypted image saved as: {output_path}")
    except Exception as e:
        print(f"❌ Error during decryption: {e}")

def main():
    """Main menu for user interaction."""
    print("\n🔐 IMAGE ENCRYPTION & DECRYPTION TOOL")
    print("1️⃣ Encrypt an image")
    print("2️⃣ Decrypt an image")
    print("3️⃣ Encrypt and then decrypt")
    print("4️⃣ Exit")

    choice = input("\nEnter your choice (1/2/3/4): ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice! Please enter a valid option.")
        return

    if choice == "4":
        print("👋 Exiting... Have a great day!")
        return

    input_path = input("Enter the input image file path: ").strip()
    
    if not os.path.exists(input_path):
        print("❌ Error: File not found. Please provide a valid image path.")
        return

    seed = int(input("Enter a seed (integer) for encryption/decryption: "))

    encrypted_path = "encrypted_image.png"
    decrypted_path = "decrypted_image.jpg"

    if choice == "1":
        encrypt_image(input_path, encrypted_path, seed)

    elif choice == "2":
        decrypt_image(input_path, decrypted_path, seed)

    elif choice == "3":
        encrypt_image(input_path, encrypted_path, seed)
        decrypt_image(encrypted_path, decrypted_path, seed)

if __name__ == "__main__":
    main()
