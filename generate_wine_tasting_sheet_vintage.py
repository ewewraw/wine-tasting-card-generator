import random
import math
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

# --- FONT CONFIGURATION ---
# To get the true "Ink" look, download "GreatVibes-Regular.ttf" or "Allura-Regular.ttf"
# from Google Fonts and put it in the same folder as this script.
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

custom_font_name = "GreatVibes-Regular.ttf" # Change this to your downloaded filename
font_registered = False

try:
    pdfmetrics.registerFont(TTFont('InkFont', custom_font_name))
    header_font = "InkFont"
    body_font = "InkFont"
    font_registered = True
    print(f"Success: Using custom font {custom_font_name}")
except:
    # Fallback if you haven't downloaded a font yet
    header_font = "Times-BoldItalic"
    body_font = "Times-Italic"
    print("Notice: Custom font not found. Using Times-Italic fallback.")

def create_vintage_tasting_card(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # --- Dreamy / Ink Palette ---
    # Background: Antique Parchment
    paper_base = Color(0.96, 0.93, 0.85) 
    
    # Text/Lines: Deep Sepia / Iron Gall Ink (Not pure black)
    ink_color = Color(0.25, 0.15, 0.10) 
    
    # Accents: Faded Burgundy/Wine stain
    wine_stain = Color(0.6, 0.2, 0.2, alpha=0.15)
    
    # Texture colors (for the paper effect)
    stain_dark = Color(0.85, 0.80, 0.70, alpha=0.3)
    stain_light = Color(1, 1, 0.95, alpha=0.4)
    ink_splatter = Color(0.25, 0.15, 0.10, alpha=0.6)

    # --- Layout Constants (STRICTLY PRESERVED) ---
    margin_left = 15
    vertical_header_width = 25
    content_x = margin_left + vertical_header_width + 10 
    
    right_col_x = width * 0.58 
    right_col_width = width - right_col_x - 15
    
    aroma_box_x = right_col_x
    aroma_box_width = right_col_width
    
    notes_box_width = right_col_width * 0.75
    notes_box_x = width - notes_box_width - 15
    
    criteria_right_boundary = notes_box_x - 15
    
    # --- 1. PROCEDURAL BACKGROUND GENERATOR ---
    def draw_old_paper_background():
        """Creates a wrinkled paper and ink stain effect procedurally."""
        # 1. Base Fill
        c.setFillColor(paper_base)
        c.rect(0, 0, width, height, stroke=0, fill=1)
        
        # 2. "Wrinkles" and Texture (Large random blobs)
        for _ in range(60):
            size = random.randint(50, 200)
            x = random.randint(0, int(width))
            y = random.randint(0, int(height))
            
            # Randomly choose between dark stain or light highlight
            if random.random() > 0.5:
                c.setFillColor(stain_dark)
            else:
                c.setFillColor(stain_light)
                
            # Draw irregular organic shapes (simulating water stains)
            p = c.beginPath()
            p.moveTo(x, y)
            for i in range(5):
                p.curveTo(
                    x + random.randint(-size, size), y + random.randint(-size, size),
                    x + random.randint(-size, size), y + random.randint(-size, size),
                    x + random.randint(-size, size), y + random.randint(-size, size)
                )
            p.close()
            c.drawPath(p, stroke=0, fill=1)

        # 3. Wine/Coffee Rings
        c.setLineWidth(2)
        c.setStrokeColor(wine_stain)
        for _ in range(3):
            rx = random.randint(0, int(width))
            ry = random.randint(0, int(height))
            r = random.randint(20, 60)
            c.circle(rx, ry, r, stroke=1, fill=0)

        # 4. Tiny Ink Splatters
        c.setFillColor(ink_splatter)
        for _ in range(40):
            sx = random.randint(0, int(width))
            sy = random.randint(0, int(height))
            sr = random.uniform(0.5, 2.5)
            c.circle(sx, sy, sr, stroke=0, fill=1)

    # --- Dreamy Drawing Functions ---

    def draw_ornate_rect(x, y, w, h):
        """Draws a 'swirly' double-line border typical of vintage labels."""
        # Inner Frame
        c.setStrokeColor(ink_color)
        c.setLineWidth(0.8)
        c.roundRect(x, y, w, h, 8, stroke=1, fill=0)
        
        # Outer Frame (Decorative)
        offset = 3
        c.setLineWidth(1.5)
        # Using bezier curves for corners to make them look more elegant/swirly
        # Top-Left
        p = c.beginPath()
        # Top Left Corner Swirl
        p.moveTo(x - offset, y + h - 10)
        p.curveTo(x - offset, y + h + offset, x - offset, y + h + offset, x + 10, y + h + offset)
        # Top Line
        p.lineTo(x + w - 10, y + h + offset)
        # Top Right Corner
        p.curveTo(x + w + offset, y + h + offset, x + w + offset, y + h + offset, x + w + offset, y + h - 10)
        # Right Line
        p.lineTo(x + w + offset, y + 10)
        # Bottom Right Corner
        p.curveTo(x + w + offset, y - offset, x + w + offset, y - offset, x + w - 10, y - offset)
        # Bottom Line
        p.lineTo(x + 10, y - offset)
        # Bottom Left Corner
        p.curveTo(x - offset, y - offset, x - offset, y - offset, x - offset, y + 10)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
        
        # Decorative accents at midpoints (simple diamonds)
        c.setFillColor(ink_color)
        mid_x = x + w/2
        # Top diamond
        p = c.beginPath()
        p.moveTo(mid_x, y + h + offset + 2); p.lineTo(mid_x + 3, y + h + offset); p.lineTo(mid_x, y + h + offset - 2); p.lineTo(mid_x - 3, y + h + offset); p.close()
        c.drawPath(p, stroke=0, fill=1)
        # Bottom diamond
        p = c.beginPath()
        p.moveTo(mid_x, y - offset + 2); p.lineTo(mid_x + 3, y - offset); p.lineTo(mid_x, y - offset - 2); p.lineTo(mid_x - 3, y - offset); p.close()
        c.drawPath(p, stroke=0, fill=1)


    def draw_ink_bubble(x, y, w, h):
        """Draws a bubble that looks like a smooth ink loop."""
        c.setStrokeColor(ink_color)
        c.setLineWidth(0.8)
        # Slight transparency to look like watered down ink
        c.setStrokeColor(Color(0.25, 0.15, 0.10, alpha=0.7))
        c.roundRect(x, y, w, h, 6, stroke=1, fill=0)

    # --- Draw the Background First ---
    draw_old_paper_background()

    # --- Content Drawing Functions ---

    def draw_vertical_header(text, y_center):
        c.saveState()
        c.translate(margin_left + 10, y_center) 
        c.rotate(90)
        c.setFillColor(ink_color)
        # If using handwritten font, bump size up slightly for readability
        size = 16 if font_registered else 14
        c.setFont(header_font, size)
        c.drawCentredString(0, -3, text.upper())
        c.restoreState()

    def draw_criteria_row(label, options, y, spacing=80, has_bubbles=False):
        c.setFillColor(ink_color)
        
        # Labels slightly larger for handwritten fonts
        label_size = 12 if font_registered else 10
        body_size = 11 if font_registered else 9
        
        c.setFont(header_font, label_size)
        c.drawString(content_x, y, label)
        
        c.setFont(body_font, body_size)
        option_list = [opt.strip() for opt in options.split('–')]
        
        current_opt_x = content_x + spacing
        
        for i, opt in enumerate(option_list):
            c.setFillColor(ink_color)
            c.drawString(current_opt_x, y, opt)
            
            text_width = c.stringWidth(opt, body_font, body_size)
            
            if has_bubbles:
                bubble_width = 30 
                bubble_height = 11 # Slightly taller for elegance
                bubble_x = current_opt_x + (text_width / 2) - (bubble_width / 2)
                draw_ink_bubble(bubble_x, y - 12, bubble_width, bubble_height)
                
            gap = 25 if has_bubbles else 12 
            current_opt_x += text_width + gap
            
            if i < len(option_list) - 1:
                sep_x = current_opt_x - (gap / 2) - 2
                c.drawString(sep_x, y, "~") # Tilde looks nice as separator in ink fonts

        return y - (28 if has_bubbles else 22)

    def draw_input_row(label, y):
        c.setFillColor(ink_color)
        label_size = 12 if font_registered else 10
        c.setFont(header_font, label_size)
        c.drawString(content_x, y, label)
        
        # Fine line for writing on
        c.setStrokeColor(Color(0.25, 0.15, 0.10, alpha=0.5))
        c.setLineWidth(0.5)
        c.line(content_x + 110, y, criteria_right_boundary, y) 
        return y - 24

    def draw_three_level_inputs(main_label, y):
        c.setFillColor(ink_color)
        label_size = 12 if font_registered else 10
        sub_size = 11 if font_registered else 9
        
        c.setFont(header_font, label_size)
        c.drawString(content_x, y, main_label)
        
        sub_labels = ["Grapes", "Process", "Maturing"]
        current_row_y = y
        
        c.setFont(body_font, sub_size)
        
        for sub in sub_labels:
            c.setFillColor(ink_color)
            c.drawString(content_x + 80, current_row_y, sub + ":")
            
            c.setStrokeColor(Color(0.25, 0.15, 0.10, alpha=0.5))
            c.setLineWidth(0.5)
            line_start = content_x + 140
            c.line(line_start, current_row_y, criteria_right_boundary, current_row_y)
            
            current_row_y -= 18 
            
        return current_row_y - 5 

    def draw_dotted_header_row(label, x, y, width):
        label_size = 12 if font_registered else 10
        c.setFont(header_font, label_size)
        c.setFillColor(ink_color)
        c.drawString(x, y, label)
        
        label_w = c.stringWidth(label, header_font, label_size)
        line_start = x + label_w + 5
        line_end = x + width
        
        c.setStrokeColor(Color(0.25, 0.15, 0.10, alpha=0.5))
        c.setLineWidth(0.5)
        c.line(line_start, y, line_end, y)

    def draw_aroma_box(start_y):
        LIFT_AMOUNT = 15 
        start_y += LIFT_AMOUNT
        title_y = start_y - 12 
        
        c.setFillColor(ink_color)
        title_size = 14 if font_registered else 12
        c.setFont(header_font, title_size)
        c.drawCentredString(aroma_box_x + aroma_box_width/2, title_y, "AROMAS & FLAVORS")
        
        box_y = title_y - 12 
        
        # --- GENERICIZED AROMA DATA ---
        aroma_data = [
            ("FRUIT & FLORAL (Base)", [
                "Flowers: blossom, rose, violet, jasmine",
                "Orchard: apple, pear, quince, grape",
                "Citrus: lemon, lime, grapefruit, orange, zest",
                "Stone Fruit: peach, apricot, nectarine",
                "Tropical: banana, pineapple, mango, lychee, melon",
                "Berries: raspberry, strawberry, cranberry, currant",
                "Dark Fruit: blackberry, plum, blueberry, black cherry",
                "Vegetal: grass, bell pepper, asparagus, leaf",
                "Herbal: mint, eucalyptus, dill, fennel",
                "Spice: pepper, licorice, anise, cinnamon",
                "Ripeness: tart, ripe, jammy, baked, dried",
                "Minerality: stone, chalk, saline, flint"
            ]),
            ("WINEMAKING (Process)", [
                "Yeast: dough, biscuit, bread, toast, pastry",
                "Dairy/MLF: butter, cream, yogurt, cheese",
                "Wood: vanilla, coconut, cedar, smoke, clove, coffee"
            ]),
            ("MATURATION (Age)", [
                "Earth: mushroom, forest floor, leather, game",
                "Bottle Age: honey, nut, ginger, petrol, marmalade",
                "Oxidation: almond, walnut, caramel, toffee, cocoa"
            ])
        ]
        
        c.setFillColor(ink_color)
        # Font sizes need to be slightly smaller to fit the text in the column
        section_font_size = 9 if font_registered else 7.5
        item_font_size = 8 if font_registered else 6.5
        line_height = 9 
        
        for section, items in aroma_data:
            c.setFont(header_font, section_font_size)
            c.drawString(aroma_box_x + 5, box_y, section)
            box_y -= line_height + 1
            c.setFont(body_font, item_font_size)
            for item in items:
                c.drawString(aroma_box_x + 5, box_y, item)
                box_y -= line_height
            box_y -= 3 

        box_height = start_y - box_y + 5
        draw_ornate_rect(aroma_box_x, box_y, aroma_box_width, box_height)

    def draw_notes_box(start_y, end_y):
        end_y -= 5 
        box_height = start_y - end_y
        
        c.setFillColor(ink_color)
        title_size = 12 if font_registered else 10
        c.setFont(header_font, title_size)
        c.drawCentredString(notes_box_x + notes_box_width/2, start_y - 10, "NOTES")
        
        box_top = start_y - 20
        box_height -= 20
        
        draw_ornate_rect(notes_box_x, end_y, notes_box_width, box_height)
        
        line_y = box_top - 15
        while line_y > end_y + 5:
            c.setStrokeColor(Color(0.25, 0.15, 0.10, alpha=0.3))
            c.setLineWidth(0.5)
            c.line(notes_box_x + 5, line_y, notes_box_x + notes_box_width - 5, line_y)
            line_y -= 15

    # --- START DRAWING ---
    
    SECTION_SPACING = 15  
    
    current_y = height - 40
    
    # --- 1. HEADER ---
    header_w = right_col_x - margin_left - 20
    row_height = 24
    
    draw_dotted_header_row("Wine Name:", margin_left, current_y, header_w)
    current_y -= row_height
    draw_dotted_header_row("Producer:", margin_left, current_y, header_w)
    current_y -= row_height
    draw_dotted_header_row("Region:", margin_left, current_y, header_w)
    current_y -= row_height
    draw_dotted_header_row("Varietals:", margin_left, current_y, header_w)
    current_y -= row_height
    
    date_w = header_w * 0.4
    draw_dotted_header_row("Date:", margin_left, current_y, date_w)
    vintage_x = margin_left + date_w + 20
    vintage_w = header_w * 0.25 
    draw_dotted_header_row("Vintage:", vintage_x, current_y, vintage_w)
    
    draw_aroma_box(height - 45)
    
    current_y -= 30 
    
    # --- 2. VISUAL ---
    app_start_y = current_y 
    # Replaced "Clarity" with "Has Sediment?" concept or similar, 
    # but sticking to synonyms for Clarity/Intensity
    current_y = draw_criteria_row("Clarity", "Clear – Hazy", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Depth", "Pale – Medium – Dark", current_y, has_bubbles=True)
    
    c.setFont(header_font, 12 if font_registered else 9)
    c.setFillColor(ink_color)
    c.drawString(content_x, current_y, "Hue")
    c.setFont(body_font, 11 if font_registered else 8.5)
    c.drawString(content_x + 80, current_y, "White: Straw – Yellow – Gold – Amber")
    current_y -= 16 
    c.drawString(content_x + 80, current_y, "Rosé: Pink – Salmon – Copper")
    current_y -= 16
    c.drawString(content_x + 80, current_y, "Red: Purple – Ruby – Garnet – Brick")
    current_y -= 20
    
    app_end_y = current_y + 18 
    draw_vertical_header("Visual", (app_start_y + app_end_y) / 2)
    
    current_y -= SECTION_SPACING
    
    notes_start_y = current_y + 10
    
    # --- 3. SMELL ---
    smell_start_y = current_y
    current_y = draw_criteria_row("Condition", "Clean – Faulty?", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Strength", "Light – Moderate – Powerful", current_y, has_bubbles=True)
    current_y = draw_three_level_inputs("Aromas", current_y)
    current_y = draw_criteria_row("Aging", "Young – Developing – Peak – Past Peak", current_y, has_bubbles=True)
    smell_end_y = current_y + 20
    draw_vertical_header("Smell", (smell_start_y + smell_end_y) / 2)
    
    current_y -= SECTION_SPACING
    
    # --- 4. TASTE ---
    taste_start_y = current_y
    
    # Generic sweetness scale
    current_y = draw_criteria_row("Sweetness", "Bone Dry – Dry – Semi-Dry – Semi-Sweet – Sweet", current_y, spacing=60, has_bubbles=True)
    
    current_y = draw_criteria_row("Tartness", "Low – Moderate – Crisp – High", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Tannins", "Low – Moderate – Chewy – High", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Alcohol", "Low – Moderate – High", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Body", "Light – Medium – Full", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Bubbles", "Still – Gentle – Aggressive", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Intensity", "Subtle – Moderate – Intense", current_y, has_bubbles=True)
    current_y = draw_three_level_inputs("Flavors", current_y)
    current_y = draw_criteria_row("Finish", "Short – Moderate – Long – Persistent", current_y, has_bubbles=True)
    taste_end_y = current_y + 20
    draw_vertical_header("Taste", (taste_start_y + taste_end_y) / 2)
    
    draw_notes_box(notes_start_y, current_y + 20)

    current_y -= SECTION_SPACING
    
    # --- 5. VERDICT ---
    conc_start_y = current_y
    
    c.setFont(header_font, 12 if font_registered else 9)
    c.setFillColor(ink_color) 
    c.drawString(content_x, current_y, "Rating")
    
    c.setFont(body_font, 11 if font_registered else 8.5)
    options = ["Flawed", "Below Avg", "Average", "Good", "Excellent", "Exceptional"]
    opt_x = content_x + 80
    for opt in options:
        c.setFillColor(ink_color)
        c.drawString(opt_x, current_y, opt)
        text_width = c.stringWidth(opt, body_font, 11 if font_registered else 8.5)
        bubble_width = 30 
        bubble_x = opt_x + (text_width / 2) - (bubble_width / 2)
        draw_ink_bubble(bubble_x, current_y - 12, bubble_width, 11)
        opt_x += text_width + 30 
    current_y -= 30
    
    c.setFont(header_font, 12 if font_registered else 9)
    c.setFillColor(ink_color)
    c.drawString(content_x, current_y, "Status")
    
    c.setFont(body_font, 11 if font_registered else 8.5)
    readiness_options = ["Needs Time", "Ready to Drink", "At Peak", "Declining"]
    opt_x = content_x + 80
    for opt in readiness_options:
        c.setFillColor(ink_color)
        c.drawString(opt_x, current_y, opt)
        t_w = c.stringWidth(opt, body_font, 11 if font_registered else 8.5)
        b_w = 30
        b_x = opt_x + (t_w/2) - (b_w/2)
        draw_ink_bubble(b_x, current_y - 12, b_w, 11)
        opt_x += t_w + 30
        
    current_y -= 25
    conc_end_y = current_y + 10
    draw_vertical_header("Verdict", (conc_start_y + conc_end_y) / 2)

    c.save()

if __name__ == "__main__":
    create_vintage_tasting_card("Vintage_Tasting_Card.pdf")