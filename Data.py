from enum import Enum


class FilterFields(Enum):
    ALL = 'All'
    MISSING_PICTURE = 'Missing Picture'
    MISSING_VIDEO = 'Missing Video'
    MISSING_DATE = 'Missing Date'
    MISSING_NUMBER_OF_PLAYERS = 'Missing Number of Players'
    MISSING_RATING = 'Missing Rating'
    MISSING_DEVELOPER = 'Missing Developer'
    MISSING_PUBLISHER = 'Missing Publisher'
    MISSING_DESCRIPTION = 'Missing Description'
    MISSING_GENRE = 'Missing Genre'
    MISSING_REGION = 'Missing Region'
    KID_GAME = 'Kid Game'
    HIDDEN = 'Hidden'
    FAVORITE = 'Favorite'
    NAME = 'Name'
    RATING = 'Rating'
    GENRE = 'Genre'
    REGION = 'Region'
    DATE = 'Date'
    PLAYERS = 'Players'
    PUBLISHER = 'Publisher'
    DEVELOPER = 'Developer'
    DESCRIPTION = 'Desc'

