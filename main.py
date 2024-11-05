import requests
import html

amount = input("Please enter the amount of questions you want: ")
difficulty = input(
    "Please specify how difficult you'd like the questions to be (easy/medium/hard): "
)

url = "https://opentdb.com/api.php"

request_params = {
    "type": "boolean",
    "amount": amount,
    "difficulty": difficulty,
    "category": "18",
}

response = requests.get(
    url, headers={"Accept": "application/json"}, params=request_params
)

data = response.json()["results"]

qna = [["Question", "Answer"]]

for item in data:
    q = "True or False? " + html.unescape(item["question"])

    # if item["type"] == "boolean":
    #     q = "True or False? " + q
    a = html.unescape(item["correct_answer"])

    qna.append([q, a])

    print(q)
    answer = input("Answer: ")

    if answer == a:
        print("Correct answer")
    else:
        print(f"Wrong answer, correct answer is {a}")


# with open("tech trivia.csv", "w", newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(qna)

# print(data)

# print(qna)
