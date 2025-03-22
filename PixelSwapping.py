from PIL import Image
import random

def swap_pixels(pixels, swap_map):
    """Swaps pixels based on the provided swap map."""
    return [pixels[i] for i in swap_map]

def generate_swap_map(size, seed):
    """Generates a swap map based on the image size and a seed."""
    random.seed(seed)
    swap_map = list(range(size))
    random.shuffle(swap_map)
    return swap_map

def encrypt_image(input_image_path, output_image_path, seed):
    """Encrypts an image by swapping its pixels."""
    try:
        image = Image.open(input_image_path)
        pixels = list(image.getdata())
        swap_map = generate_swap_map(len(pixels), seed)
        encrypted_pixels = swap_pixels(pixels, swap_map)
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save(output_image_path)
        print(f"✅ Image encrypted and saved as {output_image_path}")
        return swap_map  # Return swap map for decryption
    except Exception as e:
        print(f"❌ Error: {e}")

def decrypt_image(input_image_path, output_image_path, swap_map):
    """Decrypts an image by reversing the pixel swap."""
    try:
        image = Image.open(input_image_path)
        encrypted_pixels = list(image.getdata())
        reverse_swap_map = sorted(range(len(swap_map)), key=lambda x: swap_map[x])
        decrypted_pixels = swap_pixels(encrypted_pixels, reverse_swap_map)
        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_image_path)
        print(f"✅ Image decrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n📌 Choose an option:")
    print("1️⃣ Encrypt an image")
    print("2️⃣ Decrypt an image")
    print("3️⃣ Encrypt and then decrypt")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    input_image_path = input("Enter the input image path: ").strip()
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.jpg"

    if choice == "1":
        seed = int(input("Enter a seed (integer): "))
        encrypt_image(input_image_path, encrypted_image_path, seed)
    
    elif choice == "2":
        seed = int(input("Enter the seed used for encryption: "))
        swap_map = generate_swap_map(len(Image.open(input_image_path).getdata()), seed)
        decrypt_image(input_image_path, decrypted_image_path, swap_map)
    
    elif choice == "3":
        seed = int(input("Enter a seed (integer): "))
        swap_map = encrypt_image(input_image_path, encrypted_image_path, seed)
        decrypt_image(encrypted_image_path, decrypted_image_path, swap_map)
    
    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
