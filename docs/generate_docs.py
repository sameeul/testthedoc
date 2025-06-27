import random
import os
from datetime import datetime

def generate_random_markdown():
    # Create docs directory if it doesn't exist
    os.makedirs("docs", exist_ok=True)
    
    # Create a new markdown file
    filename = f"docs/index.md"
    
    with open(filename, "w") as md_file:
        # Title and intro
        md_file.write("# Random Markdown Content\n\n")
        md_file.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*\n\n")
        
        # Table of Contents
        md_file.write("## Table of Contents\n\n")
        md_file.write("- [Headers](#headers)\n")
        md_file.write("- [Text Formatting](#text-formatting)\n")
        md_file.write("- [Lists](#lists)\n")
        md_file.write("- [Code Examples](#code-examples)\n")
        md_file.write("- [Links and Images](#links-and-images)\n")
        md_file.write("- [Tables](#tables)\n")
        md_file.write("- [Blockquotes](#blockquotes)\n")
        md_file.write("- [Task Lists](#task-lists)\n")
        md_file.write("- [Horizontal Rules](#horizontal-rules)\n\n")
        
        # Headers
        md_file.write("## Headers\n\n")
        md_file.write("# Header Level 1\n")
        md_file.write("## Header Level 2\n")
        md_file.write("### Header Level 3\n")
        md_file.write("#### Header Level 4\n")
        md_file.write("##### Header Level 5\n")
        md_file.write("###### Header Level 6\n\n")
        
        # Text Formatting
        md_file.write("## Text Formatting\n\n")
        md_file.write("This is **bold text** using double asterisks.\n\n")
        md_file.write("This is __bold text__ using double underscores.\n\n")
        md_file.write("This is *italic text* using single asterisks.\n\n")
        md_file.write("This is _italic text_ using single underscores.\n\n")
        md_file.write("This is ***bold and italic text*** using triple asterisks.\n\n")
        md_file.write("This is ~~strikethrough text~~ using tildes.\n\n")
        md_file.write("This is `inline code` using backticks.\n\n")
        
        # Lists
        md_file.write("## Lists\n\n")
        md_file.write("### Unordered List\n\n")
        md_file.write("- Item 1\n")
        md_file.write("- Item 2\n")
        md_file.write("  - Nested Item 2.1\n")
        md_file.write("  - Nested Item 2.2\n")
        md_file.write("- Item 3\n\n")
        
        md_file.write("### Ordered List\n\n")
        md_file.write("1. First Item\n")
        md_file.write("2. Second Item\n")
        md_file.write("   1. Nested Item 2.1\n")
        md_file.write("   2. Nested Item 2.2\n")
        md_file.write("3. Third Item\n\n")
        
        # Code Blocks
        md_file.write("## Code Examples\n\n")
        md_file.write("\n")
        md_file.write("def hello_world():\n")
        md_file.write("    print('Hello, World!')\n")
        md_file.write("\n")
        md_file.write("# Call the function\n")
        md_file.write("hello_world()\n")
        md_file.write("\n\n")
        
        md_file.write("\n")
        md_file.write("function helloWorld() {\n")
        md_file.write("    console.log('Hello, World!');\n")
        md_file.write("}\n")
        md_file.write("\n")
        md_file.write("// Call the function\n")
        md_file.write("helloWorld();\n")
        md_file.write("\n\n")
        
        # Links and Images
        md_file.write("## Links and Images\n\n")
        md_file.write("[Link to Google](https://www.google.com)\n\n")
        md_file.write("[Link with Title](https://www.github.com 'GitHub Homepage')\n\n")
        md_file.write("![Alt text for an image](https://via.placeholder.com/150 'Image Title')\n\n")
        md_file.write("<https://www.example.com> - Automatic link\n\n")
        
        # Tables
        md_file.write("## Tables\n\n")
        md_file.write("| Header 1 | Header 2 | Header 3 |\n")
        md_file.write("|----------|----------|----------|\n")
        md_file.write("| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |\n")
        md_file.write("| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |\n")
        md_file.write("| Row 3, Col 1 | Row 3, Col 2 | Row 3, Col 3 |\n\n")
        
        md_file.write("### Table Alignment\n\n")
        md_file.write("| Left-aligned | Center-aligned | Right-aligned |\n")
        md_file.write("|:-------------|:---------------:|---------------:|\n")
        md_file.write("| Left | Center | Right |\n")
        md_file.write("| Text | Text | Text |\n\n")
        
        # Blockquotes
        md_file.write("## Blockquotes\n\n")
        md_file.write("> This is a blockquote.\n>\n")
        md_file.write("> It can span multiple lines.\n>\n")
        md_file.write("> > This is a nested blockquote.\n\n")
        
        # Task Lists
        md_file.write("## Task Lists\n\n")
        md_file.write("- [x] Completed task\n")
        md_file.write("- [ ] Incomplete task\n")
        md_file.write("- [x] Another completed task\n")
        md_file.write("- [ ] Another incomplete task\n\n")
        
        # Horizontal Rules
        md_file.write("## Horizontal Rules\n\n")
        md_file.write("Three hyphens:\n\n")
        md_file.write("---\n\n")
        md_file.write("Three asterisks:\n\n")
        md_file.write("***\n\n")
        md_file.write("Three underscores:\n\n")
        md_file.write("___\n\n")
        
        # Conclusion
        md_file.write("## Conclusion\n\n")
        md_file.write("This document demonstrates various Markdown syntax elements that can be used in your documentation.\n\n")
        
    print(f"Random Markdown file created: {filename}")
    return filename

if __name__ == "__main__":
    generate_random_markdown()