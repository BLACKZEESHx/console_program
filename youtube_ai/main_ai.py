# import pyshorteners
# link = input("Enter the link: ")
# shortener = pyshorteners.Shortener(debug=True)
# short_url = shortener.tinyurl.short(link)
# print(short_url)
# exit()
from pytube import YouTube, Search
from print_with_color import bcolors
from write_stylish import write_like_gpt


def Download(url_video:str,output_path:str) -> str:
    video = YouTube(url_video)
    try:
        write_like_gpt("Download in progress...")
    # Get the highest resolution video stream and download it
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=output_path)
        write_like_gpt(bcolors.UNDERLINE + "------------------------- 100% complete")
    except Exception as e:
        write_like_gpt("something goes wrong...")
def search(query:str) -> str:
    # Create a search object
    search = Search(query)

    # Get a list of videos that match the query
    videos = search.results

    # Print information about each video
    for video in videos:
        print("Title:", video.title)
        print("Description:", video.description)
        print("Thumbnail URL:", video.thumbnail_url)
        print("Video URL:", video.watch_url)
        print("Channel Name:", video.channel_id)
        print("Channel URL:", video.channel_url)
        print("Views:", video.views)
        print("Duration:", video.length)
        print("--------------------")

def Video_Detail(url:str) -> str: 
    # Create a YouTube object and retrieve video metadata
    video_url = url # Replace with your desired video URL
    video = YouTube(video_url)
    video_title =  video.title
    video_description =  video.description
    video_thumbnail_url =  video.thumbnail_url
    channel_id =  video.channel_id
    channel_url =  video.channel_url
    video_keyword =  video.keywords
    video_views =  video.views
    author =  video.author
    duration = video.length
    rates = video.rating
    # Print the video metadata
    print("Title:",  video_title)
    print("Description:",  video_description)
    print("Rates:",  rates)
    print("Thumbnail URL:",  video_thumbnail_url)
    print("Channel Id:",  channel_id)
    print("Channel url:",  channel_url)
    print("Video keywords:",  video_keyword)
    print("Total Views:",  video_views)
    print("Author:",  author)

Video_Detail(url="https://www.youtube.com/shorts/s-MsZo02dos")
# search("BLACKZEESH")
# Download("https://www.youtube.com/watch?v=QqtWzWf3hmE",output_path="Videos")