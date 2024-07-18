
import pickle
from matplotlib import image 
import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu

# Import Dataset
airline = pd.read_csv('data_bersih.csv')
offset = 1
airline.index += offset
airline.index.name = 'No'

# Atur tema Streamlit
st.set_page_config(
    page_title="Klasifikasi Tingkat Kepuasaan Penumpang",
    page_icon=":plane:",
    layout="wide",
    initial_sidebar_state="expanded",
)
# kodingan Sidebar 
with st.sidebar:
    nav = option_menu(
        menu_title="Menu Aplikasi",
        options=["Beranda", "Klasifikasi Kepuasan"],
        icons=["house", "folder"],
        menu_icon="*️⃣",
        default_index=0,
        styles={
            "container": {"background-color": "#EDEDED", "padding": "10px"},
            "icon": {"color": "#DFD7BF", "cursor": "pointer"},
            "nav-link-selected": {"background-color": "#190482"},
        }
    )

if nav == "Beranda":


    # Mengatur efek animasi dan gaya teks menggunakan CSS
    st.markdown(
        """
        <style>
        @keyframes move-text {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .blue-moving-text {
            position: relative;
            white-space: nowrap;
            overflow: hidden;
            animation: move-text 6s linear infinite;
            color: navy !important;
            font-size: 75px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# efek animasi bergerak dari kiri ke kanan dan warna teks biru tua
    # st.markdown("<h1 class='blue-moving-text'>SELAMAT DATANG</h1>", unsafe_allow_html=True)
# Mengatur warna teks menjadi biru tua
    st.markdown(
        """
        <style>
        .blue-text {
            color: navy !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# Menampilkan judul dengan teks biru tua
    # CSS untuk menengahkan teks
    css = """
    h1 {
        font-size: 50px;
        text-align: center;
        color: navy ; /* Warna teks biru */
        margin-top: -25px; 
    }
    """
    # Menggunakan st.markdown untuk menampilkan teks dalam format HTML
    st.markdown(
        "<h1>KLASIFIKASI TINGKAT KEPUASAN PENUMPANG DI MASKAPAI PENERBANGAN🛫</h1>",
        unsafe_allow_html=True
    )
    st.markdown("""
    <p style='text-align: justify;'>👉Aplikasi ini bertujuan untuk membantu dalam mengevaluasi dan mengklasifikasi tingkat kepuasan penumpang supaya dapat menjadi acuan dalam meningkatkan layanan di maskapai penerbangan.</p>
    """, unsafe_allow_html=True)
    # Menambahkan CSS ke dalam aplikasi Streamlit
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    # st.image('airline.jpg')
    # st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("## 📊<span class='navy-text'>DATASET</span>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify;'>Dataset yang digunakan pada penelitian sudah dibersihkan peneliti, berjumlah 96.812 dan memiliki 14 fitur dan 1 label. Dataset ini bersumber dari website kaggle.com tahun 2022, berikut data yang digunakan pada penelitian ini : </p>
    """, unsafe_allow_html=True)
    # st.write="Dataset yang digunakan pada penelitian sudah dibersihkan peneliti, berjumlah 96.812 dan memiliki 14 fitur dan 1 label. Dataset ini bersumber dari website kaggle.com tahun 2022, berikut data yang digunakan pada penelitian ini"
    link_text = "Sumber dataset"
    link_url = "https://www.kaggle.com/datasets/mysarahmadbhat/airline-passenger-satisfaction"
    # Create a hyperlink using st.markdown
    st.markdown(f"[{link_text}]({link_url})")

    st.dataframe(airline)
    st.markdown(
        """
        <style>
        .navy-text {
            color: navy !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("## 🗳️<span class='navy-text'>INFORMASI DATA</span>", unsafe_allow_html=True)
    st.markdown("""* <em>Customer Type</em> (Jenis Pelanggan) - Firts Time (0) Returning(1).
* <em>Type of Travel</em> (Jenis Perjalanan): Perjalanan pribadi(0) atau Perjalanan bisnis(1).
* <em>Class</em> (Kelas Perjalanan): kelas bisnis(0), ekonomi (1), atau ekonomi plus (2).
* <em>Departure Delay</em> (Keterlambatan Keberangkatan): Menyatakan jumlah menit keterlambatan saat keberangkatan.
* <em>Arrival Delay</em> (Keterlambatan Kedatangan): Menyatakan jumlah menit keterlambatan saat kedatangan.
* <em>Inflight wifi service</em> (Layanan Wifi dalam Penerbangan): Tingkat kepuasan terhadap layanan wifi di dalam pesawat(1-5).
* <em>Ease of Online booking</em> (Kemudahan Pemesanan Online): Tingkat kepuasan terhadap kemudahan dalam melakukan pemesanan tiket secara online(1-5).
* <em>Food and drink</em>  (Makanan dan Minuman): Tingkat kepuasan terhadap makanan dan minuman yang disajikan di pesawat(1-5).
* <em>Seat comfort</em> (Kenyamanan Kursi): Tingkat kepuasan terhadap kenyamanan kursi(1-5).
* <em>Inflight entertainment</em>  (Hiburan dalam Penerbangan): Tingkat kepuasan terhadap hiburan yang disediakan di pesawat(1-5).
* <em>On-board service</em> (Layanan di Pesawat): Tingkat kepuasan terhadap layanan yang diberikan di dalam pesawat(1-5).
* <em>Baggage handling</em> (Penanganan Bagasi): Tingkat kepuasan terhadap penanganan bagasi(1-5).
* <em>Inflight service</em> (Layanan dalam Penerbangan): Tingkat kepuasan terhadap layanan di dalam pesawat(1-5).
* <em>Cleanliness</em> (Kebersihan): Tingkat kepuasan terhadap kebersihan(1-5).
* <em>Satisfaction</em> (Kepuasan): Menunjukkan tingkat kepuasan penumpang terhadap maskapai penerbangan, dengan nilai tidak puas/netral (0) dan puas (1).""", unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .navy-text {
            color: navy !important;
        }

        .custom-image {
            margin-bottom: 20px;
        }

        .move-right {
            margin-left: auto;
        }

        .image-container {
            display: flex;
            justify-content: center;
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("##	📈<span class='navy-text'>VISUALISASI</span>", unsafe_allow_html=True)
    
    # Membuat dua baris dengan dua gambar di atas
    col1, col2 = st.columns(2)

    with col1:
        st.image("cmknn.png", width=600, output_format='PNG', use_column_width='always')
        st.markdown("<p style='color: navy; font-weight: bold; text-align: center;'>Confusion Matrix K-NN</p>", unsafe_allow_html=True)

    with col2:
        st.image("cmadaboost.png", width=600, output_format='PNG', use_column_width='always')
        st.markdown("<p style='color: navy; font-weight: bold; text-align: center;'>Confusion Matrix Adaboost</p>", unsafe_allow_html=True)

    # Memindahkan gambar "evaluasi.png" ke bawah
    # Menampilkan gambar line graph
    st.image("linegraph.png", width=600, output_format='PNG')

    st.markdown(
    "<div style='text-align: left; margin-left: 70px;'><p style='color: navy; font-weight: bold;'>Perbandingan nilai akurasi, precision, dan recall K-NN dan Adaboost</p></div>",
    unsafe_allow_html=True
)

    # st.markdown("")
    # st.image("linegraph.png", caption="Perbandingan nilai akurasi, precision, dan recall K-NN dan Adaboost", width=600)
    
    st.markdown('<hr>', unsafe_allow_html=True)
elif nav == "Klasifikasi Kepuasan":
    st.header("MASUKAN NILAI UNTUK MELAKUKAN KLASIFIKASI")
    st.markdown("Nilai 1-3 = Tidak Puas/Netral")
    st.markdown("Nilai 4-5 = Puas")
# membaca model
    with open('adaboost_model.sav', 'rb') as file:
        adaboost_model = pickle.load(file, encoding='utf-8')
    col1, col2 = st.columns(2)
    with col1:
        # st.write("Jenis Pelanggan")
        Customer_Type = st.radio("Masukan tipe Pelanggan! Firts Time(0) Returning(1)", 
                            [0,1], horizontal=True)
    with col1:
        # st.write("Tipe Penerbangan Penumpang")
        Type_of_Travel = st.radio("Masukan tipe penerbangan penumpang! Perjalanan pribadi(0) Perjalanan bisnis(1)", 
                            [0,1], horizontal=True)
    with col1:
        # st.write("Kelas Perjalanan Penumpang ")
        Class = st.radio("Masukan tipe Kelas Perjalanan Penumpang! kelas bisnis(0), ekonomi (1),ekonomi plus (2)", 
                            [0,1,2], horizontal=True)
    with col1:
        Departure_Delay = st.slider("Masukan menit Keterlambatan Keberangkatan!", 0, 120, 0, key = "slider_1")
    with col1:
        Arrival_Delay = st.slider("Masukan menit Keterlambatan Kedatangan!", 0, 120, 0, key = "slider_2")
    with col1:
        # st.write(" Tingkat kepuasan pemesanan Online ")
        Ease_of_Online_Booking = st.radio("Masukan Tingkat kepuasan pemesanan Online!", 
                            [1,2,3,4,5], horizontal=True)
    with col1:
        # st.write("Tingkat kepuasan layanan On-board ")                   
        On_board_Service = st.radio("Masukan Tingkat kepuasan layanan On-board! ",
                            [1,2,3,4,5], horizontal=True)
    with col2:
        # st.write("Tingkat kepuasan kenyamanan kursi")                    
        Seat_Comfort = st.radio("Masukan Tingkat kepuasan kenyamanan kursi! ",
                            [1,2,3,4,5], horizontal=True) 
    with col2:
        # st.write("Tingkat kepuasaan kebersihan ")                  
        Cleanliness = st.radio("Masukan Tingkat kepuasaan kebersihan!",
                            [1,2,3,4,5], horizontal=True)
    with col2:
        # st.write("Tingkat kepuasan makanan dan minuman ")
        Food_and_Drink = st.radio("Masukan Tingkat kepuasan makanan dan minuman!",
                            [1,2,3,4,5], horizontal=True) 
    with col2:
        # st.write("Tingkat kepuasan layanan dalam pesawat ")
        In_flight_Service = st.radio("Masukan Tingkat kepuasan layanan dalam pesawat!",
                            [1,2,3,4,5], horizontal=True)   
    with col2:
        # st.write("Tingkat kepuasan layanan wifi dalam pesawat")
        In_flight_Wifi_Service = st.radio("Masukan Tingkat kepuasan layanan wifi dalam pesawat!", 
                            [1,2,3,4,5], horizontal=True)
    with col2:
        # st.write(" Tingkat kepuasan hiburan dalam pesawat")                  
        In_flight_Entertainment = st.radio("MasukanTingkat kepuasan hiburan dalam pesawat!",
                            [1,2,3,4,5], horizontal=True)
    with col2:
        # st.write("Tingkat kepuasan penanganan bagasi")              
        Baggage_Handling = st.radio("Masukan Tingkat kepuasan penanganan bagasi!", [1,2,3,4,5], key="baggage_handling", horizontal=True)


    adaboost_predict = ''

    if st.button('Klasifikasi Kepuasan'):
        Customer_Type = int(Customer_Type)
        Type_of_Travel = int(Type_of_Travel)
        Class   = int(Class)
        Departure_Delay = float(Departure_Delay)
        Arrival_Delay = float(Arrival_Delay)
        Ease_of_Online_Booking = int(Ease_of_Online_Booking)
        On_board_service = int(On_board_Service)
        Seat_Comfort = int(Seat_Comfort)
        Cleanliness = int(Cleanliness)
        Food_and_Drink = int(Food_and_Drink)
        In_flight_Service = int(In_flight_Service)
        In_flight_Wifi_Service = int(In_flight_Wifi_Service)
        In_flight_Entertainment = int(In_flight_Entertainment)
        Baggage_Handling = int(Baggage_Handling)
        

        adaboost_predict = adaboost_model.predict([[Customer_Type, Type_of_Travel, Class, Departure_Delay , Arrival_Delay , Ease_of_Online_Booking, On_board_Service, Seat_Comfort, Cleanliness, Food_and_Drink, In_flight_Service, In_flight_Wifi_Service, In_flight_Entertainment, Baggage_Handling]])
        
        if adaboost_predict[0] == 0:
            adaboost_predict = ''
            st.image("unsatisfied.jpg", caption="Penumpang dinyatakan Tidak Puas / Netral")
        else :
            adaboost_predict = ''
            st.image("satisfied.jpg", caption="Penumpang Dinyatakan Puas")
    with col1:
        st.write = "Hasil Klasifikasi:", adaboost_predict
