def solution(genres, plays):
    answer = []
    genres_cnt = {}
    for i in range(len(genres)):
        if genres[i] in genres_cnt:
            genres_cnt[genres[i]] += plays[i]
        else:
            genres_cnt[genres[i]] = plays[i]
    d = []
    for i in range(len(genres)):
        d.append((i, genres_cnt[genres[i]], plays[i], genres[i]))
    d.sort(key=lambda x: (x[1], x[2], -x[0]),
          reverse=True)
    genres_in = {}
    for g in genres:
        genres_in[g] = 0
    for dd in d:
        if genres_in[dd[3]] < 2:
            answer.append(dd[0])
            genres_in[dd[3]] += 1
    return answer