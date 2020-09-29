from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, Log
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, LogSerializer, AlbumCommentSerializer, SongCommentSerializer
from random import sample
from datetime import datetime
import math


class TimeRecommend(APIView):
    def get(self, request):
        now = datetime.now()
        hour = now.hour
        print(f'hour: {hour}')
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
                logs = Log.objects.filter(user=request.user, time__hour__range=(0, 7))
            elif 7 <= hour < 11:
                logs = Log.objects.filter(user=request.user, time__hour__range=(7, 11))
            elif 12 <= hour < 14:
                logs = Log.objects.filter(user=request.user, time__hour__range=(12, 14))
            elif 20 <= hour <= 23:
                logs = Log.objects.filter(user=request.user, time__hour__range=(20, 24))
            else:
                logs = Log.objects.filter(user=request.user)

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
                rest = 18 - len(logs_all)
                rest_sad = int(math.ceil(rest*0.6))
                rest_sad_all = sad_songs_all.exclude(pk__in=sad_selected_nums, like__lt=500)
                rest_sad_sample = sample(range(len(rest_sad_all)), rest_sad)
                rest_sad_lst = [rest_sad_all[i] for i in rest_sad_sample]

                rest_love = rest - rest_sad
                rest_love_all = love_songs_all.exclude(pk__in=love_selected_nums, like__lt=500)
                rest_love_sample = sample(range(len(rest_love_all)), rest_love)
                rest_love_lst = [rest_love_all[i] for i in rest_love_sample]

                songs_all = logs_all + rest_sad_lst + rest_love_lst
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
            sad_songs_all = Song.objects.filter(type__exact='sad').exclude(like__lt=500)
            love_songs_all = Song.objects.filter(type__exact='love').exclude(like__lt=500)
            joy_songs_all = Song.objects.filter(type__exact='joy').exclude(like__lt=500)

            if 0 <= hour < 7:
                sad_sample = sample(range(len(sad_songs_all)), 13)
                love_sample = sample(range(len(love_songs_all)), 5)
                all = [sad_songs_all[i] for i in sad_sample] + [love_songs_all[i] for i in love_sample]

            elif 7 <= hour < 11:  # 신나는 노래 + 설레는 노래
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
                all = [love_songs_all[i] for i in love_sample] \
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