#!/usr/bin/env python3
import os
import re

def fix_spacing(content):
    """Fix spacing issues in blog content for both mobile and desktop"""
    
    # Remove multiple consecutive blank lines and replace with single blank line
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Ensure single blank line before major sections
    content = re.sub(r'(\s*</div>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</blockquote>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</pre>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ul>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ol>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</p>\s*)\n\s*(<h2)', r'\1\n\n\2', content)
    
    # Ensure single blank line before subsections (h3)
    content = re.sub(r'(\s*</div>\s*)\n\s*(<h3)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ul>\s*)\n\s*(<h3)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ol>\s*)\n\s*(<h3)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</p>\s*)\n\s*(<h3)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</pre>\s*)\n\s*(<h3)', r'\1\n\n\2', content)
    
    # Ensure single blank line before info-box and highlight-box
    content = re.sub(r'(\s*</p>\s*)\n\s*(<div class="info-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ul>\s*)\n\s*(<div class="info-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ol>\s*)\n\s*(<div class="info-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</pre>\s*)\n\s*(<div class="info-box">)', r'\1\n\n\2', content)
    
    content = re.sub(r'(\s*</p>\s*)\n\s*(<div class="highlight-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ul>\s*)\n\s*(<div class="highlight-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</ol>\s*)\n\s*(<div class="highlight-box">)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</pre>\s*)\n\s*(<div class="highlight-box">)', r'\1\n\n\2', content)
    
    # Ensure single blank line before blockquotes
    content = re.sub(r'(\s*</div>\s*)\n\s*(<blockquote>)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</p>\s*)\n\s*(<blockquote>)', r'\1\n\n\2', content)
    
    # Ensure single blank line before pre blocks
    content = re.sub(r'(\s*</p>\s*)\n\s*(<pre>)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*</h3>\s*)\n\s*(<pre>)', r'\1\n\n\2', content)
    
    # Remove extra spaces before closing tags
    content = re.sub(r'\s+(</(div|blockquote|pre|ul|ol|p|h2|h3)>)', r'\1', content)
    
    return content

def process_blog_files():
    """Process all HTML files in the posts directory"""
    posts_dir = "posts"
    
    if not os.path.exists(posts_dir):
        print(f"Directory {posts_dir} not found!")
        return
    
    html_files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    
    for filename in html_files:
        filepath = os.path.join(posts_dir, filename)
        print(f"Processing {filename}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Fix spacing
            fixed_content = fix_spacing(content)
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(fixed_content)
            
            print(f"Fixed spacing in {filename}")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    process_blog_files()
    print("Spacing fix completed for all existing blog files!")