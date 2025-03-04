import re

# fucntion to get session id
def extract_session_id(session_str: str):
    
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

# function to use list comprehension to get back result

def get_back_str_from_food_dict(food_dict:dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


if __name__ == "__main__":
   print(extract_session_id("projects/chef-lark-lrkc/agent/sessions/9667a2b6-9f31-3e3b-cbfd-606785053b71/contexts/ongoing-order"))
