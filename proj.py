import marimo

__generated_with = "0.11.30"
app = marimo.App(width="medium", layout_file="layouts/proj.grid.json")


@app.cell
def _(mo):
    show_indicatrix = mo.ui.switch(True)
    mo.md(f"Show indicatrix {show_indicatrix}")
    return (show_indicatrix,)


@app.cell
def _(mo):
    show_graticule = mo.ui.switch(True)
    mo.md(f"Show graticule {show_graticule}")
    return (show_graticule,)


@app.cell(hide_code=True)
def _(
    globe,
    graticule,
    indicatrix,
    plt,
    proj,
    show_graticule,
    show_indicatrix,
    world,
):
    _crs = proj.value
    _fig = plt.figure(figsize=(14, 7))
    _ax = _fig.add_subplot(111)
    _ax.set_axis_off()
    globe.to_crs(crs = _crs).plot(ax = _ax, fc = "#00000000", lw = 0)
    world.to_crs(crs = _crs).plot(ax = _ax, ec = "k", lw = 0.5)
    if show_graticule.value:
        graticule.to_crs(crs = _crs).plot(ax = _ax, fc = "#00000000", ec = "#666666", lw = 0.2)
    if show_indicatrix.value:
        indicatrix.to_crs(crs = _crs).plot(ax = _ax, fc = "#ff000040", lw = 0)
    _ax
    return


@app.cell
def _(mo):
    _dict = {
        "WGS84": "+proj=lonlat",
        "Adams World in a Square": "+proj=adams_ws1",
        "Adams World in a Square II": "+proj=adams_ws2",
        "Aitoff": "+proj=aitoff",
        "Apian Globular": "+proj=apian",
        "August Epicycloidal": "+proj=august",
        "Azimuthal Equidistant": "+proj=aeqd",
        "Boggs": "+proj=boggs",
        "Bonne": "+proj=bonne +lat_1=40",
        "Collignon": "+proj=collg",
        "Compact Miller": "+proj=comill",
        "Craster Parabolic (Putnins P4)": "+proj=crast",
        "Denoyer Semi-Elliptical": "+proj=denoy",
        "Eckert I": "+proj=eck1",
        "Eckert II": "+proj=eck2",
        "Eckert III": "+proj=eck3",
        "Eckert IV": "+proj=eck4",
        "Eckert V": "+proj=eck5",
        "Eckert VI": "+proj=eck6",
        "Equal Area Cylindrical": "+proj=cea",
        "Equal Earth": "+proj=eqearth",
        "Euler": "+proj=euler +lat_1=67 +lat_2=75",
        "Fahey": "+proj=fahey",
        "Foucaut": "+proj=fouc",
        "Foucaut Sinusoidal": "+proj=fouc_s",
        "Gall (Gall Stereographic)": "+proj=gall",
        "General Sinusoidal": "+proj=gn_sinu +m=2 +n=3",
        "Goode Homolosine": "+proj=goode",
        "Ginsburg VIII": "+proj=gins8",
        "Hammer & Eckert-Greifendorff": "+proj=hammer",
        "Hatano Asymmetrical Equal Area": "+proj=hatano",
        "Kavrayskiy V": "+proj=kav5",
        "Kavrayskiy VII": "+proj=kav7",
        "Lagrange": "+proj=lagrng",
        "Lambert Azimuthal Equal Area": "+proj=laea",
        "Larrivee": "+proj=larr", 
        "Loximuthal": "+proj=loxim",
        "McBryde-Thomas Flat-Polar Sine (No. 1)": "+proj=mbt_s",
        "McBryde-Thomas Flat-Pole Sine (No. 2)": "+proj=mbt_fps",
        "McBryde-Thomas Flat-Polar Parabolic": "+proj=mbtfpp",
        "McBryde-Thomas Flat-Polar Quartic": "+proj=mbtfpq",
        "McBryde-Thomas Flat-Polar Sinusoidal": "+proj=mbtfps",
        "Miller": "+proj=mill",
        "Mollweide": "+proj=moll", 
        "Natural Earth": "+proj=natearth",
        "Natural Earth II": "+proj=natearth2",
        "Nell": "+proj=nell",
        "Nell-Hammer": "+proj=nell_h",
        "Nicolosi-Globular": "+proj=nicol",
        "Oblated Equal Area": "+proj=oea +m=1 +n=2",
        "General Oblique Transform": "+proj=ob_tran +o_proj=hammer +o_lon_p=40 +o_lat_p=50 +lon_0=60",
        "Ortelius Oval": "+proj=ortel",
        "Patterson": "+proj=patterson",
        "Peirce Quincuncial": "+proj=peirce_q +lon_0=25 +shape=square",
        "Polyconic (American)": "+proj=poly",
        "Putnins P1": "+proj=putp1",
        "Putnins P2": "+proj=putp2",
        "Putnins P3'": "+proj=putp3p",
        "Putnins P4'": "+proj=putp4p",
        "Putnins P5": "+proj=putp5",
        "Putnins P5'": "+proj=putp5p",
        "Putnins P6": "+proj=putp6",
        "Putnins P6'": "+proj=putp6p",
        "Quartic Authalic": "+proj=qua_aut",
        "Rectangular Polyconic": "+proj=rpoly",
        "Robinson": "+proj=robin",
        "Roussilhe Stereographic": "+proj=rouss", 
        "Sinusoidal (Sanson-Flamsteed)": "+proj=sinu",
        "Times": "+proj=times",
        "Tobler-Mercator": "+proj=tobmerc",
        "Two Point Equidistant": "+proj=tpeqd +lat_1=60 +lat_2=65",
        "Urmaev V": "+proj=urm5 +n=0.9 +alpha=2 +q=4",
        "Urmaev Flat-Polar  Stereographic": "+proj=urmfps +n=0.5",
        "van der Grinten": "+proj=vandg",
        "van der Grinten II": "+proj=vandg2",
        "van der Grinten III": "+proj=vandg3",
        "van der Grinten IV": "+proj=vandg4",
        "Vitovsky I": "+proj=vitk1 +lat_1=45 +lat_2=55",
        "Wagner I (Kavrayskiy VI)": "+proj=wag1",
        "Wagner II": "+proj=wag2",
        "Wagner III": "+proj=wag3",
        "Wagner IV": "+proj=wag4",
        "Wagner V": "+proj=wag5",
        "Wagner VI": "+proj=wag6",
        "Werenskiold": "+proj=weren",
        "Winkel I": "+proj=wink1",
        "Winkel II": "+proj=wink2",
    }
    proj = mo.ui.dropdown(options = _dict, value = "WGS84")
    proj
    return (proj,)


