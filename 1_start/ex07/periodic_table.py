def parse_line(line):
    # Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1
    name, data = line.split(" = ")
    details = {}
    for item in data.split(", "):
        key, value = item.split(":")
        details[key.strip()] = value.strip()
    return name, details

def generate_html():
    elements = []
    
    with open('periodic_table.txt', 'r') as f:
        for line in f:
            if line.strip():
                elements.append(parse_line(line))

    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Tableau Périodique</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                td {
                    border: 1px solid #999;
                    padding: 4px;
                    width: 5.5%;
                    vertical-align: top;
                    text-align: center;
                    font-family: sans-serif;
                }
                .empty {
                    border: none;
                }
                .number {
                    font-size: 0.65em;
                    text-align: left;
                    color: #555;
                    margin: 0;
                }
                .symbol {
                    font-size: 1.6em;
                    font-weight: bold;
                    margin: 2px 0;
                }
                .name {
                    font-size: 0.6em;
                    margin: 0;
                }
                .molar {
                    font-size: 0.6em;
                    color: #444;
                    margin: 0;
                }
            </style>
        </head>
        <body>
            <table>
                <tr>
    """
    
    current_pos = 0
    for name, info in elements:
        pos = int(info['position'])
        
        # Changement de ligne
        if pos < current_pos:
            # Remplissage jusqu'à la fin de la ligne (colonne 17)
            for _ in range(current_pos, 18):
                html += '            <td class="empty"></td>\n'
            html += "        </tr>\n        <tr>\n"
            current_pos = 0
            
        # Remplissage des cases vides avant l'élément
        for _ in range(current_pos, pos):
            html += '            <td class="empty"></td>\n'
            
        # Case de l'élément
        html += f"""
        <td>
            <p class="number">{info['number']}</p>
            <p class="symbol">{info['small']}</p>
            <h4 class="name">{name}</h4>
            <p class="molar">{info['molar']}</p>
        </td>
        """
        current_pos = pos + 1
        
    # Remplissage de la fin de la dernière ligne
    for _ in range(current_pos, 18):
        html += '            <td class="empty"></td>\n'
        
    html += """        
    </tr>
    </table>
    </body>
    </html>
    """
    
    with open('periodic_table.html', 'w') as f:
        f.write(html)

if __name__ == '__main__':
    generate_html()
