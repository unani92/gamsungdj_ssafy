from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Song, Log, Genre
from .serializers import SongSerializer
from datetime import datetime
from random import sample, shuffle
import math


class TimeRecommend(APIView):
    def get(self, request):
        now = datetime.now()
        hour = now.hour

        if request.user.is_authenticated:  # logged in user

            # 사용자가 좋아요를 누른 곡은 추천에서 제외
            sad_songs_all = Song.objects.filter(type__exact='sad')\
                .exclude(user_like__in=[request.user])\
                .order_by('-like')
            love_songs_all = Song.objects.filter(type__exact='love')\
                .exclude(user_like__in=[request.user.pk])\
                .order_by('-like')
            joy_songs_all = Song.objects.filter(type__exact='joy')\
                .exclude(user_like__in=[request.user.pk])\
                .order_by('-like')

            # extract all user's logs by time
            if 0 <= hour < 7:
                logs = Log.objects.filter(user=request.user, time__hour__range=(0, 7)).exclude(song__type='no lyric')
            elif 7 <= hour < 11:
                logs = Log.objects.filter(user=request.user, time__hour__range=(7, 11)).exclude(song__type='no lyric')
            elif 12 <= hour < 14:
                logs = Log.objects.filter(user=request.user, time__hour__range=(12, 14)).exclude(song__type='no lyric')
            elif 20 <= hour <= 23:
                logs = Log.objects.filter(user=request.user, time__hour__range=(20, 24)).exclude(song__type='no lyric')
            else:
                logs = Log.objects.filter(user=request.user).exclude(song__type='no lyric')

            # log based recommend
            if logs:
                feelings = [log.song.type for log in logs]
                counts = {'sad': 0, 'joy': 0, 'love': 0}
                for feel in feelings:
                    counts[feel] += 1
                sad_prop = int(counts['sad'] / len(feelings) * 100)
                joy_prop = int(counts['joy'] / len(feelings) * 100)
                love_prop = int(counts['love'] / len(feelings) * 100)

                sad_songs = math.ceil(sad_prop / 100 * 12)
                sad_songs = sample(range(len(sad_songs_all)), sad_songs)
                sad_songs_extracted = [sad_songs_all[i] for i in sad_songs]
                sad_selected_nums = [song.pk for song in sad_songs_extracted]

                joy_songs = math.ceil(joy_prop / 100 * 12)
                joy_songs = sample(range(len(joy_songs_all)), joy_songs)
                joy_songs_extracted = [joy_songs_all[i] for i in joy_songs]
                joy_selected_nums = [song.pk for song in joy_songs_extracted]

                love_songs = math.ceil(love_prop / 100 * 12)
                love_songs = sample(range(len(love_songs_all)), love_songs)
                love_songs_extracted = [love_songs_all[i] for i in love_songs]
                love_selected_nums = [song.pk for song in love_songs_extracted]

                logs_all = sad_songs_extracted + joy_songs_extracted + love_songs_extracted

                # 18개 중 나머지는 슬픈노래, 설레는 노래 중에서 섞어서 추천
                rest_sad = int(math.ceil(18*0.4))
                rest_sad_all = sad_songs_all.exclude(pk__in=sad_selected_nums, like__lt=500)
                rest_sad_sample = sample(range(len(rest_sad_all)), rest_sad)
                rest_sad_lst = [rest_sad_all[i] for i in rest_sad_sample]

                rest_love = int(math.ceil(18*0.3))
                rest_love_all = love_songs_all.exclude(pk__in=love_selected_nums, like__lt=500)
                rest_love_sample = sample(range(len(rest_love_all)), rest_love)
                rest_love_lst = [rest_love_all[i] for i in rest_love_sample]

                rest_joy = int(math.ceil(18 * 0.3))
                rest_joy_all = joy_songs_all.exclude(pk__in=joy_selected_nums, like__lt=500)
                rest_joy_sample = sample(range(len(rest_joy_all)), rest_joy)
                rest_joy_lst = [rest_joy_all[i] for i in rest_joy_sample]

                # 사용자가 좋아요 누른 곡 분석을 통한 추천
                songs_liked = Song.objects.filter(user_like__in=[request.user])
                if songs_liked:
                    liked_types = [song.type for song in songs_liked]
                    liked_genres = [genre.name for song in songs_liked for genre in song.genres.all()]

                    from collections import Counter
                    types_cnt = Counter(liked_types).most_common(2)
                    genres_cnt = Counter(liked_genres).most_common(2)

                    if len(types_cnt) >= 2 and len(genres_cnt) >= 2:
                        genre1 = Genre.objects.get(name__contains=genres_cnt[0][0])
                        genre2 = Genre.objects.get(name__contains=genres_cnt[1][0])
                        rec1 = Song.objects.filter(type=types_cnt[0][0], genres__in=[genre1], like__gt=1000)
                        rec1_sample = sample(range(len(rec1)), 4)
                        rec1 = [rec1[i] for i in rec1_sample]
                        rec2 = Song.objects.filter(type=types_cnt[1][0], genres__in=[genre2], like__gt=1000)
                        rec2_sample = sample(range(len(rec2)),2)
                        rec2 = [rec2[i] for i in rec2_sample]
                        songs_all = rec1 + logs_all + rest_sad_lst + rest_love_lst + rest_joy_lst + rec2
                    else:
                        genre1 = Genre.objects.get(name__contains=genres_cnt[0][0])
                        rec1 = Song.objects.filter(type=types_cnt[0][0], genres__in=[genre1], like__gt=1000)
                        rec1_sample = sample(range(len(rec1)), 4)
                        rec1 = [rec1[i] for i in rec1_sample]
                        songs_all = rec1 + logs_all + rest_sad_lst + rest_love_lst + rest_joy_lst

                else:
                    songs_all = logs_all + rest_sad_lst + rest_love_lst + rest_joy_lst
                shuffle(songs_all)
                serializer = SongSerializer(songs_all, many=True)

            else:  # if user's log not exist
                if 0 <= hour < 7:
                    sad_sample = sample(range(len(sad_songs_all)), 13)
                    love_sample = sample(range(len(love_songs_all)), 5)
                    all = [sad_songs_all[i] for i in sad_sample] + [love_songs_all[i] for i in love_sample]
                elif 7 <= hour < 11:   # 신나는 노래 + 설레는 노래
                    joy_sample = sample(range(len(joy_songs_all)), 12)
                    love_sample = sample(range(len(love_songs_all)), 6)
                    all = [joy_songs_all[i] for i in joy_sample] + [love_songs_all[i] for i in love_sample]
                elif 12 <= hour < 14:
                    joy_sample = sample(range(len(joy_songs_all)), 18)
                    all = [joy_songs_all[i] for i in joy_sample]
                elif 20 <= hour <= 23:
                    love_sample = sample(range(len(love_songs_all)), 11)
                    sad_sample = sample(range(len(sad_songs_all)), 5)
                    joy_sample = sample(range(len(joy_songs_all)), 2)
                    all = [love_songs_all[i] for i in love_sample]\
                          + [sad_songs_all[i] for i in sad_sample] + [joy_songs_all[i] for i in joy_sample]
                else:
                    love_sample = sample(range(len(love_songs_all)), 6)
                    sad_sample = sample(range(len(sad_songs_all)), 6)
                    joy_sample = sample(range(len(joy_songs_all)), 6)
                    all = [love_songs_all[i] for i in love_sample] \
                          + [sad_songs_all[i] for i in sad_sample] + [joy_songs_all[i] for i in joy_sample]
                serializer = SongSerializer(all, many=True)

            return Response({
                'cnt': len(serializer.data),
                'data': serializer.data
            })

        else:  # not logged in

            if 0 <= hour < 7:
                sad_songs = Song.objects.select_related('album').filter(type='sad', like__gt=500)
                love_songs = Song.objects.select_related('album').filter(type='love', like__gt=500)
                sad_sample = sample(range(len(sad_songs)), 13)
                love_sample = sample(range(len(love_songs)), 5)
                all = [sad_songs[i] for i in sad_sample] + [love_songs[i] for i in love_sample]

            elif 7 <= hour < 11:  # 신나는 노래 + 설레는 노래
                joy_songs = Song.objects.select_related('album').filter(type='joy', like__gt=500)
                love_songs = Song.objects.select_related('album').filter(type='love', like__gt=500)
                joy_sample = sample(range(len(joy_songs)), 12)
                love_sample = sample(range(len(love_songs)), 6)
                all = [joy_songs[i] for i in joy_sample] + [love_songs[i] for i in love_sample]
            elif 12 <= hour < 14:
                joy_songs = Song.objects.select_related('album').filter(type='joy', like__gt=500)
                joy_sample = sample(range(len(joy_songs)), 18)
                all = [joy_songs[i] for i in joy_sample]
            elif 20 <= hour <= 23:
                love_songs = Song.objects.select_related('album').filter(type='love', like__gt=500)
                sad_songs = Song.objects.select_related('album').filter(type='sad', like__gt=500)
                joy_songs = Song.objects.select_related('album').filter(type='joy', like__gt=500)

                love_sample = sample(range(len(love_songs)), 11)
                sad_sample = sample(range(len(sad_songs)), 5)
                joy_sample = sample(range(len(joy_songs)), 2)
                all = [love_songs[i] for i in love_sample] \
                      + [sad_songs[i] for i in sad_sample] + [joy_songs[i] for i in joy_sample]
            else:
                all = Song.objects.select_related('album').filter(like__gt=1000)
                all_sample = sample(range(len(all)),18)
                all = [all[i] for i in all_sample]

            serializer = SongSerializer(all, many=True)
            return Response({
                'cnt': len(serializer.data),
                'data': serializer.data
            })

class ClimateRecommend(APIView):
    def get(self, request):

        rain_contains = Song.objects.filter(Q(name__contains='비 ') | Q(name__contains='빗') | Q(name__contains='비가') | Q(name__contains='빗물'))
        rain_cnt = sample(range(len(rain_contains)), 6)
        rain_contains = [rain_contains[i] for i in rain_cnt]
        ballad = Song.objects.filter(Q(type='love') | Q(type='joy'), genres__name__in=['발라드', '국내드라마'])
        ballad_cnt = sample(range(len(ballad)), 12)
        ballad = [ballad[i] for i in ballad_cnt]
        rain_all = rain_contains + ballad
        serializer = SongSerializer(rain_all, many=True)
        shuffle(rain_all)
        return Response(serializer.data)
