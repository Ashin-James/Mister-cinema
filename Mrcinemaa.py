import google.generativeai as genai

genai.configure(api_key="AIzaSyCoYzJU2VHpaOgBq0CoElAuy_MyRJIhVhw")

model = genai.GenerativeModel("gemini-1.5-flash")

system_prompt = "You are Mister Cinema(not a chatbot), a friendly, humorous, and interactive movie suggester.Ask the user what type of movies they want to watch, and then provide a list of 20 movies in that genre.For each movie, give a brief summary of the story if user asked and also include the IMDb rating. You are Funny,humorous, super interactive and knowledgable .Interact with the user about the movie.Express humouress expression. Chat like a movie-loving friend with a fun sense of humor."
conversation_memory = []

def chat_with_bot(user_input):

    conversation_memory.append(f"You: {user_input}")

    prompt = system_prompt + "\n".join(conversation_memory)

    response = model.generate_content(prompt)

    if hasattr(response, 'text') and response.text:
        bot_response = response.text

        conversation_memory.append(f"Mister Cinema: {bot_response}")
        return bot_response
    else:
        return "I'm sorry, I cannot provide a response to that."

if __name__ == "__main__":
    print("Hi, I am Mister Cinema! Ask me for movie recommendations, I'm here to help make your movie experience awesome!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("It seems like you’re ready to head out! I hope I helped you find some amazing movies to watch. Remember, if you ever need movie recommendations, a good laugh, or just want to chat about films, Mister Cinema is here for you!")
            break
        response = chat_with_bot(user_input)
        print(f"Mister Cinema: {response}")
