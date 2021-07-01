"""A video player class."""

from .video_library import VideoLibrary
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.now_playing_videoid = ''
        self.pause = False
        self.playlists = {}
        self.flagged = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
        return num_videos

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title, reverse=False)
        # print(type(videos))
        for v in videos:
            tags = str(v.tags)
            tags=tags.replace("'","")
            tags=tags.replace(",", "") 
            tags=tags.replace(")", "") 
            tags=tags.replace("(", "") 
            # print(tags)
            # print(type(v))
            print(f"\t {v.title} ({v.video_id}) [{tags}]")


    def play_video(self, video_id):
        video_to_play = self._video_library.get_video(video_id)
        

        video_flagged = False
        if self.flagged:
            for videos_f in self.flagged:
                if video_id.lower() in videos_f:
                    video_flagged = True
                    reason = videos_f[1]
                    break


        if video_flagged:
            print(f"Cannot play video: Video is currently flagged (reason:{reason})")
        elif video_to_play is None:
            print("Cannot play video: Video does not exist") 
        else:
            if self.now_playing_videoid:
                video_playing = self._video_library.get_video(self.now_playing_videoid)
                print(f"Stopping video: {video_playing.title}")
                print(f"Playing video: {video_to_play.title}")
                self.now_playing_videoid = video_id

            else: 
                print(f"Playing video: {video_to_play.title}")
                self.now_playing_videoid = video_id

        self.pause = False

        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if self.now_playing_videoid:
            # remove the current video id from the record
            video_playing = self._video_library.get_video(self.now_playing_videoid)
            print(f"Stopping video: {video_playing.title}")
            self.now_playing_videoid = ''
            self.pause = False
        else: 
            print(f"Cannot stop video: No video is currently playing")

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        num_videos = len(self._video_library.get_all_videos())
        videos = self._video_library.get_all_videos()
        random_index = randint(0, num_videos-1)
        self.play_video(videos[random_index].video_id)
        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.now_playing_videoid:
            video_playing = self._video_library.get_video(self.now_playing_videoid)
            if self.pause == True:
                print(f"Video already paused: {video_playing.title}")
            else:
                print(f"Pausing video: {video_playing.title}")
                self.pause = True
           
        else: 
            print(f"Cannot pause video: No video is currently playing")

        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        video_playing = self._video_library.get_video(self.now_playing_videoid)
        if self.pause:
            self.pause = False
            print(f"Continuing video: {video_playing.title}")
        elif not video_playing:
            print(f"Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")
        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        video_playing = self._video_library.get_video(self.now_playing_videoid)
        if video_playing:
            tags = str(video_playing.tags)
            tags=tags.replace("'","")
            tags=tags.replace(",", "") 
            tags=tags.replace(")", "") 
            tags=tags.replace("(", "") 
            # print(tags)
            if self.pause:
                print(f"Currently playing: {video_playing.title} ({video_playing.video_id}) [{tags}] - PAUSED")
            else:
                print(f"Currently playing: {video_playing.title} ({video_playing.video_id}) [{tags}]")

        else:
            print("No video is currently playing")

        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        for playlist in self.playlists.keys():
            if playlist_name.upper() == playlist.upper():
                print("Cannot create playlist: A playlist with the same name already exists")
                break
        else:
            self.playlists[playlist_name]=[]
            print("Successfully created new playlist: " + playlist_name)
        # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_exists = False
        video_id_exists = False
        for playlist in list(self.playlists.keys()):
            if playlist_name.upper() == playlist.upper():
                playlist_exists = True
                real_playlist_name = playlist
                break
        
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v.video_id.lower() == video_id.lower():
                video_id_exists = True
                video_title = v.title
                break
        video_flagged = False
        if self.flagged:
            for videos_f in self.flagged:
                if video_id.lower() in videos_f:
                    video_flagged = True
                    reason = videos_f[1]
                    break
        if video_flagged:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason:{reason})")
        elif playlist_exists == False:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        
        elif video_id_exists == False:
            print(f"Cannot add video to {playlist_name}: Video does not exist")

        elif video_id.lower() in self.playlists[real_playlist_name]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            self.playlists[real_playlist_name].append(video_id.lower())
            print(f"Added video to {playlist_name}: {video_title}")

        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlists:
            print("Showing all playlists:")
            for keys in sorted(list(self.playlists.keys()), key=str.lower):
                print(f"{keys}")
        else:
            print("No playlists exist yet")

        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = False
        for playlist in list(self.playlists.keys()):
            if playlist_name.upper() == playlist.upper():
                playlist_exists = True
                real_playlist_name = playlist
                break
        if playlist_exists:
            print(f"Showing playlist: {playlist_name}")
            if len(self.playlists[real_playlist_name]) == 0:
                print("\tNo videos here yet")
            else:
                for song in self.playlists[real_playlist_name]:
                    video = self._video_library.get_video(song)
                    tags = str(video.tags)
                    tags=tags.replace("'","")
                    tags=tags.replace(",", "") 
                    tags=tags.replace(")", "") 
                    tags=tags.replace("(", "") 
                    print(f"{video.title} ({video.video_id}) [{tags}]")

        else:
            print(f"\tCannot show playlist {playlist_name}: Playlist does not exist")

        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_exists = False
        video_id_exists = False
        video_exists_in_playlist = False
        for playlist in list(self.playlists.keys()):
            if playlist_name.upper() == playlist.upper():
                playlist_exists = True
                real_playlist_name = playlist
                break
        
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v.video_id.upper() == video_id.upper():
                video_id_exists = True
                video_title = v.title
                break
        if not playlist_exists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        
        elif not video_id_exists:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")

        elif video_id not in self.playlists[real_playlist_name]:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        
        else:
            self.playlists[real_playlist_name].remove(video_id.lower())
            print(f"Removed video from {playlist_name}: {video_title}")
        # print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = False
        
        for playlist in list(self.playlists.keys()):
            if playlist_name.upper() == playlist.upper():
                playlist_exists = True
                real_playlist_name = playlist
                break
        if playlist_exists:
            self.playlists[real_playlist_name] = []
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = False
        for playlist in list(self.playlists.keys()):
            if playlist_name.upper() == playlist.upper():
                playlist_exists = True
                real_playlist_name = playlist
                break
        if playlist_exists:
            self.playlists.pop(real_playlist_name, None)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        # print("deletes_playlist needs implementation")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title, reverse=False)
        matched_id = []
        for v in videos:
            if search_term.lower() in v.title.lower():
                matched_id.append(v.video_id)
        
        if matched_id:
            i = 1
            print(f"Here are the results for {search_term}:")
            for id in matched_id:
                video = self._video_library.get_video(id)
                tags = str(video.tags)
                tags=tags.replace("'","")
                tags=tags.replace(",", "") 
                tags=tags.replace(")", "") 
                tags=tags.replace("(", "") 
                print(f"  {i}) {video.title} ({video.video_id}) [{tags}]")

                i = i+1
            
            print("Would you like to play any of the above? If yes, "
            "specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            option = input()
            # option = input("Would you like to play any of the above? If yes, "
            # "specify the number of the video. \n If your answer is not a valid number, we will assume it's a no.")

            try:
                value = int(option)
                if value > 1 and value < len(matched_id)+1 :
                    self.play_video(matched_id[value-1])
            except ValueError:
                pass

        else:
            print(f"No search results for {search_term}")
            
        
        # print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title, reverse=False)
        matched_id = []
        for v in videos:
            if video_tag.lower() in v.tags:
                matched_id.append(v.video_id)
        
        if matched_id:
            i = 1
            print(f"Here are the results for {video_tag}:")
            for id in matched_id:
                video = self._video_library.get_video(id)
                tags = str(video.tags)
                tags=tags.replace("'","")
                tags=tags.replace(",", "") 
                tags=tags.replace(")", "") 
                tags=tags.replace("(", "") 
                print(f"  {i}) {video.title} ({video.video_id}) [{tags}]")

                i = i+1
            
            print("Would you like to play any of the above? If yes, "
            "specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            option = input()

            try:
                value = int(option)
                if value > 1 and value < len(matched_id)+1 :
                    self.play_video(matched_id[value-1])
            except ValueError:
                pass

        else:
            print(f"No search results for {video_tag}")
           
        # print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        videos = self._video_library.get_all_videos()
        matched = False
        for video_f in self.flagged:
            if video_id.lower() in video_f:
                print("Cannot flag video: Video is already flagged")
                break
        else:
            for v in videos:
                if video_id.lower() in v.video_id:
                    matched = True
                    if flag_reason:
                        self.flagged.append([v.video_id,flag_reason])
                        print(f"Successfully flagged video: {v.title} (reason: {flag_reason})")
                    else:
                        self.flagged.append([v.video_id, "Not supplied"])
                        print(f"Successfully flagged video: {v.title} (reason: Not supplied)")
                    
            if matched == False:
                print("Cannot flag video: Video does not exist")

        # print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

