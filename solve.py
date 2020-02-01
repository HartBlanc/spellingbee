import re


def lambda_handler(event, context):

    solve
    
    HTML_START = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>sendToKindle</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>

        </style>

    </head>

    <body>
    <ul>
'''

    HTML_middle = ""

    HTML_END = '''
</ul>
</body>

</html>'''

    results = solve(event['query']['std_letters'], event['query']['special_letter'], event['query']['min_length'])



    HTML_middle = '\n'.join([f"<li>{result}</li>" for result in results])

    return HTML_START + HTML_middle + HTML_END

def solve(std_letters, special_letter, min_length=4):
    
    allowed_letters = std_letters + [special_letter]

    with open("words_alpha.txt") as f:
        words = f.read().split('\n')
        print(words[0])
        print(len(words))

    print("[{''.join(allowed_letters)}]*{special_letter}[{allowed_letters}]*")

    pattern = re.compile(f"[{''.join(allowed_letters)}]*{special_letter}[{''.join(allowed_letters)}]*")

    return sorted([w for w in words if re.fullmatch(pattern, w) and len(w) >= min_length], key= lambda x : len(x), reverse=True)

# if __name__ == "__main__":
#     with open("index.html", "w") as f:
#         f.write(lambda_handler({'std_letters': "habel".split(), 'special_letter': "k", 'min_length': 4}, None))

