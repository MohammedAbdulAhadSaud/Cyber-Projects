import hashlib

# Function to hash a given PIN using SHA-256
def hash_pin(pin):
    """Hashes a 6-digit PIN using SHA-256."""
    return hashlib.sha256(pin.encode('utf-8')).hexdigest()

# Function to brute-force the PIN
def brute_force_crack(hashed_pin,n):
    """Brute-force attack to crack a 6-digit PIN hash."""
    # Loop through all possible n-digit PIN combinations (000000 to 999999)
    for pin in range(1000000):
        # Format the pin to be n digits with leading zeros
        pin_str = str(pin).zfill(n)
        
        # Hash the PIN
        hashed_attempt = hash_pin(pin_str)
        
        # Check if the hash matches the target hash
        if hashed_attempt == hashed_pin:
            print(f"Password cracked! The original PIN is: {pin_str}")
            return pin_str  # Return the cracked PIN
    
    print("Could not crack the PIN with brute force.")
    return None

    
def main():
    # Get the hashed PIN from the user
    n=int(input("Enter the n-digits of PIN : "))
    
    hashed_pin = input(f"Enter the SHA-256 hashed {n}-digit PIN to crack: ").strip()
    #hashed_pin = hashed_prompt
    # Attempt to crack the PIN
    cracked_pin = brute_force_crack(hashed_pin,n)

    if cracked_pin:
        print(f"Successfully cracked the PIN: {cracked_pin}")
    else:
        print("Failed to crack the PIN.")

if __name__ == "__main__":
    main()
    
    
  
