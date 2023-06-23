from dri.timeline_item import TimelineItem
from dri.color import MarkerColor


class Timeline:
    def GetName(self) -> str:
        """
        Returns the timeline name.

        Returns
        -------
        str
            Timeline name

        """
        ...

    def SetName(self, timeline_name) -> bool:
        """
        Sets the timeline name if timelineName (string) is unique. Returns True if
        successful.

        Parameters
        ----------
        timeline_name
            Timeline name to set

        Returns
        -------
        bool
            True if the timeline name was set successfully, False otherwise.

        """
        ...

    def GetStartFrame(self) -> int:
        """
        Returns the frame number at the start of timeline.

        Returns
        -------
        int
            Frame number at the start of timeline

        """
        ...

    def GetEndFrame(self) -> int:
        """
        Returns the frame number at the end of timeline.

        Returns
        -------
        int
            Frame number at the end of timeline

        """
        ...

    def SetStartTimecode(self, timecode: str) -> bool:
        """
        Set the start timecode of the timeline to the string 'timecode'. Returns true
        when the change is successful, false otherwise.

        Parameters
        ----------
        timecode
            Start timecode of the timeline, such as "01:00:00:00".

        Returns
        -------
        bool
            True if the change was successful, False otherwise.

        Examples
        --------
        >>> current_timeline.SetStartTimecode("00:00:00:00")
        True

        """
        ...

    def GetStartTimecode(self) -> str:
        """
        Returns the start timecode for the timeline.

        Returns
        -------
        str
            Start timecode for the timeline

        Examples
        --------
        >>> current_timeline.GetStartTimecode()
        '01:00:00:00'

        """
        ...

    def GetTrackCount(self, track_type: str) -> int:
        """
        Returns the number of tracks for the given track type ("audio", "video" or
        "subtitle").

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")

        Returns
        -------
        int
            Number of tracks for the given track type

        """
        ...

    def AddTrack(self, track_type: str, optional_sub_track_type: str = None) -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio"). Second argument
        optionalSubTrackType is required for "audio".

        optionalSubTrackType can be one of {"mono", "stereo", "5.1", "5.1film",
        "7.1", "7.1film", "adaptive1", ... , "adaptive24"}.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle")
        optional_sub_track_type
            Sub track type ("audio", "video" or "subtitle"). Optional. Can be one of
            "mono", "stereo", "5.1", "5.1film", "7.1", "7.1film", "adaptive1",
            "adaptive2", "adaptive3", ..., "adaptive24".

        Returns
        -------
        bool
            True if the track was added successfully, False otherwise.

        """
        ...

    def DeleteTrack(self, track_type: str, track_index: int) -> bool:
        """
        Deletes track of trackType ("video", "subtitle", "audio") and given
        trackIndex. 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track was deleted successfully, False otherwise.

        """
        ...

    def SetTrackEnable(self, track_type: str, track_index: int, enabled: bool) -> bool:
        """
        Enables/Disables track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        enabled

        Returns
        -------
        bool
            True if the track was enabled/disabled successfully, False otherwise.

        """
        ...

    def GetIsTrackEnabled(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is enabled and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is enabled, False otherwise.

        """
        ...

    def SetTrackLock(self, track_type: str, track_index: int, locked: bool) -> bool:
        """
        Locks/Unlocks track with given trackType and trackIndex.

        trackType is one of {"audio", "video", "subtitle"}.

        trackIndex is in this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).
        locked
            Track locked or not.

        Returns
        -------
        bool
            True if the track was locked/locked successfully, False otherwise.

        """
        ...

    def GetIsTrackLocked(self, track_type: str, track_index: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is locked and False
        otherwise.

        Parameters
        ----------
        track_type
            Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        bool
            True if the track is locked, False otherwise.

        """
        ...

    def DeleteClips(
        self,
        clips: list[TimelineItem],
        ripple_delete: bool = False,
    ) -> bool:
        """
        Deletes specified TimelineItems from the timeline, performing ripple delete
        if the second argument is True. Second argument is optional (The default for
        this is False).

        Parameters
        ----------
        clips
            TimelineItems to delete. Can be
        ripple_delete
            True if the second argument is True.

        Returns
        -------
        bool
            True if the clips were deleted successfully, False otherwise.

        Notes
        -----
        -   If clip have audio, then DeleteClips will only delete the video (which is
            :class:`TimelineItem`), leaving the audio in the timeline.

        """
        ...

    def SetClipsLinked(self, clips: list[TimelineItem], linked: bool) -> bool:
        """
        Links or unlinks the specified TimelineItems depending on second argument.

        Parameters
        ----------
        clips
            TimelineItems to link/unlink.
        linked
            Link or not.

        Returns
        -------
        bool
            True if the clips were linked/unlinked successfully, False otherwise.

        """
        ...

    def GetItemListInTrack(
        self, track_type: str, track_index: int
    ) -> list[TimelineItem]:
        """
        Returns a list of timeline items on that track (based on trackType and
        trackIndex). 1 <= trackIndex <= GetTrackCount(trackType).

        Parameters
        ----------
        track_type
                Track type ("audio", "video" or "subtitle").
        track_index
            Track index. In this range: 1 <= trackIndex <= GetTrackCount(trackType).

        Returns
        -------
        list[TimelineItem]
            Returns a list of TimelineItem on that track.

        """
        ...

    def AddMarker(
        self,
        frame_id: int,
        color: MarkerColor,
        name: str,
        note: str,
        duration: int,
        custom_data: str,
    ) -> bool:
        """
        Creates a new marker at given frameId position and with given marker
        information. 'customData' is optional and helps to attach user specific data
        to the marker.

        Parameters
        ----------
        frame_id
            Frame id of the marker. Frame id = Record Frame -
            :func:`dri.timeline.GetStartFrame`.
        color
            Marker color.
        name
            Marker name.
        note
            Marker note.
        duration
            Marker duration.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was created successfully.

        Notes
        -----
        -   frameId is not source frame, but a Record Frame minus the first frame
            of the current timeline (you can get it through
            :func:`dri.timeline.GetStartFrame`) - 01:00:00:00 (24 fps timeline: 86400,
            25 fps timeline: 90000).
        -   For example: Here is a marker located at record frame 86607. We know that
            current timeline is 24fps, so the first frame is 86400. Here we can get the
            frameId which is 86607 - 86400 = 207.

        """
        ...

    def GetMarkers(self) -> dict[int, dict[str, str | int]]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their
        information.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.

        """
        ...

    def GetMarkerByCustomData(
        self, custom_data: str
    ) -> dict[int, dict[str, str | int]]:
        """
        Returns marker {information} for the first matching marker with specified
        customData.

        Parameters
        ----------
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        dict[int, dict[str, str | int]]
            Dict of all markers and dicts with their information.


        """
        ...

    def UpdateMarkerCustomData(self, frame_id: int, custom_data: str) -> bool:
        """
        Updates customData (string) for the marker at given frameId position.
        CustomData is not exposed via UI and is useful for scripting developer to
        attach any user specific data to markers.

        Parameters
        ----------
        frame_id
            Frame id of the marker.
        custom_data
            Custom data helps to attach user specific data to the marker. Not visible
            in the UI.

        Returns
        -------
        bool
            True if the marker was updated successfully.

        """
        ...

    def GetMarkerCustomData(self, frame_id: int) -> str:
        """
        Returns customData string for the marker at given frameId position.

        Parameters
        ----------
        frame_id
            Frame id of the marker.

        Returns
        -------
        str
            Custom data string.

        """
        ...