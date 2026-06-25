import sys
import time
from pathlib import Path
import pymupdf4llm
from tqdm import tqdm

# Initialize paths and ensure directories exist
pdf_dir = Path('pdf')
markdown_dir = Path('markdown')
markdown_dir.mkdir(parents=True, exist_ok=True)

# Fetch and display available PDF files
pdf_files = list(pdf_dir.glob('*.pdf'))

print("\nAvailable PDF files in 'pdf/' directory:")
print('-' * 50)
if not pdf_files:
    print("[No PDF files found. Please add .pdf files to the 'pdf' folder]")
    print('-' * 50)
    sys.exit(0)

for f in pdf_files:
    print(f"  • {f.name}")
print('-' * 50)

# Get clean user input (strips accidental leading/trailing spaces)
file_name = input("Enter PDF file name (with extension): ").strip()
pdf_file = pdf_dir / file_name

# Validate file existence before conversion
if not pdf_file.is_file():
    print(f"\n❌ Error: '{file_name}' not found inside the '{pdf_dir}' directory.")
    sys.exit(1)

print(f"\nProcessing '{pdf_file.name}'...")

# Optimized progress bar: Simulates initialization, runs core task, completes smoothly
with tqdm(total=100, desc="Converting PDF", unit="%", ncols=80) as pbar:
    # 1. Simulate fast initial progress setup (20%)
    for _ in range(4):
        time.sleep(0.05)
        pbar.update(5)
        
    # 2. Perform the actual conversion (Heavy lifting)
    markdown_text = pymupdf4llm.to_markdown(str(pdf_file), embed_images=True)
    pbar.update(60)  # Jump bar forward after extraction finishes
    
    # 3. Simulate file writing/saving finish line (20%)
    for _ in range(4):
        time.sleep(0.05)
        pbar.update(5)

# Save output using modern pathlib path resolution
output_path = markdown_dir / f"{pdf_file.stem}.md"
output_path.write_text(markdown_text, encoding="utf-8")

print(f"\n🎉 Conversion complete! Output saved to: {output_path}\n")
