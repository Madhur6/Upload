# Upload App

This Django app allows you to upload PDF files, extract text using OCR, and display the extracted text in a user-friendly manner.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Upload.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Upload
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the app.

## Usage

1. Upload PDF files on the home page.
2. Click on the "Extract" button to perform OCR on the uploaded files.
3. View the extracted text and download the CSV file.

## Project Structure

- `core`: Django app folder containing the main functionalities.
- `media`: Folder to store uploaded files and extracted images.

## Dependencies

- [Django](https://www.djangoproject.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Pillow](https://pillow.readthedocs.io/)
- [easyocr](https://github.com/JaidedAI/EasyOCR)

## Credits

- [Bootstrap](https://getbootstrap.com/): Used for styling the frontend.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

