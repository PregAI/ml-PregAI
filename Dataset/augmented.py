import os
import cv2
import random

def flip_images(input_folder, output_folder, num_images_to_flip):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Choose a random subset of image files
    random.seed(42)  # Set a specific seed for reproducibility
    images_to_flip = random.sample(image_files, min(num_images_to_flip, len(image_files)))

    for image_file in images_to_flip:
        # Read the image
        image_path = os.path.join(input_folder, image_file)

        # Add print statements for debugging
        print(f"Processing image: {image_path}")

        img = cv2.imread(image_path)

        # Check if the image is loaded successfully
        if img is None:
            print(f"Error loading image: {image_path}")
            continue

        # Flip the image horizontally
        flipped_img = cv2.flip(img, 1)

        # Generate the output file path
        output_path = os.path.join(output_folder, f"flip_{image_file}")

        # Save the flipped image
        cv2.imwrite(output_path, flipped_img)

if __name__ == "__main__":
    # Specify your input and output folders
    input_folder_path = "yoga-9/Warrior Pose"
    output_folder_path = "yoga-9/Warrior Pose Flip"
    num_images_to_flip = 5

    # Call the function to flip randomly selected images
    flip_images(input_folder_path, output_folder_path, num_images_to_flip)
