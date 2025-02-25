#!/bin/bash

# Prompt the user for the word
read -p "Enter the word (include special characters if needed): " word

# Prompt the user for the output filename
read -p "Enter the output filename (without extension): " filename

# Create the output file path
output_file="$HOME/Tools/$filename.txt"

# Generate all case combinations including special characters and their variations
function generate_case_combinations {
    local input="$1"
    local output=()
    local length=${#input}

    # Generate combinations using bit manipulation
    for ((i=0; i < (1 << length); i++)); do
        local combination=""
        for ((j=0; j < length; j++)); do
            char="${input:j:1}"
            if (( (i & (1 << j)) )); then
                combination+="${char^^}"  # Uppercase
            else
                combination+="${char,,}"  # Lowercase
            fi
        done
        output+=("$combination")
    done

    # Add variations for special characters
    for variant in "${output[@]}"; do
        # Example: Replace '!' with '@' and '#' with '$'
        echo "$variant" >> "$output_file"  # Save the original case combination
        variant="${variant//!/@}"  # Replace '!' with '@'
        variant="${variant//#/\$}"  # Replace '#' with '$'
        echo "$variant" >> "$output_file"  # Save the modified variant
    done
}

# Call the function to generate combinations
generate_case_combinations "$word"

# Inform the user
echo "Wordlist saved to $output_file"
