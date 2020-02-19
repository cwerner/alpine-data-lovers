import streamlit as st

events = {0: "Introduction",
          1: "#01 - Web visualisation",
          2: "#02 - Dimensionality reduction",
          3: "#03 - TBA"}


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
            ### {self.title}

            **{self.speaker}** ({self.speaker_affiliation})
            """)

        st.info(f"**Summary:** {self.summary}")
        if self.video_url:
            st.error("Video not yet uploaded")
            st.video(self.video_url, start_time=30)
        
        if self.resources:
            st.warning(self.resources)
    

talks = {}


t1 = Talk("Visualizing large gridded data sets on the web with Bokeh Server",
          "[Christian Chwala](https://www.imk-ifu.kit.edu/staff_Christian_Chwala.php)", 
          "IMK-IFU/ University of Augsburg",
          """\
              As datasets get larger and larger, it becomes more important
              to provide interactive exploration tools on the web instead
              of download links. Using a combination of *bokeh* server
              and *xarray* it is easy to provide web visualization of
              large local and remote data sets. This talk gives a short
              introduction and some examples using gridded weather radar data.""",
          resources="[GitHub link](https://github.com/cchwala/bokeh_examples_ifu_meetup), "
                    "[Slides](https://minio.cwerner.ai/adl/meetup-01/slides/adl01_chwala-bokeh_slides.pdf), "
                    "Resources: [Bokeh](https://docs.bokeh.org/en/latest/), "
                    "[Xarray](http://xarray.pydata.org/en/stable/)", 
          video_url="https://www.youtube.com/watch?v=BHACKCNDMW8")

t2 = Talk("Streamlit - creating custom ML/ DS tools fast",
          "[Christian Werner](https://www.imk-ifu.kit.edu/staff_Christian_Werner.php)", 
          "IMK-IFU",
          """\
              In the last years more and more options to create and deploy data driven
              apps emerged in the Python ecosystem. One of the newest contenders is
              *streamlit*. It promises to get you from your data or analysis to a nice
              functional deployed app in days instead of months. I'll quickly introduce
              this new library and demo some simple apps.""",
          resources="[GitHub link](https://github.com/cwerner/adl01_streamlit-demo), "
                    "[Slides](https://minio.cwerner.ai/adl/meetup-01/slides/adl01_werner-streamlit_slides.pdf), "
                    "Resources: [Streamlit](https://www.streamlit.io)",
          video_url="https://www.youtube.com/watch?v=BHACKCNDMW8")

t3 = Talk("Observation monitoring and time series visualization with Grafana",
          "[Benjamin Fersch](https://www.imk-ifu.kit.edu/staff_Benjamin_Fersch.php)", 
          "IMK-IFU",
          """\
              Time variant processes are important in many scientific disciplines, 
              in particular for environmental and ecosystem or climate research.
              Time series data are gathered from observations with diverse techniques
              and sensors but also from modeling. Grafana is a tool to easily
              visualize, aggregate and compare such data based on the users
              requirements. It can be used to monitor sensor recordings,
              from computer systems to field stations. In this talk, we will
              see various applications that visualize data from a time series database.
              """,
          resources="Sorry - no slides, Resources: [Grafana](https://grafana.com), [InfluxDB](https://www.influxdata.com)",
          video_url="https://www.youtube.com/watch?v=BHACKCNDMW8")

t4 = Talk("Reducing the dimension of your data - How losing information leads to finding information",
          "[Julius Polz](https://www.imk-ifu.kit.edu/staff_Julius_Polz.php)", 
          "IMK-IFU",
          """\
              It can be challenging to find latent features in high dimensional data like
              images or chunks of a time-series. Dimension reduction techniques like UMAP
              or t-SNE can be used to project the high dimensional data to a lower dimensional
              representation which we can visualize and which still contains useful information
              about the global shape of the data. In this meetup, we will talk about how such
              unsupervised learning techniques can be used to find outliers and similarities
              in the data. Our example will be the attenuation time-series of commercial microwave
              links, which are used to derive information about rainfall.
              """
          resources="[GitHub link](https://github.com/jpolz/cml_umap_example), " +\
                    "[Slides](https://minio.cwerner.ai/adl/meetup-01/slides/adl01_werner-streamlit_slides.pdf), "+\
                    "Resources: [UMAP-learn](https://umap-learn.readthedocs.io/en/latest/), "+\
                    "[T-SNE](https://lvdmaaten.github.io/tsne/), "+\
                    "[Reading](https://onlinelibrary.wiley.com/doi/full/10.1002/wat2.1337)",
          video_url="https://www.youtube.com/watch?v=BHACKCNDMW8")




talks["01-01-Chwala"] = t1
talks["01-02-Werner"] = t2
talks["01-03-Fersch"] = t3
talks["02-01-Polz"]   = t4
       

def event01():
    st.markdown("""\
        ## Web tools for effective data visualisation

        Location: [`KIT Campus Alpin, IMK-IFU, Garmisch-Partenkirchen`](https://www.imk-ifu.kit.edu)  
        Date: `22.01.2020 6-9pm`  
        Meetup: [event link](https://www.meetup.com/alpine-data-lovers/events/267293349/)

        """)
    
    for _id, talk in talks.items():
        if _id[0:2] == '01':
            talk.render()
            st.markdown("""\
                ---  
                """)

def event02():
    st.markdown("""\
        ## Reducing the dimensionality of your data

        Location: [`KIT Campus Alpin, IMK-IFU, Garmisch-Partenkirchen`](https://www.imk-ifu.kit.edu)  
        Date: `19.02.2020 6-9pm`  
        Meetup: [event link](https://www.meetup.com/alpine-data-lovers/events/268269575/)

        """)

    for _id, talk in talks.items():
        if _id[0:2] == '02':
            talk.render()
            st.markdown("""\
                ---  
                """)


def event03():
    st.markdown("""\
        ## TBA

        Location: [`KIT Campus Alpin, IMK-IFU, Garmisch-Partenkirchen`](https://www.imk-ifu.kit.edu)  
        Date: `18.03.2020 6-9pm`

        """)

event = {1: event01, 2: event02, 3: event03}

def main():
    st.title("Alpine Data Lovers - Meetup :mountain:")
    page = st.empty()
    selection = st.sidebar.selectbox("Events", [0, 1, 2, 3], 0, format_func=events.get)

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
