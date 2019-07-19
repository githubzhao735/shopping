from libs.https import render_json
from social import logics


def recommence(request):

    user = request.user

    rec_users = logics.recommence_user(user)

    users = [u.to_dict() for u in rec_users]

    return render_json(data = users)

def like(request):

    user = request.user

    sid = request.POST.get("sid")

    logics.like_someone(user.id,sid)
    return render_json()

