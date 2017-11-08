from gbcma.db.comments import CommentsRepository
from gbcma.db.proposals import ProposalsRepository
from gbcma.db.sessions import SessionsRepository
from gbcma.db.users import UsersRepository
from gbcma.db.votes import VotesRepository

proposals = ProposalsRepository()
users = UsersRepository()
sessions = SessionsRepository()
votes = VotesRepository()
comments = CommentsRepository()