@app.cell
def _(geom, gpd, np):
    def get_parallel(lat):
        lons = [-179.9] + list(range(-179, 180)) + [179.9]
        return geom.LineString([(lon, lat) for lon in lons])

    def get_meridian(lon):
        lats = [-89.9] + list(range(-89, 90)) + [89.9]
        return geom.LineString([(lon, lat) for lat in lats])

    def get_graticule(spacing = 15):
        return gpd.GeoSeries(
            [get_parallel(lon) for lon in range(-90, 91, spacing)] +
            [get_meridian(lat) for lat in range(-180, 181, spacing)], crs = 4326)

    def get_globe():
        return gpd.GeoSeries([geom.Polygon([(x, y) for x, y in zip(
            [-180] * 180 + [_ for _ in range(-180, 180)] + 
            [ 180] * 180 + [_ for _ in range(180, -180, -1)],
            [_ for _ in range(-90,90)]      + [ 90] * 360 + 
            [_ for _ in range(90, -90, -1)] + [-90] * 360)])], crs = 4326)

    def get_indicatrix():
        xys = [(x, y) for x in range(-165, 166, 15)
                      for y in range( -75,  76, 15)]
        lats = [xy[1] for xy in xys]
        xy = gpd.GeoSeries([geom.Point(xy) for xy in xys], crs = 4326).to_crs("+proj=merc")
        return gpd.GeoSeries([xy.buffer(3e5 / np.cos(lat * np.pi / 180)) for xy, lat in zip(xy, lats)], crs = "+proj=merc").to_crs(4326)
    return get_globe, get_graticule, get_indicatrix, get_meridian, get_parallel


@app.cell
def _(geom, get_globe, get_graticule, get_indicatrix, gpd):
    world = gpd.read_file("https://raw.githubusercontent.com/DOSull/projection-atlas/refs/heads/main/app/ne.geojson")
    world.geometry = gpd.GeoSeries(
        [geom.LineString(s.exterior).segmentize(1) for s in world.geometry])
    globe = get_globe()
    graticule = get_graticule()
    indicatrix = get_indicatrix()
    return globe, graticule, indicatrix, world


@app.cell
def _():
    import geopandas as gpd
    import shapely.geometry as geom
    import matplotlib.pyplot as plt
    import numpy as np
    return geom, gpd, np, plt


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
