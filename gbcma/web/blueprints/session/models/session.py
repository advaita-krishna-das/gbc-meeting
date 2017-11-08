from flask_socketio import emit

from .chat import SessionChat
from .stages import SessionStages
from .users import SessionUsers


class Session:
    """Represents Session."""
    def __init__(self, session_id):
        """
        Initializes new instance of the Session class.
        :param session_id: Session Id
        """
        self.__session_id = session_id
        self.__stages = SessionStages(self)
        self.__users = SessionUsers(self)
        self.__chat = SessionChat(self)

        # subscribe for aspects' events
        self.__users.changed.subscribe(self.__on_user_state_changed)
        self.__stages.changed.subscribe(self.__on_stage_changed)

    @property
    def session_id(self):
        return self.__session_id

    @property
    def chat(self):
        return self.__chat

    @property
    def stages(self):
        return self.__stages

    @property
    def users(self):
        return self.__users

    def notify(self, event, data, room=None):
        emit(event, data, room=room or self.__session_id)

    def __on_user_state_changed(self, socket_id, user, joined):
        self.notify("stage", self.__stages.current.view, room=socket_id)

    def __on_stage_changed(self, stage):
        self.notify("stage", stage.view)