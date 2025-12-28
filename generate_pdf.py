from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('static/logo.jpg', 10, 8, 25)
        # Helvetica bold 15
        self.set_font('Helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'PhishShield User Guide', new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
        # Line break
        self.ln(30)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Helvetica italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', align='C')
        # About Us
        self.ln(5)
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 10, 'About Us', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(5)
        self.set_font('Helvetica', '', 8)
        self.multi_cell(0, 5, 'Our vision is to create a safer online environment for everyone. PhishShield is a tool designed to empower users to protect themselves from phishing attacks. We believe that with the right tools, everyone can navigate the web with confidence and security. With the help of this, we are safe from malicious actors on the internet.', align='C')


def create_phishshield_guide():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_text_color(101, 67, 33)
    pdf.set_font('Times', '', 12)

    # How to use section
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'How to Use PhishShield', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10,
        "1. Navigate to the PhishShield homepage.\n"
        "2. In the input box, type or paste the full URL of the website you want to check.\n"
        "3. Click the 'Check Safety' button.\n"
        "4. The next page will show you the result of the analysis, indicating whether the site is likely safe or a phishing attempt.\n"
        "5. The result page also shows a confidence score and the specific features of the URL that were analyzed."
    )
    pdf.ln(10)

    # Benefits section
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'Benefits of Using PhishShield', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10,
        """- **Real-time Protection:** Get an instant analysis of a URL before you visit it.
- **Increased Awareness:** Understand the characteristics of phishing URLs by seeing the feature analysis.
- **Peace of Mind:** Browse the web with more confidence, knowing you have a tool to check suspicious links.
- **Easy to Use:** A simple and intuitive interface makes it easy for anyone to check a URL."""
    )
    pdf.ln(10)

    pdf.output('PhishShield_Guide.pdf')

if __name__ == '__main__':
    create_phishshield_guide()
