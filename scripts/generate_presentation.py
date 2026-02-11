#!/usr/bin/env python3
"""
Script to generate a PowerPoint presentation from markdown content.
This script is used to create and update the ImpactSocial presentation.

Usage:
    python3 scripts/generate_presentation.py

Requirements:
    pip install python-pptx

Input:
    docs/presentation-plateforme-developpement-participatif.md

Output:
    docs/presentations/plateforme-developpement-participatif.pptx
"""

import re
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN


def parse_markdown(md_file):
    """Parse the markdown file and extract slides content."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the main header
    content = re.sub(r'^# .+\n', '', content, count=1)
    
    # Split by slide sections (## Slide X : ...)
    slides_raw = re.split(r'\n---\n', content)
    
    slides = []
    for slide_raw in slides_raw:
        if not slide_raw.strip():
            continue
        
        slide_data = {
            'title': '',
            'subtitle': '',
            'bullets': [],
            'notes': '',
            'has_placeholder': False
        }
        
        lines = slide_raw.strip().split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('## Slide'):
                # Extract title from "## Slide X : Title"
                match = re.match(r'## Slide \d+ : (.+)', line)
                if match:
                    slide_data['title'] = match.group(1)
            
            elif line.startswith('**Titre :**'):
                slide_data['title'] = line.replace('**Titre :**', '').strip()
            
            elif line.startswith('**Sous-titre :**'):
                slide_data['subtitle'] = line.replace('**Sous-titre :**', '').strip()
            
            elif line.startswith('**Points clés :**'):
                current_section = 'bullets'
            
            elif line.startswith('**Notes de présentation :**'):
                current_section = 'notes'
            
            elif line.startswith('**[Placeholder'):
                slide_data['has_placeholder'] = True
                slide_data['bullets'].append(line.replace('**', '').replace('[', '').replace(']', ''))
            
            elif line.startswith('- ') and current_section == 'bullets':
                slide_data['bullets'].append(line[2:])  # Remove "- " prefix
            
            elif line.startswith('"') and current_section == 'notes':
                # Extract notes text between quotes
                slide_data['notes'] += line.strip('"') + ' '
        
        if slide_data['title']:
            slides.append(slide_data)
    
    return slides


def create_presentation(slides, output_file):
    """Create a PowerPoint presentation from slides data."""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    for idx, slide_data in enumerate(slides):
        # Choose layout based on slide type
        if idx == 0 and slide_data['subtitle']:
            # Title slide
            slide_layout = prs.slide_layouts[0]  # Title Slide layout
            slide = prs.slides.add_slide(slide_layout)
            title = slide.shapes.title
            subtitle = slide.placeholders[1]
            
            title.text = slide_data['title']
            subtitle.text = slide_data['subtitle']
        else:
            # Content slide with bullets
            slide_layout = prs.slide_layouts[1]  # Title and Content layout
            slide = prs.slides.add_slide(slide_layout)
            title = slide.shapes.title
            content = slide.placeholders[1]
            
            title.text = slide_data['title']
            
            # Add bullets
            tf = content.text_frame
            tf.clear()  # Clear default text
            
            for i, bullet in enumerate(slide_data['bullets']):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                
                p.text = bullet
                p.level = 0
                p.font.size = Pt(18)
        
        # Add notes if present
        if slide_data['notes']:
            notes_slide = slide.notes_slide
            text_frame = notes_slide.notes_text_frame
            text_frame.text = slide_data['notes'].strip()
    
    # Save the presentation
    prs.save(output_file)
    print(f"✓ Presentation created successfully: {output_file}")
    print(f"✓ Total slides: {len(slides)}")


def main():
    """Main function to generate the PowerPoint presentation."""
    # Get the repository root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Parent of scripts dir
    
    # Paths
    md_file = os.path.join(base_dir, 'docs/presentation-plateforme-developpement-participatif.md')
    output_dir = os.path.join(base_dir, 'docs/presentations')
    output_file = os.path.join(output_dir, 'plateforme-developpement-participatif.pptx')
    
    # Verify input file exists
    if not os.path.exists(md_file):
        print(f"✗ Error: Markdown file not found: {md_file}")
        return 1
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Parse markdown and create presentation
    print(f"Parsing markdown file: {md_file}")
    slides = parse_markdown(md_file)
    print(f"Found {len(slides)} slides")
    
    print(f"\nCreating PowerPoint presentation...")
    create_presentation(slides, output_file)
    
    print(f"\n✓ Done! Presentation saved to: {output_file}")
    print(f"\nYou can open the file with:")
    print(f"  - Microsoft PowerPoint")
    print(f"  - LibreOffice Impress")
    print(f"  - PowerPoint Online")
    print(f"  - Google Slides (import)")
    
    return 0


if __name__ == '__main__':
    exit(main())
