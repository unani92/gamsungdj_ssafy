        // async fetchYoutubeId(song) {
        //   const { data } = await axios.get(youtubeURL, {
        //     params: {
        //       key: API_KEY,
        //       part: 'snippet',
        //       maxResults: 1,
        //       type: 'video',
        //       q: song.artist[0].name + ' ' + song.name
        //     }
        //   })
        //   const { items } = data
        //   const { videoId } = items[0].id
        //   const reqData = {'src': videoId}
        //   song['src'] = videoId
        //   await http.post(`addsrc/${song.id}/`, reqData,'')
        // },
        // async addToPlaylistAndPlay(data) {
        //   if (data['src']) {
        //     this.playlist.unshift(data)
        //     this.$store.state.playerControl = "add"
        //     this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        //   } else {
        //     await this.fetchYoutubeId(data)
        //     this.playlist.unshift(data)
        //     this.$store.state.playerControl = "add"
        //     this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        //   }
        // },
                // async addToPlaylist(data) {
        //     if (data['src']) {
        //         this.playlist.push(data)
        //         this.$notify('primary', "재생 목록에 추가 었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        //     }
        //     else {
        //         await this.fetchYoutubeId(data)
        //         this.playlist.push(data)
        //         this.$notify('primary', "재생 목록에 추가 었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        //     }
        // },
