class GiverErrors(Exception):
    pass


class UserNotFoundError(GiverErrors):
    name = 'user.not_found'


class IncorrectScoreError(GiverErrors):
    name = 'score.incorrect'
