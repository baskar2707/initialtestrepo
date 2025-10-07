import os
import argparse
from datetime import datetime

def generate_file(output_dir, file_size_mb, index):
    """Creates a file with specified size of random data."""
    file_path = os.path.join(output_dir, f"data_{index}.bin")
    with open(file_path, "wb") as f:
        f.write(os.urandom(file_size_mb * 1024 * 1024))  # Write file_size_mb of random data
    print(f"✅ Created file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate data files periodically.")
    parser.add_argument("-d", "--directory", required=True, help="Base output directory to store files")
    parser.add_argument("-s", "--size", type=int, required=True, help="File size in MB")
    parser.add_argument("-f", "--filescount", type=int, required=True, help="Files count")
    
    args = parser.parse_args()
    base_output_dir = args.directory
    file_size_mb = args.size
    no_of_files = args.filescount

    os.makedirs(base_output_dir, exist_ok=True)  # Ensure the base directory exists

   
    # Create a new directory with a timestamp for each run
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join(base_output_dir, f"run_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)

    for i in range(no_of_files):
        # Create a new directory with a timestamp for each run
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = os.path.join(base_output_dir, f"run_{timestamp}")
        os.makedirs(output_dir, exist_ok=True)

        # Generate file in the newly created directory
        generate_file(output_dir, file_size_mb, i)

    print("✅ Script completed! Files generated.")

if __name__ == "__main__":
    main()
