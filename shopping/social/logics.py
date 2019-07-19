import datetime

from social.models import Swiped
from user.models import User

def recommence_user(user):

    today = datetime.date.today()

    max_year = today.year-user.profile.min_dating_age

    min_year = today.year-user.profile.max_dating_age

    # print(max_year,min_year)

    swiped_users = Swiped.objects.filter(uid=user.id).only("sid")

    swiped_sid_list = [s.sid for s in swiped_users]

    rec_user = User.objects.filter(
        location=user.profile.location,
        sex=user.profile.dating_sex,
        birth_year__gte=min_year,
        birth_year__lte=max_year

    ).exclude(id__in = swiped_sid_list)

    print(rec_user.count())
    print(rec_user.query)

    return rec_user


def like_someone(uid,sid):
    Swiped.objects.create(uid=uid,sid=sid)

    if Swiped.is_liked(uid,sid):
        print("friend")








