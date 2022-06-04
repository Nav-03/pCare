from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# relationship table for evnt table and coordinator table
Event_Coordinator = db.Table('association',
                             db.Column("event_id", db.Integer, db.ForeignKey(
                                 "event.id"), primary_key=True),
                             db.Column("coordinator_id", db.Integer, db.ForeignKey(
                                 "coordinator.id"), primary_key=True)
                             )


class Coordinator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    event = db.relationship("Event",
                            secondary=Event_Coordinator)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'Coordinator : {self.email}'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


# relationship table for guest table and permission table
GuestPermission = db.Table('guest_association',
                           db.Column("guest_id", db.Integer, db.ForeignKey(
                               "guest.id"), primary_key=True),
                           db.Column("permission_id", db.Integer, db.ForeignKey(
                               "permission.id"), primary_key=True)
                           )


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.Text)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    permission = db.relationship("Permission",
                                 secondary=GuestPermission)
    event = db.relationship("Event")
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    guest_hash = db.Column(db.String(500), unique=True, nullable=True)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'Guest : {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "guest_hash": self.guest_hash,
            "event_id": self.event_id,
            "email": self.email,
            "name": self.name,
            "image": self.image,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # do not serialize the password, its a security breach
        }


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vip = db.Column(db.Boolean(), unique=False, nullable=False)
    valet = db.Column(db.Boolean(), unique=False, nullable=False)
    dinner = db.Column(db.Boolean(), unique=False, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    guest = db.relationship(Guest,
                            secondary=GuestPermission)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'Permission : {self.guest}'

    def serialize(self):
        return {
            "id": self.id,
            "vip": self.id,
            "valet": self.id,
            "dinner": self.id,
            "event_id": self.event_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # do not serialize the password, its a security breach
        }


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(120), unique=True, nullable=False)
    coordinator = db.relationship("Coordinator",
                                  secondary=Event_Coordinator)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'Event : {self.event_name}'

    def serialize(self):
        return {
            "id": self.id,
            "event_name": self.event_name,
            "guest_id": self.guest_id,
            "event": list(map(lambda x: x.serialize(), self.event)),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class contactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'contactUs : {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "message": self.message,
        }
