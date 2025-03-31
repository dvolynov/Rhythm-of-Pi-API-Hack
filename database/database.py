from sqlalchemy import and_
from .models import SessionLocal, User, Song, Level


class Database:

    def __init__(self):
        self.db = SessionLocal()

    def close_session(self):
        self.db.close()

    def get_user(self, hash: str):
        try:
            return (
                self.db.query(User)
                .filter(User.hash == hash)
                .first()
            )
        finally:
            self.close_session()

    def get_song(self, user_id: int, task_id: str):
        try:
            return (
                self.db.query(Song)
                .filter(and_(Song.user_id == user_id, Song.task_id == task_id))
                .first()
            )
        finally:
            self.close_session()

    def get_levels(self):
        try:
            return (
                self.db.query(Level)
                .order_by(Level.level.asc())
                .all()
            )
        finally:
            self.close_session()

    def get_user_by_ip(self, ip: str):
        try:
            return (
                self.db.query(User)
                .filter(User.ip == ip)
                .first()
            )
        finally:
            self.close_session()

    def add_user(self, ip: str, hash: str):
        try:
            user = self.get_user_by_ip(ip)
            if user:
                return user

            new_user = User(ip=ip, hash=hash)
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except Exception as e:
            self.db.rollback()
            print(f"Error adding user: {e}")
        finally:
            self.close_session()

    def add_song(self, title, duration, tags, url, task_id, image_url, hash):
        try:
            user = self.get_user(hash)
            if not user:
                return None

            song = self.get_song(user.id, task_id)
            if song:
                return song

            new_song = Song(
                title=title,
                duration=duration,
                tags=tags,
                task_id=task_id,
                url=url,
                image_url=image_url,
                user_id=user.id,
            )
            self.db.add(new_song)
            self.db.commit()
            self.db.refresh(new_song)
            return new_song
        except Exception as e:
            self.db.rollback()
            print(f"Error adding song: {e}")
        finally:
            self.close_session()