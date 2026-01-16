# Wine Tasting Card Generator

Generate wine tasting cards in PDF format with multiple design styles.

## Overview

This project provides Python scripts that generate customizable wine tasting cards following common wine tasting certifications and industry standards. Each script produces a different visual style. 

I know you could have generated it with AI, but it would take some back-and-forth prompting to achieve the result. So, simply feed this layout into your LLM instead to save some time!

## Card Features

All tasting cards include standard professional criteria:

- **Visual Section**: Clarity, intensity, and color/hue assessment
- **Smell Section**: Condition, intensity, aroma characteristics, and evolution
- **Taste Section**: Sweetness, tartness/acidity, tannins, alcohol, body, texture, flavor intensity, and finish
- **Verdict Section**: Quality rating and readiness for drinking
- **Aroma Box**: Comprehensive reference guide grouping aromas by category (Fruit/Floral, Winemaking, Maturation)
- **Notes Box**: Space for additional observations and pairings

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the repository**
   ```bash
   cd wine-project
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download custom fonts**
   ```bash
   python setup_fonts.py
   ```
   This will download the Patrick Hand handwritten and GreatVibes fonts.

## Usage

To generate a tasting card, run the desired script:

```bash
# Activate virtual environment first
source venv/bin/activate

# Generate sketchy style card
python generate_wine_tasting_sheet_sketchy.py

# Generate vintage style card with elegant ink aesthetic
python generate_wine_tasting_sheet_vintage.py

# Generate handwritten style card with Patrick Hand font
python generate_wine_tasting_sheet_handwritten.py
```

Each script will generate a PDF file in the project directory. My favorite is the handwritten one, and I find the vintage one visually heavy, but who cares about my personal preference. Feel free to customize the scripts to fit your taste! 🎨

### Available Scripts

- **`generate_wine_tasting_sheet_sketchy.py`** - Hand-drawn aesthetic with sketchy lines
- **`generate_wine_tasting_sheet_vintage.py`** - Classic, elegant design with vintage aesthetics and procedural paper texture
- **`generate_wine_tasting_sheet_handwritten.py`** - Clean design using Patrick Hand custom handwritten font

## Customization

### Colors

You can customize the color palette by editing the color definitions in any script:

```python
wine_red = Color(0.45, 0.1, 0.15)  # Deep wine red
dark_grey = Color(0.2, 0.2, 0.2)   # Text color
light_grey = Color(0.7, 0.7, 0.7)  # Lines and subtle elements
```

Colors are defined using RGB values (0.0 to 1.0 range).

### Fonts

- **Sketchy style** uses Courier font for a "raw/draft" look
- **Vintage style** uses GreatVibes custom font for an elegant ink aesthetic
- **Handwritten style** uses Patrick Hand custom handwritten font for a casual appearance

To change fonts in any script, modify the font definitions:

```python
header_font = "Times-Bold"
body_font = "Helvetica"
```

### Layout and Spacing

Adjust margins, column widths, and spacing by modifying the layout constants:

```python
left_margin = 30
right_margin = width - 30
main_content_right = width * 0.57
```

### Aroma Categories

The Aroma Box content can be customized by editing the `aroma_data` or similar data structure in the script. Each style may organize aromas slightly differently.

## File Structure

```
wine-project/
├── README.md
├── requirements.txt
├── setup_fonts.py
├── PatrickHand.ttf (downloaded via setup_fonts.py)
├── GreatVibes-Regular.ttf (downloaded via setup_fonts.py)
├── .gitignore
├── generate_wine_tasting_sheet_sketchy.py
├── generate_wine_tasting_sheet_vintage.py
├── generate_wine_tasting_sheet_handwritten.py
└── PDF outputs/
    ├── Generic_Sketchy_Tasting_Card.pdf
    ├── Vintage_Tasting_Card.pdf
    └── Generic_Sketchy_Tasting_Card.pdf
```

## Dependencies

- `reportlab==4.2.5` - PDF generation library

## Tips for Using the Cards

1. **Print Settings**: Use standard A4 paper for best results
2. **Color vs. B&W**: The vintage style works well in both color and black & white printing
3. **Multiple Copies**: Generate cards in bulk by running scripts multiple times
4. **Customization**: Feel free to fork and modify for your specific needs

## Troubleshooting

**Issue**: "PatrickHand.ttf not found" or "GreatVibes-Regular.ttf not found"
- **Solution**: Run `python setup_fonts.py` to download both custom fonts

**Issue**: "reportlab module not found"
- **Solution**: Make sure your virtual environment is activated and run `pip install -r requirements.txt`

**Issue**: PDF not being generated
- **Solution**: Check that you have write permissions in the project directory

## License

This project is open source and free for personal and educational use. See LICENSE file for details.

## Contributing

Feel free to customize these scripts for your own wine tasting needs. If you create interesting variations, consider sharing them!

---

Happy tasting! 🍷
