from flask import Blueprint, render_template, current_app #, session

from app.models.painting import Painting

painting_routes = Blueprint("painting_routes", __name__)

@painting_routes.route("/paintings")
def paintings():
    paintings = Painting.all()
    return render_template("paintings.html", paintings=paintings)
