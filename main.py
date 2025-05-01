import inputdata
import folium
from folium.features import DivIcon
import pandas as pd
import webbrowser


def main():
    start = 50.085, 14.412

    data = pd.DataFrame({
        "lat": inputdata.latitude,
        "lon": inputdata.longitude,
        "name": inputdata.pubname,
        "addr": inputdata.pubaddress,
        "img": [inputdata.Rokoko, inputdata.Pinkasů, inputdata.Irish, inputdata.Tygra, inputdata.Márnice,
                inputdata.Kocoura, inputdata.Hrocha, inputdata.Mål]
    })

    # m = folium.Map(location=start, width=700, height=500, zoom_start=15, min_zoom=5, max_zoom=18, )
    m = folium.Map(location=start, zoom_start=15, min_zoom=10, max_zoom=18, width="100%", height="100%")

    for i in range(0, len(data)):
        folium.Marker(
            location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
            popup=data.iloc[i]['addr'],
            icon=DivIcon(html=f"""<div style="font-size: 12pt;font-family: helvetica;
             color: purple">{data.iloc[i]["name"]}</div>""")).add_to(m)

    tooltip = "Klikk på meg"

    for i in range(0, len(data)):
        html = f"""<div>
            <img src={data.iloc[i]["img"]}>
            <br /><span>{data.iloc[i]["name"]}</span>
            <br /><span>{data.iloc[i]["addr"]}</span>
            </div>"""
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, max_width=300)
        folium.Marker(
            location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
            popup=popup,
            icon=folium.Icon(icon="beer", prefix="fa", color="blue"),
            tooltip=tooltip,
        ).add_to(m)

    title = "Praha 2025"
    title_html = """
                 <h3 align="center" ;"font-size:22px"><b>{}</b></h3>
                 """.format(title)
    m.get_root().html.add_child(folium.Element(title_html))

    # folium.TileLayer('OpenStreetMap', attr='folium.TileLayer').add_to(m)
    # folium.TileLayer('Stamen Toner', attr='folium.TileLayer').add_to(m)
    # folium.TileLayer('Stamen Water Color', attr='folium.TileLayer').add_to(m)
    # folium.TileLayer('cartodbpositron', attr='folium.TileLayer').add_to(m)
    # folium.TileLayer('cartodbdark_matter', attr='folium.TileLayer').add_to(m)
    # folium.LayerControl().add_to(m)

    m.save("index.html")

    webbrowser.open("index.html")


if __name__ == '__main__':
    main()
