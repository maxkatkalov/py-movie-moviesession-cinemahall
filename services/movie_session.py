import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime.datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )

    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    movie_session_to_update = get_movie_session_by_id(session_id)

    if show_time:
        movie_session_to_update.show_time = show_time

    if movie_id:
        movie_session_to_update.movie_id = movie_id

    if cinema_hall_id:
        movie_session_to_update.cinema_hall_id = cinema_hall_id

    movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()