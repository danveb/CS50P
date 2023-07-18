# Implement a Python program that prompts user for their name
# output (using fpdf2) a CS50 shirtificate in a file called "shirtificate.pdf"
# specs:
# - orientation: Portrait
# - format: A4 (210mm w * 297mm h)
# - top of PDF: "CS50 Shirtificate" as text, centered horizontally
# - shirt's image centered horizontally
# - user's name should be on top of shirt, in white text

from fpdf import FPDF

# pdf = FPDF(orientation="P", unit="mm", format="A4")
# pdf.add_page()
# pdf.set_font("helvetica", "B", 16)
# pdf.cell(40, 10, "John Harvard")
# pdf.output("shirtificate.pdf")

# build a class Shirt

class Shirt:
    def __init__(self, name):
        self.name = name
        self.tailor()

    # GET
    @classmethod
    def shirtify(cls):
        name = input("Name: ").strip()
        return cls(name)


    def tailor(self):
        """Output a PDF with Harvard's shirt"""
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # set font for text on top of PDF
        pdf.set_font("helvetica", "B", 36)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()

        # add an image of Harvard's shirt
        pdf.image("shirtificate.png", x=15, y=(297/4), w=180)

        # set font for text on top of shirt
        pdf.set_font("helvetica", "B", 24)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")

        # output to pdf
        pdf.output("shirtificate.pdf")

def main():
    """Main function to shirtify CS50"""
    Shirt.shirtify()

if __name__ == "__main__":
    main()