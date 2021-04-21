from Topic import Topic
from Obsever import Observer
from TopicSub import TopicSub


def main():
    topic = Topic()

    observer_one = TopicSub("This is my first Sub")
    observer_two = TopicSub("This is my Second Sub")

    topic.subscribe(observer_one)
    topic.subscribe(observer_two)

    topic.set_topic("Crypto News")


if __name__ == "__main__":
    main()