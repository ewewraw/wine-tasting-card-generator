import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

# --- CUSTOM HANDWRITTEN FONT ---
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Handwritten', 'PatrickHand.ttf'))

def create_generic_sketchy_card(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # --- Modern Minimalist Palette ---
    pencil_grey = Color(0.2, 0.2, 0.2) 
    wine_red = Color(0.55, 0.15, 0.2)
    light_grey = Color(0.7, 0.7, 0.7)
    
    # --- Fonts ---
    header_font = "Handwritten" 
    body_font = "Handwritten"
    
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
    
    # --- Sketchy Drawing Functions ---

    def draw_pencil_stroke(x1, y1, x2, y2, color, stroke_width=0.8):
        c.setStrokeColor(color)
        c.setDash([]) 
        c.setLineWidth(stroke_width)
        j1 = random.uniform(-0.5, 0.5); j2 = random.uniform(-0.5, 0.5)
        c.line(x1 + j1, y1 + j1, x2 + j2, y2 + j2)
        c.setLineWidth(stroke_width * 0.6)
        j3 = random.uniform(-1.0, 1.0); j4 = random.uniform(-1.0, 1.0)
        c.line(x1 + j3, y1 + j3, x2 + j4, y2 + j4)

    def draw_pencil_rect(x, y, w, h, color=wine_red):
        overshoot = 4.0 
        draw_pencil_stroke(x - overshoot, y + h, x + w + overshoot, y + h, color) 
        draw_pencil_stroke(x - overshoot, y, x + w + overshoot, y, color)         
        draw_pencil_stroke(x, y - overshoot, x, y + h + overshoot, color)         
        draw_pencil_stroke(x + w, y - overshoot, x + w, y + h + overshoot, color) 

    def draw_pencil_bubble(x, y, w, h):
        c.setStrokeColor(light_grey)
        c.setDash([])
        c.setLineWidth(0.8)
        jx = random.uniform(-0.5, 0.5); jy = random.uniform(-0.5, 0.5)
        c.roundRect(x + jx, y + jy, w, h, 4, stroke=1, fill=0)
        c.setLineWidth(0.5)
        jx2 = random.uniform(-1.0, 1.0); jy2 = random.uniform(-1.0, 1.0)
        c.roundRect(x + jx2, y + jy2, w, h, 4, stroke=1, fill=0)

    # --- Content Drawing Functions ---

    def draw_vertical_header(text, y_center):
        c.saveState()
        c.translate(margin_left + 10, y_center) 
        c.rotate(90)
        c.setFillColor(wine_red)
        c.setFont(header_font, 12)
        c.drawCentredString(0, -3, text.upper())
        c.restoreState()

    def draw_criteria_row(label, options, y, spacing=80, has_bubbles=False):
        c.setFillColor(pencil_grey)
        c.setFont(header_font, 9)
        c.drawString(content_x, y, label)
        c.setFont(body_font, 8.5)
        option_list = [opt.strip() for opt in options.split('–')]
        current_opt_x = content_x + spacing
        
        for i, opt in enumerate(option_list):
            c.setFillColor(pencil_grey)
            c.drawString(current_opt_x, y, opt)
            text_width = c.stringWidth(opt, body_font, 8.5)
            if has_bubbles:
                bubble_width = 30 
                bubble_height = 10
                bubble_x = current_opt_x + (text_width / 2) - (bubble_width / 2)
                draw_pencil_bubble(bubble_x, y - 12, bubble_width, bubble_height)
            gap = 25 if has_bubbles else 12 
            current_opt_x += text_width + gap
            if i < len(option_list) - 1:
                sep_x = current_opt_x - (gap / 2) - 2
                c.drawString(sep_x, y, "-") 
        return y - (28 if has_bubbles else 22)

    def draw_input_row(label, y):
        c.setFillColor(pencil_grey)
        c.setFont(header_font, 9)
        c.drawString(content_x, y, label)
        c.setStrokeColor(light_grey)
        c.setLineWidth(0.5)
        c.setDash([1, 4]) 
        c.line(content_x + 110, y, criteria_right_boundary, y) 
        c.setDash([])
        return y - 24

    def draw_three_level_inputs(main_label, y):
        c.setFillColor(pencil_grey)
        c.setFont(header_font, 9)
        c.drawString(content_x, y, main_label)
        
        # UPDATED: Using generic terminology to match Aroma Box headers
        sub_labels = ["Grapes", "Winemaking", "Maturation"]
        current_row_y = y
        
        c.setFont(body_font, 8.5)
        for sub in sub_labels:
            c.setFillColor(pencil_grey)
            c.drawString(content_x + 80, current_row_y, sub + ":")
            c.setStrokeColor(light_grey)
            c.setLineWidth(0.5)
            c.setDash([1, 4])
            line_start = content_x + 140
            c.line(line_start, current_row_y, criteria_right_boundary, current_row_y)
            c.setDash([])
            current_row_y -= 18 
        return current_row_y - 5 

    def draw_dotted_header_row(label, x, y, width):
        c.setFont(header_font, 9)
        c.setFillColor(pencil_grey)
        c.drawString(x, y, label)
        label_w = c.stringWidth(label, header_font, 9)
        line_start = x + label_w + 5
        line_end = x + width
        c.setStrokeColor(light_grey)
        c.setLineWidth(0.5)
        c.setDash([1, 4])
        c.line(line_start, y, line_end, y)
        c.setDash([]) 

    def draw_aroma_box(start_y):
        LIFT_AMOUNT = 15 
        start_y += LIFT_AMOUNT
        title_y = start_y - 12 
        
        c.setFillColor(wine_red)
        c.setFont(header_font, 11)
        c.drawCentredString(aroma_box_x + aroma_box_width/2, title_y, "AROMAS & FLAVORS")
        
        box_y = title_y - 12 
        
        # --- GENERICIZED AROMA DATA ---
        aroma_data = [
            ("Grapes (Fruit/Floral)", [
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
            ("Winemaking (Process)", [
                "Yeast: dough, biscuit, bread, toast, pastry",
                "Dairy/MLF: butter, cream, yogurt, cheese",
                "Wood: vanilla, coconut, cedar, smoke, clove, coffee"
            ]),
            ("Maturation (Aging)", [
                "Earth: mushroom, forest floor, leather, game",
                "Bottle Age: honey, nut, ginger, petrol, marmalade",
                "Oxidation: almond, walnut, caramel, toffee, cocoa"
            ])
        ]
        
        c.setFillColor(pencil_grey)
        section_font_size = 7.5
        item_font_size = 6.5
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
        draw_pencil_rect(aroma_box_x, box_y, aroma_box_width, box_height, color=wine_red)

    def draw_notes_box(start_y, end_y):
        end_y -= 5 
        box_height = start_y - end_y
        
        c.setFillColor(wine_red)
        c.setFont(header_font, 10)
        c.drawCentredString(notes_box_x + notes_box_width/2, start_y - 10, "NOTES")
        
        box_top = start_y - 20
        box_height -= 20
        
        draw_pencil_rect(notes_box_x, end_y, notes_box_width, box_height, color=wine_red)
        
        line_y = box_top - 15
        while line_y > end_y + 5:
            c.setStrokeColor(light_grey)
            c.setLineWidth(0.5)
            c.setDash([1, 4])
            c.line(notes_box_x + 3, line_y, notes_box_x + notes_box_width - 3, line_y)
            line_y -= 15
        c.setDash([])

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
    current_y = draw_criteria_row("Clarity", "Clear – Hazy", current_y, has_bubbles=True)
    current_y = draw_criteria_row("Depth", "Pale – Medium – Dark", current_y, has_bubbles=True)
    
    c.setFont(header_font, 9)
    c.setFillColor(pencil_grey)
    c.drawString(content_x, current_y, "Hue")
    c.setFont(body_font, 8.5)
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
    
    # Updated to pass "Aromas" as the main label, but internal labels are now generic
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
    
    # Updated to pass "Flavors" as main label
    current_y = draw_three_level_inputs("Flavors", current_y)
    
    current_y = draw_criteria_row("Finish", "Short – Moderate – Long – Persistent", current_y, has_bubbles=True)
    taste_end_y = current_y + 20
    draw_vertical_header("Taste", (taste_start_y + taste_end_y) / 2)
    
    draw_notes_box(notes_start_y, current_y + 20)

    current_y -= SECTION_SPACING
    
    # --- 5. VERDICT ---
    conc_start_y = current_y
    
    c.setFont(header_font, 9)
    c.setFillColor(pencil_grey) 
    c.drawString(content_x, current_y, "Rating")
    
    c.setFont(body_font, 8.5)
    # Generic quality scale
    options = ["Flawed", "Below Avg", "Average", "Good", "Excellent", "Exceptional"]
    opt_x = content_x + 80
    for opt in options:
        c.setFillColor(pencil_grey)
        c.drawString(opt_x, current_y, opt)
        text_width = c.stringWidth(opt, body_font, 8.5)
        bubble_width = 30 
        bubble_x = opt_x + (text_width / 2) - (bubble_width / 2)
        draw_pencil_bubble(bubble_x, current_y - 12, bubble_width, 9)
        opt_x += text_width + 30 
    current_y -= 30
    
    c.setFont(header_font, 9)
    c.setFillColor(pencil_grey)
    c.drawString(content_x, current_y, "Status")
    
    c.setFont(body_font, 8.5)
    # Generic readiness scale
    readiness_options = ["Needs Time", "Ready to Drink", "At Peak", "Declining"]
    opt_x = content_x + 80
    for opt in readiness_options:
        c.setFillColor(pencil_grey)
        c.drawString(opt_x, current_y, opt)
        t_w = c.stringWidth(opt, body_font, 8.5)
        b_w = 30
        b_x = opt_x + (t_w/2) - (b_w/2)
        draw_pencil_bubble(b_x, current_y - 12, b_w, 9)
        opt_x += t_w + 30
        
    current_y -= 25
    conc_end_y = current_y + 10
    draw_vertical_header("Verdict", (conc_start_y + conc_end_y) / 2)

    c.save()

if __name__ == "__main__":
    create_generic_sketchy_card("Generic_Handwritten_Tasting_Card.pdf")