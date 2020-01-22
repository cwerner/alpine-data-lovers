import streamlit as st

events = {0: "Introduction",
          1: "#01 - Web visualisation",
          2: "#02 - ???"}


class Talk:
    title: str = None
    speaker: str = None
    speaker_affiliation: str = None
    video_url: str = None
    summary: str = None
    resources: str = None

    def __init__(self, title, speaker, speaker_affiliation, summary, 
                 video_url = None, resources = None):
        self.title = title
        self.speaker = speaker
        self.speaker_affiliation = speaker_affiliation

        self.summary = summary
        if video_url:
            self.video_url = video_url
        
        if resources:
            self.resources = resources
    
    def render(self):
        st.markdown(f"""\
            ## {self.title}

            **{self.speaker}** ({self.speaker_affiliation})
            """)

        st.info(f"Summary: {self.summary}")
        if self.video_url:
            st.video(self.video_url)
        
        if self.resources:
            st.warning(self.resources)
    

talks = {}

t1 = Talk("Visualizing large gridded data sets on the web with Bokeh Server",
          "Christian Chwala", 
          "IMK-IFU/ University of Augsburg",
          "Here we'll have a nice summary...",
          resources="[GitHub link](http://github.com/myrepo), [Slides](http://myslides.com)",
          video_url="https://youtu.be/_T8LGqJtuGc")

t2 = Talk("Streamlit - creating custom ML/ DS tools fast",
          "Christian Werner", 
          "IMK-IFU",
          "Here we'll have a nice summary...",
          resources="[GitHub link](https://github.com/cwerner/adl01_streamlit-demo), [Slides](http://myslides.com)",
          video_url="https://youtu.be/_T8LGqJtuGc")

t3 = Talk("Observation monitoring and time series visualization with Grafana",
          "Benjamin Fersch", 
          "IMK-IFU",
          "Here we'll have a nice summary...",
          resources="[Slides](http://myslides.com)",
          video_url="https://youtu.be/_T8LGqJtuGc")

talks["01-01-Chwala"] = t1
talks["01-02-Werner"] = t2
talks["01-03-Fersch"] = t3
       

def event01():
    st.markdown("""\
        ## Web tools for effective data visualisation

        Location: [`KIT Campus Alpin, IMK-IFU, Garmisch-Partenkirchen`](https://www.imk-ifu.kit.edu)  
        Date: `22.01.2020 6-9pm`

        """)
    
    for _, talk in talks.items():
        talk.render()
        st.markdown("""\
            ---  
            """)

def event02():
    st.markdown("""\
        TBA
        """)

event = {1: event01, 2: event02}

def main():
    st.title("Alpine Data Lovers - Meetup :mountain:")
    page = st.empty()
    selection = st.sidebar.selectbox("Events", [0, 1, 2], 0, format_func=events.get)

    if selection == 0:
        page.markdown("""\
            :wave: Hi there!  
            
            Welcome to the landing page of the [**Alpine Data Lovers Meetup**](https://www.meetup.com/alpine-data-lovers). 
            You'll find a list of events, talks and the associated resources (slides, videos, code examples) on this page. 

            :point_left: to go to a specific meetup event, select it over there...
            
            Christian  

            ---  

            """)
        

        st.sidebar.success('Select an event')
        st.balloons()
    else:
        page.empty()
        event[selection]()


if __name__ == "__main__":
    main()
