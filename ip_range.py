import ipaddress

def print_ip_range_to_file():
    while True:
        # Prompt user for the starting subnet
        ip_subnet = input("Enter the starting subnet in CIDR notation (e.g., 192.168.1.0/24) or type 'quit' to exit: ")

        if ip_subnet.lower() == 'quit':
            print("Exiting the program.")
            break

        try:
            # Parse the input IP subnet
            network = ipaddress.IPv4Network(ip_subnet, strict=False)

            # Generate filename from the IP range
            filename = "_".join(str(network.network_address).split('.')) + ".txt"

            # Print all the IPs in the range to the file (excluding IPs ending in 0)
            with open(filename, "w") as output_file:
                output_file.write(f"IPs in the range {ip_subnet} (excluding IPs ending in 0):\n")
                for ip in network:
                    if str(ip).endswith('.0'):
                        continue
                    output_file.write(str(ip) + "\n")

            print(f"IPs in the range (excluding IPs ending in 0) have been written to {filename}")

        except ipaddress.AddressValueError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    print_ip_range_to_file()
