# AI Art Inspiration Generator

A beginner-friendly Streamlit application that creates AI-powered art ideas and images using OpenAI's image generation API.

## Project structure

```
AI_Art_Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation steps

1. Install Python 3.10 or newer.
2. Open a terminal or command prompt.
3. Navigate to the project folder:

```bash
cd /Users/pallavisinghal/Downloads/AI_Art_Generator
```

4. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

5. Set your OpenAI API key in your environment.

On macOS or Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

## How to run the application

Run the Streamlit app from the terminal:

```bash
streamlit run app.py
```

This will open a local browser window or show a local URL such as `http://localhost:8501`.

## What the app does

- Lets you type an inspiration theme.
- Lets you choose an art style.
- Lets you choose a colour theme.
- Lets you choose a complexity level.
- Builds a detailed AI prompt automatically.
- Sends the prompt to OpenAI's `gpt-image-1` model.
- Displays the generated 1024x1024 image.
- Lets you download the image as a PNG file.

## Common errors and solutions

- `Missing OpenAI API key`: Make sure you set `OPENAI_API_KEY` in your terminal before running the app.
- `Please enter an inspiration theme`: Type a theme such as `Peace` or `Nature` in the input field.
- `Invalid API key`: Check your OpenAI key and make sure it is copied correctly.
- `API errors or image generation errors`: Wait a moment and try again, or verify your internet connection.

## Ideas for future improvements

- Add a second image size option like 512x512 or 2048x2048.
- Add more art styles or custom user style descriptions.
- Save generated prompts to a history panel.
- Let users preview the prompt before sending it to the API.
- Add a gallery page to compare multiple generated artworks.
