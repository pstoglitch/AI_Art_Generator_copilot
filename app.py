import os
import base64
import streamlit as st
from openai import OpenAI
from openai.error import OpenAIError

st.set_page_config(
    page_title="AI Art Inspiration Generator",
    page_icon="🎨",
    layout="wide",
)

ART_STYLE_DETAILS = {
    "Mandala": (
        "Circle symmetry, sacred geometry, radial patterns, concentric layers, and meditation-inspired design."
    ),
    "Gond Art": (
        "Traditional Indian tribal art with nature storytelling, animals, birds, plants, fine repetitive patterns, and dot decorations."
    ),
    "Madhubani Art": (
        "Mithila painting style with bold outlines, decorative borders, floral motifs, and traditional Indian symbols."
    ),
    "Warli Art": (
        "Tribal storytelling scenes of village life, human and nature figures, and simple geometric patterns."
    ),
    "Contemporary Digital Art": (
        "Modern illustration with creative digital composition, polished style, and professional visual presentation."
    ),
}

COLOR_THEME_DETAILS = {
    "Vibrant Colors": "Bright and energetic colors that create a joyful and powerful mood.",
    "Pastel Colors": "Soft and gentle tones that feel calm, soothing, and delicate.",
    "Earthy Natural Colors": "Warm natural shades inspired by soil, leaves, wood, and nature.",
    "Traditional Indian Colors": "Rich Indian color palette with saffron, deep blues, greens, and gold tones.",
    "Monochrome Black and White": "Strong black and white contrast for elegant and timeless artwork.",
}

COMPLEXITY_DESCRIPTIONS = {
    "Beginner Friendly": "Simple patterns, clear shapes, and easy-to-understand design.",
    "Medium Detail": "Balanced complexity with detailed patterns and more artistic elements.",
    "Highly Intricate": "Complex patterns, fine details, and a professional artwork style.",
}


def build_image_prompt(theme: str, style: str, color_theme: str, complexity: str) -> str:
    theme = theme.strip()
    style_description = ART_STYLE_DETAILS.get(style, "Beautiful artistic style.")
    color_description = COLOR_THEME_DETAILS.get(color_theme, "A strong color palette.")
    complexity_description = COMPLEXITY_DESCRIPTIONS.get(complexity, "A polished art level.")

    prompt = (
        f"Create a high-quality professional artwork inspired by the idea '{theme}'. "
        f"Use the {style} style with {style_description} "
        f"Apply {color_theme} theme with {color_description} "
        f"and produce a {complexity.lower()} design with {complexity_description} "
        "The art should show strong visual storytelling, balanced composition, and a clean design. "
        "Do not include any text, letters, numbers, logos, or watermarks. "
        "The final image should look polished, vibrant, and ready for inspiration."
    )
    return prompt


def generate_image(prompt: str, api_key: str) -> bytes:
    if not api_key:
        raise ValueError("Missing OpenAI API key.")

    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",
    )

    image_base64 = response.data[0].b64_json
    return base64.b64decode(image_base64)


def main():
    st.title("🎨 AI Art Inspiration Generator")
    st.markdown(
        "Create beautiful AI-generated artwork using a theme, style, color palette, and complexity level. "
        "This beginner-friendly app builds an image prompt automatically and shows the result instantly."
    )

    st.markdown("---")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.warning(
            "To create images, you need an OpenAI API key. "
            "Set the key in your environment as OPENAI_API_KEY."
        )
        st.info(
            "Example: export OPENAI_API_KEY='your_api_key_here' on macOS or Linux. "
            "On Windows PowerShell, use: $env:OPENAI_API_KEY='your_api_key_here'."
        )

    with st.form(key="art_form"):
        col1, col2 = st.columns(2)

        with col1:
            inspiration_theme = st.text_input(
                "Inspiration Theme",
                placeholder="Peace, Nature, Harmony, Growth, Ocean, Village Life, Happiness",
                help="Type a single word or short phrase that describes the mood you want the art to show.",
            )
            art_style = st.selectbox(
                "Art Style",
                options=list(ART_STYLE_DETAILS.keys()),
                help="Choose an art style that matches the mood and detail you want.",
            )
            st.caption(ART_STYLE_DETAILS[art_style])

        with col2:
            color_theme = st.selectbox(
                "Colour Theme",
                options=list(COLOR_THEME_DETAILS.keys()),
                help="Choose the color palette that best fits the artwork mood.",
            )
            st.caption(COLOR_THEME_DETAILS[color_theme])

            complexity = st.selectbox(
                "Complexity",
                options=list(COMPLEXITY_DESCRIPTIONS.keys()),
                help="Select how detailed and intricate the final image should be.",
            )
            st.caption(COMPLEXITY_DESCRIPTIONS[complexity])

        submit_button = st.form_submit_button("Generate Artwork 🎨")

    if submit_button:
        if not inspiration_theme:
            st.error("Please enter an inspiration theme before generating artwork.")
            return
        if not api_key:
            st.error("OpenAI API key is missing. Please set OPENAI_API_KEY and try again.")
            return

        prompt = build_image_prompt(
            theme=inspiration_theme,
            style=art_style,
            color_theme=color_theme,
            complexity=complexity,
        )

        st.subheader("Prompt Preview")
        st.write(prompt)

        try:
            with st.spinner("Generating your artwork... this may take a few seconds."):
                image_bytes = generate_image(prompt=prompt, api_key=api_key)

            st.success("Your AI art is ready!")
            st.image(image_bytes, caption="Generated AI Art", use_column_width=True)
            st.download_button(
                label="Download Image",
                data=image_bytes,
                file_name="ai_art_inspiration.png",
                mime="image/png",
            )
        except OpenAIError as error:
            st.error(
                "There was a problem generating the image with OpenAI. "
                f"Please check your API key and try again. Error: {error}"
            )
        except ValueError as error:
            st.error(str(error))
        except Exception as error:
            st.error(
                "An unexpected error happened while generating the image. "
                f"Please try again or check your settings. Error: {error}"
            )

    st.markdown("---")
    st.markdown(
        "**Tip:** Try using words like `Peace`, `Nature`, `Harmony`, `Growth`, `Ocean`, `Village Life`, or `Happiness` to generate different moods. "
        "Combine those words with the art style and color theme to explore new looks."
    )


if __name__ == "__main__":
    main()
