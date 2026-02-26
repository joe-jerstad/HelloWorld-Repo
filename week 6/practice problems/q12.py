#rewrite simpler

def like_or_dislike(states_lyst):
    state = 'nothing'
    for i in states_lyst:
        if state == 'nothing':
            if i == 'like':
                state = 'like'
            elif i == 'dislike':
                state = 'dislike'
        elif state == 'like':
            if i == 'like':
                state = 'nothing'
            if i == 'dislike':
                state = 'dislike'
        elif state == 'dislike':
            if i == 'like':
                state = 'like'
            if i == 'dislike':
                state = 'nothing'

    return state

print(like_or_dislike(['like', 'dislike', 'dislike']))

