# Import the necessary libraries
import qrcode  # For generating QR codes
from PIL import Image  # For working with images

# Define the data for the QR code (e.g., a URL)
data = "https://twitter.com/AshmitaKun721"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Create a QRCode object
qr.add_data(data)  # Add the data to the QR code
qr.make(fit=True)  # Generate the QR code based on the data

# Create an image from the QR code
fill_color = "black"  # Set the color of the QR code modules
back_color = "white"  # Set the background color
image = qr.make_image(fill_color=fill_color, back_color=back_color)  # Create the image

# Save the image
image.save("qr_code.png")  # Save the image as a PNG file

# Display the generated QR code image
image.show()  # Open the image using the default image viewer
