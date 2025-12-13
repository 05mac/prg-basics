class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def dislay_timeline(self):
        print(f'{self.username}, {len(self.posts)}')


profile1 = SocialMediaProfile("johndoe")
profile1.add_post('Hello, world!')
profile1.add_post('Had a great day at the park!')
profile1.add_post("What's up, Natalie? How are you?")
profile1.dislay_timeline()

# def main()
#     pass