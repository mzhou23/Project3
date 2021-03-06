from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

items = []
tags = []


class Priority:
    def __init__(self, priority):
        self.priority_colors = {"low": "green", "medium": "orange", "high": "red"}

        if priority not in self.priority_colors:
            self.priority = "medium"
        else:
            self.priority = priority

        self.priority_list = self.create_priority_list(self.priority)
        self.color = self.get_priority_color(self.priority)

    def create_priority_list(self, priority):
        priority_list = ["low", "medium", "high"]
        if priority in priority_list:
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


class Tag:
    def __init__(self, original_tags):

        self.tag = "none"
        self.tag_list = [self.tag]
        self.update_tag_list(original_tags)

    def get_tag(self):
        return self.tag

    def set_tag(self, tag, original_tags):
        self.tag = tag
        self.update_tag_list(original_tags)

    def update_tag_list(self, original_tags):
        self.tag_list = original_tags.copy()
        if self.tag in self.tag_list and self.tag != "none":
            self.tag_list.remove(self.tag)
            self.tag_list.insert(0, self.tag)
            self.tag_list.append("none")
        else:
            self.tag = "none"
            self.tag_list.insert(0, "none")


@app.route("/")
def index():
    date = datetime.now()
    welcome = render_template(
        "welcome.html",
        title="Doddle - To-Do App",
        time=date.strftime("%d/%m/%y\n%H:%M:%S"),
    )
    item_list = render_template("item_list.html", items=items)
    item_adder = render_template("adder.html")
    tag_adder = render_template("tag.html", tags=tags)
    return welcome + item_adder + item_list + tag_adder


@app.route("/remove/<int:id>")
def remove(id):
    for i in range(len(items)):
        if items[i]["id"] == id:
            del items[i]
            break
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    item_name = request.form.get("item_name")
    if len(items) > 0:
        new_id = items[-1]["id"] + 1
    else:
        new_id = 0
    if item_name != "":
        date = datetime.now()
        new_item = {
            "name": item_name,
            "checked": False,
            "priority": Priority("medium"),
            "tag": Tag(tags),
            "id": new_id,
            "time": date.strftime("%d/%m/%H:%M"),
        }
        items.append(new_item)
    return redirect(url_for("index"))


@app.route("/prioritize/<int:id>", methods=["POST"])
def prioritize(id):
    priority = request.form.get("priority_selection")
    for i in range(len(items)):
        if items[i]["id"] == id:
            items[i]["priority"] = Priority(priority)
    return redirect(url_for("index"))


@app.route("/check/<int:id>")
def check(id):
    for i in range(len(items)):
        if items[i]["id"] == id:
            items[i]["checked"] = not items[i]["checked"]
    return redirect(url_for("index"))


@app.route("/addTag", methods=["POST"])
def addTag():
    tag_name = request.form.get("tag_name")
    # remove trailing spaces
    while tag_name[-1] == " ":
        tag_name = tag_name[:-1]
    if (
        tag_name != ""
        and tag_name[-1] != " "
        and tag_name != "none"
        and tag_name not in tags
    ):
        tags.append(tag_name)
        for item in items:
            item["tag"].update_tag_list(tags)
    return redirect(url_for("index"))


@app.route("/removeTag/<string:tag>", methods=["POST"])
def removeTag(tag):
    tags.remove(tag)
    for item in items:
        item["tag"].update_tag_list(tags)
    return redirect(url_for("index"))


@app.route("/tagItem/<int:id>", methods=["POST"])
def tagItem(id):
    tag = request.form.get("tag_selection")
    for i in range(len(items)):
        if items[i]["id"] == id:
            items[i]["tag"].set_tag(tag, tags)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
