import os
import sys
import pathlib
import textwrap
from PIL import Image
import streamlit as st
from src.logger import logging
from src.exception import CustomException


def input_image_setup(upload_image):
    """
    Processes an uploaded image to prepare it for use with the Gemini model.

    Args:
        upload_image (Any): The uploaded image data, typically from a web framework's request object.

    Returns:
        list: A list containing a dictionary with the image's mime type and data.
               If no image is uploaded, raises a FileNotFoundError.

    Raises:
        FileNotFoundError: If no image is uploaded.
        Exception: For any other unexpected errors.
    """
    logging.info("Processing uploaded image...")
    try:
        # Check if a file has been uploaded
        if upload_image is not None:

            #Read the file has been uploaded
            bytes_data = upload_image.getvalues()

            # Prepare the image information
            image_paths = [
                {
                    "mime_type": upload_image.type, #Get the mime type of the uploaded file
                    "data": bytes_data, #Get the data of the uploaded file
                }
            ]

            return image_paths
        else:
            raise FileNotFoundError("No File Uploaded")
        
    except Exception as e:
        logging.info("Error Occured while inputing image")
        raise CustomException(e,sys)

