import os

from flask import render_template, redirect, url_for, send_from_directory
from flask_login import login_required
from werkzeug.security import safe_join

from models import Rooms
from room import db
from theunderground.encodemii import room_logo
from theunderground.forms import RoomForm
from room import app
from theunderground.operations import manage_delete_item


@app.route("/theunderground/rooms")
@login_required
def list_room():
    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()
    return render_template(
        "room_list.html", rooms=rooms, type_length=len(rooms), type_max_count=30
    )


@app.route("/theunderground/rooms/<room_id>", methods=["GET", "POST"])
@login_required
def edit_room(room_id):
    form = RoomForm()

    if form.validate_on_submit():
        # Encode an image to the appropriate size.
        room_image = room_logo(form.room_logo.data.read())
        # Save to our assets directory.
        path = get_room_dir(room_id) + "/f1234.img"
        file = open(path, "wb")
        file.write(room_image)
        file.close()

        room = Rooms.query.filter_by(room_id=room_id).first()
        if room:
            room.bgm = form.bgm.data
            room.mascot = form.has_mascot.data
            room.contact = form.has_contact.data
            room.intro_msg = form.intro_msg.data
            room.mii_msg = form.mii_msg.data
            room.contact_data = form.contact.data

        db.session.add(room)
        db.session.commit()
        return redirect(url_for("list_room"))

    return render_template("room_edit.html", form=form, room_id=room_id)


@app.route("/theunderground/rooms/create", methods=["GET", "POST"])
@login_required
def create_room():
    form = RoomForm()

    if form.validate_on_submit():
        room_id = Rooms.query.order_by(Rooms.room_id.desc()).first()
        room_id = room_id.room_id + 1

        # Encode an image to the appropriate size.
        room_image = room_logo(form.room_logo.data.read())
        # Save to our assets directory.
        path = get_room_dir(room_id) + "/f1234.img"
        file = open(path, "wb")
        file.write(room_image)
        file.close()

        room = Rooms(
            room_id=room_id,
            bgm=form.bgm.data,
            mascot=form.has_mascot.data,
            contact=form.has_contact.data,
            intro_msg=form.intro_msg.data,
            mii_msg=form.mii_msg.data,
            logo2_id="f1234",
            contact_data=form.contact.data,
        )

        db.session.add(room)
        db.session.commit()
        return redirect(url_for("list_room"))

    return render_template("room_add.html", form=form)


@app.route("/theunderground/rooms/<room_id>/remove", methods=["GET", "POST"])
@login_required
def remove_room(room_id):
    def drop_room():
        db.session.delete(Rooms.query.filter_by(room_id=room_id).first())
        db.session.commit()
        return redirect(url_for("list_room"))

    return manage_delete_item(room_id, "room", drop_room)


@app.route("/theunderground/rooms/<int:room_id>/parade_banner.jpg")
@login_required
def get_parade_banner(room_id):
    return send_from_directory(
        safe_join("assets/special", room_id), "parade_banner.jpg"
    )


@app.route("/theunderground/rooms/<int:room_id>/room_banner.jpg")
@login_required
def get_room_banner(room_id: int):
    return send_from_directory(get_room_dir(room_id), "room_banner.jpg")


def get_room_dir(room_id: int) -> str:
    path = safe_join("assets/special", room_id)

    if not os.path.exists(path):
        os.mkdir(path)

    return path
