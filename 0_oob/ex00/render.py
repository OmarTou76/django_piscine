import sys
import os
import re


def render(template_path: str) -> None:
    if not template_path.endswith('.template'):
        raise ValueError("Invalid file extension. Expected a .template file.")
        
    if not os.path.exists(template_path):
        raise FileNotFoundError("File does not exist.")
        
    if not os.path.isfile(template_path):
        raise IsADirectoryError("Path is not a regular file.")
        
    import settings
    variables = {k: v for k, v in vars(settings).items() if not k.startswith('__')}

    with open(template_path, "r") as f:
        template_content = f.read()

    def replace_match(match):
        key = match.group(1)
        if key in variables:
            return str(variables[key])
        else:
            raise KeyError(f"Variable '{key}' not found in settings.")

    rendered_content = re.sub(r"\{(\w+)\}", replace_match, template_content)
    
    output_path = template_path.replace(".template", ".html")

    with open(output_path, "w") as f:
        f.write(rendered_content)

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of arguments.\nUsage: python3 render.py <file.template>")
        render(sys.argv[1])
    except Exception as e:
        print(f"Error {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()