from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

items = []
tags = []

class Priority:
    def __init__(self, priority):
        self.priority_colors = {'low': 'green', 'medium': 'orange', 'high': 'red'}

        self.priority = priority
        self.priority_list = self.create_priority_list(self.priority)
        self.color = self.get_priority_color(self.priority)

    def create_priority_list(self, priority):
        priority_list = ['low', 'medium', 'high']
        priority_list.remove(priority)
        priority_list.insert(0, priority)
        return priority_list

    def get_priority_color(self, priority):
        return self.priority_colors[priority]

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority
        self.priority_list = self.create_priority_list(self.priority)
        self.color = self.get_priority_color(self.priority)




@app.route("/")
def index():
    user = {'username': 'Will'}
    welcome = render_template("welcome.html", title='index', user=user)
    item_list = render_template("item_list.html", items=items)
    item_adder = render_template("adder.html")
    tag_adder = render_template("tag.html",tags = tags)
    return welcome + item_adder + item_list + tag_adder


@app.route("/remove/<int:id>")
def remove(id):
    for i in range(len(items)):
        if items[i]['id'] is id:
            del items[i]
            break
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    item_name = request.form.get("item_name")
    if item_name is not '':
        new_item = {'name': item_name, 'checked': False, 'priority': Priority('medium'), 'tags': '',
                    'id': len(items)}
        items.append(new_item)
    return redirect(url_for("index"))


@app.route("/prioritize/<int:id>", methods=["POST"])
def prioritize(id):
    priority = request.form.get("priority_selection")
    for i in range(len(items)):
        if items[i]['id'] is id:
            items[i]['priority'] = Priority(priority)
    return redirect(url_for("index"))


@app.route("/clear")
def clear():
    unchecked_items = []
    return redirect(url_for("index"))


@app.route("/check/<int:id>", methods=["POST"])
def check(id):
    for i in range(len(items)):
        if items[i]['id'] is id:
            items[i]['checked'] = not items[i]['checked']
    return redirect(url_for("index"))

@app.route("/tag", methods=["POST"])
def addTag():
    tag_name = request.form.get("tag_name")
    if tag_name is not '':
        tags.append(tag_name)
    print(tags)
    return redirect(url_for("index"))

@app.route("/removeTag/<string:tag>", methods=["POST"])
def removeTag(tag):
    tags.remove(tag)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
