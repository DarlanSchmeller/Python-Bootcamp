import requests
import bs4

html_data = requests.get("https://pt.wikipedia.org/wiki/Deep_Blue")

soup = bs4.BeautifulSoup(html_data.text, "lxml")
found_images_list = soup.select(".mw-file-element")

for image in found_images_list:
    print(image["src"])     # Since it's a list like object, we can access only the items we want by passing this parameter
    
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg")


# Images are just binary for the computer, since the request raw content is binary, and we can access it, we can also write this binary into a file to save the image into our computer 
with open('new_image.jpg', 'wb') as f:      # We use the WB file mode, which stands for WRITING BINARY, this allows us to write the image data directly into a file
    f.write(image_link.content)