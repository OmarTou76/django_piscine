import sys
import os
import re

def render(template_path):
    if not template_path.endswith('.template'):
        raise ValueError("Invalid file extension. Expected a .template file.")
        
    if not os.path.exists(template_path):
        raise FileNotFoundError("File does not exist.")
        
    if not os.path.isfile(template_path):
        raise IsADirectoryError("Path is not a regular file.")
        
    if not os.path.exists("settings.py"):
        raise FileNotFoundError("File 'settings.py' not found.")
        
    # Read and parse settings.py using exec to inject into globals
    with open("settings.py", "r") as f:
        exec(f.read(), glob
        
    # Read the template file
    with open(template_path, "r") as f:
        template_content = f.read()

    # Keyword expansion using format() and globals()
    # It replaces {var} with the corresponding variable in globals
    # as hinted by 'help(globals), keyword expansion...'
    rendered_content = template_content.format(**globals())
    
    # Write to HTML file
    output_path = template_path[:-9] + ".html"
    with open(output_path, "w") as f:
        f.write(rendered_content)

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of arguments.\nUsage: python3 render.py <file.template>")
        render(sys.argv[1])
    except Exception as e:
        print(f"Error {type(e).__name__}: {e}")
        # Even on error we must handle gracefully, no traceback printed
        sys.exit(1)

if __name__ == '__main__':
    main()
