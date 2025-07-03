import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium", layout_file="layouts/proj.grid.json")


@app.cell
def _():
    import geopandas as gpd
    import shapely.geometry as geom
    import matplotlib.pyplot as plt
    return geom, gpd, plt


@app.cell
def _(geom, gpd):
    def get_parallel(lat):
        return geom.LineString([(lon, lat) for lon in range(-180, 181)])

    def get_meridian(lon):
        return geom.LineString([(lon, lat) for lat in range(-90, 91)])

    def get_graticule(spacing = 30):
        return gpd.GeoSeries(
            [get_parallel(lon) for lon in range(-90, 91, spacing)] +
            [get_meridian(lat) for lat in range(-180, 181, spacing)], crs = 4326)

    def get_globe():
        return geom.Polygon([(x, y) for x, y in zip(
            [-180] * 181 + [180] * 181,
            [_ for _ in range(-90,91)] + [_ for _ in range(90, -91, -1)])])

    return get_globe, get_graticule


@app.cell
def _(get_globe, get_graticule, gpd):
    world = gpd.read_file("https://raw.githubusercontent.com/DOSull/projection-atlas/refs/heads/main/app/ne.geojson")
    globe = gpd.GeoDataFrame(geometry = gpd.GeoSeries([get_globe()]), crs = 4326)
    graticule = get_graticule()
    return globe, graticule, world


@app.cell
def _(globe, graticule, plt, proj, world):
    _globe_proj = globe.to_crs(crs = proj.value)
    _fig = plt.figure(figsize=(14, 7))
    _ax = _fig.add_subplot(111)
    _ax.set_axis_off()
    _globe_proj.plot(ax = _ax, fc = "#ddeeff", lw = 0.)
    world.to_crs(crs = proj.value).plot(ax = _ax, fc = "#aaeecc")
    graticule.to_crs(crs = proj.value).plot(ax = _ax, fc = "#00000000", ec = "#999999", lw = 0.25)
    _globe_proj.plot(ax = _ax, fc = "#00000000", ec = "k", lw = 0.35)
    return


@app.cell
def _(mo):
    _dict = {
        "Adams World in a Square"  : "+proj=adams_ws1",
        "Adams World in a Square II" : "+proj=adams_ws2",
        "Aitoff"                   : "+proj=aitoff",
        "Apian Globular I"         : "+proj=apian",
        "August Epicycloidal"      : "+proj=august",
        "Bonne"                    : "+proj=bonne +lat_1=30",
        "Ginsburg VIII"            : "+proj=gins8",
        "Hammer-Aitoff"            : "+proj=hammer",
        "Miller"                   : "+proj=mill",
        "Mollweide"                : "+proj=moll", 
        "Natural Earth"            : "+proj=natearth",
        "Natural Earth II"         : "+proj=natearth2",
        "Sinusoidal"               : "+proj=sinu",
        "Times"                    : "+proj=times",
        "van der Grinten"          : "+proj=vandg",
        "van der Grinten II"       : "+proj=vandg2",
        "van der Grinten III"      : "+proj=vandg3",
        "van der Grinten IV"       : "+proj=vandg4",
        "Winkel I"                 : "+proj=wink1",
        "Winkel II"                : "+proj=wink2",
        "Wagner I (Kavrayskiy VI)" : "+proj=wag1",
        "Wagner II"                : "+proj=wag2",
        "Wagner III"               : "+proj=wag3",
        "Wagner IV"                : "+proj=wag4",
        "Wagner V"                 : "+proj=wag5",
        "Wagner VI"                : "+proj=wag6",
        "WGS84"                    : "+proj=lonlat"
    }
    proj = mo.ui.dropdown(options = _dict, value = "WGS84")
    proj
    return (proj,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
