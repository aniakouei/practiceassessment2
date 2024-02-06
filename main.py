#Pseudocode:
#create a comment class and have texts, likes, dislikes and is_flagged
    #also put a function called print_info
#create a question class that is a subclass of parent, initialize the same but add answer and topic
    #also place another print_info function that will override
#create a list of comments and questions
# Function to print all comments and questions
# Function to print only unflagged comments and questions
# Function to calculate average engagement
# Calling the functions



class Comment:
    def __init__(self, text, likes, dislikes, is_flagged):
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        self.is_flagged = is_flagged

    def print_info(self):
        print(f"Comment: {self.text}")
        print(f"Likes: {self.likes}, Dislikes: {self.dislikes}, Is Flagged: {self.is_flagged}")


class Question(Comment):
    def __init__(self, text, likes, dislikes, is_flagged, topic, answer):
        Comment.__init__(self, text, likes, dislikes, is_flagged)
        self.topic = topic
        self.answer = answer

    def print_info(self):
        Comment.print_info(self)
        print(f"Topic: {self.topic}")
        print(f"Answer: {self.answer}")



comments_list = [
    Comment("pineapple on pizza.", 10, 10, True),
    Comment("I liked this video.", 30, 20, False),
    Comment("LOL", 4, 1, False),
    Question("Should I dislike Shrek?", 1, 15, True, "Blasphemy", "No you shouldn't"),
    Question("Why did the programmer quit their job?", 12, 12, False, "Coding", "They didn't get arrays")
]


def print_all():
    print("** ALL COMMENTS & QUESTIONS **")
    for cq in comments_list:
        cq.print_info()



def print_unflagged():
    print("** UNFLAGGED COMMENTS & QUESTIONS **")
    for cq in comments_list:
        if not cq.is_flagged:
            cq.print_info()



def average_engagement():
    total_likes_dislikes = sum(comment.likes + comment.dislikes for comment in comments_list)
    average = total_likes_dislikes / len(comments_list)
    print(f"AVERAGE ENGAGEMENT: {average} likes and dislikes per comment")


print_all()
print_unflagged()
average_engagement()
