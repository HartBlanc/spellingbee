import re
import json

def lambda_handler(event, context):
    results = solve(event["queryStringParameters"]['std_letters'],
                    event["queryStringParameters"]['special_letter'],
                    event["queryStringParameters"]['min_length'])
    
    response = {
        "statusCode": 200,
        "body": json.dumps(results)
    }
    
    return response
    

def solve(std_letters, special_letter, min_length="4"):
    
    special_letter = special_letter.lower().strip()
    std_letters = std_letters.lower().strip()
    min_length = int(min_length.strip())
    
    allowed_letters = std_letters.split() + [special_letter]
    
    with open("words_alpha.txt") as f:
        words = f.read()
    
    pattern = re.compile(
        f"^[{''.join(allowed_letters)}]*{special_letter}[{''.join(allowed_letters)}]*$",
        re.MULTILINE)
    
    return [m for m in re.findall(pattern, words) if len(m) >= min_length]
    
    # with open("words_alpha.txt") as f:
    #     words = f.read().split('\n')
    
    # pattern = re.compile(f"[{''.join(allowed_letters)}]*{special_letter}[{''.join(allowed_letters)}]*")
    
    # return [w for w in words if re.match(pattern, w) and len(w) >= min_length]

# if __name__ == "__main__":
#     with open("words_alpha.txt") as f:
#         words = f.read().split('\n')

#     words = sorted(
#         {w.lower() for w in words},
#         key = lambda x : len(x),
#         reverse=True,
#     )

#     with open("words_alpha.txt", "w") as f:
#         for w in words:
#             f.write(w)
#             f.write('\n')


