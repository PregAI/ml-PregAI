import os
import urllib.request

def download_images_from_file(file_path, output_folder):
    try:
        os.makedirs(output_folder)
    except FileExistsError:
        pass

    # Add a user-agent to mimic a web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                image_path = parts[0]
                image_url = parts[1]

                image_name = os.path.basename(image_path)  # Extracting image name from the path
                output_path = os.path.join(output_folder, image_name)

                try:
                    # Create a request object with headers
                    request = urllib.request.Request(image_url, headers=headers)
                    with urllib.request.urlopen(request) as response, open(output_path, 'wb') as out_file:
                        out_file.write(response.read())
                    print(f"Downloaded: {image_name}")
                except Exception as e:
                    print(f"Error downloading {image_name}: {e}")

if __name__ == "__main__":

    """

    # ===== donwload for all txt file =====

    # Set the path to the folder containing text files and the root output folder
    text_files_folder = "./Dataset raw/Yoga-82/yoga_dataset_links"
    root_output_folder = "./Dataset raw/Yoga-82/Downloaded_Images"

    # Iterate over text files and download images
    for filename in os.listdir(text_files_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(text_files_folder, filename)
            output_folder = os.path.join(root_output_folder, os.path.splitext(filename)[0])
            download_images_from_file(file_path, output_folder)

    """

    # ===== donwload for specific txt file =====

    # Set the path to the specific text file and the output folder
    specific_file_path = "./Dataset raw/Yoga-82/yoga_dataset_links/Four-Limbed_Staff_Pose_or_Chaturanga_Dandasana_.txt"
    root_output_folder = "./Dataset raw/Yoga-82/Downloaded_dataset/Four-Limbed_Staff_Pose_or_Chaturanga_Dandasana_"

    # Extract filename from the path
    filename = os.path.splitext(os.path.basename(specific_file_path))[0]

    # Set the output folder based on the filename
    output_folder = os.path.join(root_output_folder, filename)

    # Download images from the specific text file
    download_images_from_file(specific_file_path, output_folder)
