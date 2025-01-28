from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from app import app, db
from app.models import User, Video
from app.forms import VideoForm

main = Blueprint("main", __name__)

@main.route("/")
def index():
    videos = Video.query.all()
    return render_template("index.html", videos=videos)

@main.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    form = VideoForm()
    if form.validate_on_submit():
        file = form.video_file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        video = Video(
            title=form.title.data,
            description=form.description.data,
            filename=filename,
            user_id=current_user.id
        )
        db.session.add(video)
        db.session.commit()
        flash("Video subido correctamente!", "success")
        return redirect(url_for("main.index"))
    return render_template("upload.html", form=form)

@main.route("/watch/<int:video_id>")
def watch(video_id):
    video = Video.query.get_or_404(video_id)
    return render_template("watch.html", video=video)