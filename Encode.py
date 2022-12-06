# Encode script
import os
import sys

def encode_file(input_file, output_file, compression_level=5):
    # Open the input and output files
    with open(input_file, "rb") as input_f, open(output_file, "wb") as output_f:
        # Set the compression level
        compressor = zlib.compressobj(compression_level)

        # Read the input file in chunks
        chunk = input_f.read(1024)
        while chunk:
            # Compress the chunk and write it to the output file
            compressed_chunk = compressor.compress(chunk)
            output_f.write(compressed_chunk)

            # Read the next chunk
            chunk = input_f.read(1024)

        # Write any remaining compressed data to the output file
        remaining_data = compressor.flush()
        output_f.write(remaining_data)

# Main function
def main(argv):
    if len(argv) != 3:
        print("Usage: encode.py input_file output_file")
        sys.exit(1)

    input_file = argv[1]
    output_file = argv[2]

    if not os.path.exists(input_file):
        print("Error: input file does not exist")
        sys.exit(1)

    encode_file(input_file, output_file)

# Run the main function if the script is executed
if __name__ == "__main__":
    main(sys.argv)

