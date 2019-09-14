import json
import facebook

def main():
    token = {"EAAFRWDPyO1IBACTibzRosompw1heuUNbZA5HhNZCxTOzN5zQ8yP1zqON4EEdfh7YmZBBNLfFW2EAGSEAw0JmkLgkix6O7qyKDIzD7CVZAegqKIQI1bq6N6n0XU8ggVnicZB1wZC6X9zMzG6idCID0aGxMsWKv8PdZAoALiLTpDLXfNNWuNMj4aKXu0z2iKyyidUB2KgLN9dtQZDZD"}
    graph = facebook.GraphAPI(token)

    fields = ['email, gender,gender']

    profile = graph.get_object('me', fields=fields)
    print(json.dumps(profile, indent=4))

main()