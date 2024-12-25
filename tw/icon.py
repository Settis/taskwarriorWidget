from tw.status import Status, Type
from PyQt6.QtGui import QIcon
from PIL import Image, ImageDraw, ImageFont

ICON_FILES = {
    Type.ERROR: 'icons/todo-error.png',
    Type.OK: 'icons/todo-ok.png',
    Type.REVIEW: 'icons/todo-review.png',
    Type.WEEK: 'icons/todo-week.png',
    Type.TODAY: 'icons/todo-today.png',
    Type.OVERDUE: 'icons/todo-overdue.png'
}

def get_icon(status: Status) -> QIcon:
    tasks = status.tasks_count
    base_icon = ICON_FILES[status.type]
    if tasks == 0:
        return QIcon(base_icon)
    return QIcon(put_number(base_icon, tasks))

def put_number(base_icon: str, n: int):
    base_image = Image.open(base_icon).convert("RGBA")

    # Create an overlay with the count
    overlay = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # Define font and position for the count
    font_size = int(base_image.size[1] / 2.5)  # Adjust as needed
    font = ImageFont.truetype("NotoSans-Regular.ttf", font_size)
    text = str(min(999, n))

    # Calculate position to center the text
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Returns (x0, y0, x1, y1)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = base_image.size[0] - text_width - 5  # Right aligned
    text_y = base_image.size[1] - text_height - 25  # Bottom aligned

    # Draw the text on the overlay
    padding = 5
    draw.rounded_rectangle((text_x-padding, text_y, text_x+text_width+padding, text_y+text_height+5*padding), 5, fill="lightgray")
    draw.text((text_x, text_y), text, font=font, fill="black")

    # Combine the base image and the overlay
    combined = Image.alpha_composite(base_image, overlay)

    # Convert the result to a QPixmap
    return combined.toqpixmap()
