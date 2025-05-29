from flask import Flask, render_template, request
import requests  # type: ignore
import random

app = Flask(__name__)

housequotes = ["“You took a chance, you did something great. You were wrong, but it was still great. You should feel great that it was great. You should feel like crap that it was wrong.”", "“We were both wrong, not equally wrong. You were at least six more wronger than me.”", "“Dr. Allison Cameron: Men should grow up. Dr. Gregory House: Yeah, and dogs should stop licking themselves. It's not gonna happen.”",
               "“Dr. Robert Chase: The hematoma caused the coma. Dr. Gregory House: That's a catchy diagnosis. You could dance to that.”", "“I need thirty-six Vicodin and change for a dollar.”", "“There's no 'I' in team. There's a 'me' though, if you jumble it up.”", "“Just because you don't know what the right answer is, maybe there's even no way you could know what the right answer is doesn't make your answer right or even okay. It's much simpler than that. It's just plain wrong.”", "“You talk to God, you're religious; God talks to you, you're psychotic.”", "“Ramona: Hi. I'm having vaginal pain. Dr. Gregory House: Pleasure to meet you.”", "“You want to know how two chemicals interact, do you ask them? No, they're going to lie through their lying little teeth. Throw them in a beaker and apply heat.”", "“Jobs are not being destroyed they are being relocated. The fact that you see that as inherently bad means that you are an irrational patriot. To put it another way: a patriot.”", "“Figuring out who people are takes time. And it takes twice as much time if they're trying to impress you.”", "“Do I get bonus points if I act like I care?”",
               "“Dr. Eric Foreman: 10-year-olds do not have heart attacks. It's got to be a mistake. Dr. Gregory House: Right. The simplest explanation is she's a 40-year-old lying about her age. Maybe an actress trying to hang on”"]

videos = ["bigmoneydog.mp4", "rockeater.mp4",
          "IMGONNAKILLYOU.mp4", "benadryl.mp4", "barbie.mp4", "theoldtestament.mp4"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/uhoh")
def uhoh():
    video = random.choice(videos)
    return render_template("uhh.html", video=video)


@app.route("/joke", methods=['GET', 'POST'])
def joke():
    joke = ""
    quote = ""
    if request.method == "POST":
        response = requests.get("https://icanhazdadjoke.com/",
                                headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = response.json()
            joke = data["joke"]
            quote = random.choice(housequotes)
        else:
            joke = "Could not find joke at this time"
    return render_template("jokegen.html", joke=joke, quote=quote)


@app.route("/search", methods=['GET', 'POST'])
def search():
    joke = None
    first_search = False
    if request.method == "POST":
        first_search = True
        search = request.form.get("jokesearch")
        response = requests.get(f"https://icanhazdadjoke.com/search?term={search}",
                                headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = response.json()
            joke = data["results"]
        else:
            joke = "Could not find joke at this time"
    return render_template("jokesearch.html", joke=joke, first_search=first_search)


if __name__ == "__main__":
    # debug = true enables automatic reload on changes and better error messages
    app.run(debug=True)
