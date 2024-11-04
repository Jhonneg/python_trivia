import requests
import html


amount = input("Please enter the amount of questions you want: ")
difficulty = input(
    "Please specify how difficult you'd like the questions to be (easy/medium/hard): "
)

url = "https://opentdb.com/api.php"

request_params = {"amount": amount, "difficulty": difficulty, "category": "18"}

response = requests.get(
    url, headers={"Accept": "application/json"}, params=request_params
)

data = response.json()["results"]

qna = [["Question", "Answer"]]

for item in data:
    q = html.unescape(item["question"])
    a = html.unescape(item["correct_answer"])

    qna.append([q, a])

print(data)

# print(qna)
