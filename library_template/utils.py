import requests
from django.conf import settings
from google_images_search import GoogleImagesSearch
import random
import os
from django.core.files import File
from django.utils.text import slugify

def fetch_random_image(query):
    gis = GoogleImagesSearch(settings.GOOGLE_API_KEY, settings.GOOGLE_CSE_ID)
    search_params = {'q': query, 'num': 10, 'safe': 'high'}

    # Search for images with the given query
    gis.search(search_params)

    # Get a random image from the search results
    image_url = random.choice(gis.results()).url

    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        # Extract the content-type from the response headers
        content_type = response.headers.get('content-type')

        # Generate a unique image file name using slugify
        image_file_name = slugify(query)[:100] + '.' + content_type.split('/')[-1]

        # Create the temporary file path
        temp_file_path = os.path.join(settings.MEDIA_ROOT, 'temp', image_file_name)

        # Create the temp directory if it doesn't exist
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)

        # Save the image file to the temporary path
        with open(temp_file_path, 'wb') as f:
            f.write(response.content)

        # Open the temporary file
        with open(temp_file_path, 'rb') as f:
            # Create a Django File object from the temporary file
            django_file = File(f)

            # Save the Django File object to the media folder
            save_path = os.path.join('articles_images', image_file_name)
            saved_file_path = os.path.join(settings.MEDIA_ROOT, save_path)
            django_file.name = save_path
            with open(saved_file_path, 'wb') as saved_file:
                saved_file.write(django_file.read())

        # Remove the temporary file
        os.remove(temp_file_path)

        return saved_file_path

    return None
