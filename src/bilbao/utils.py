import geopandas as gpd
import shapely


def bbox_to_geometry(bbox):
    """Use shapely.geometry.shape to cast to shapeley geom"""
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [bbox[2], bbox[1]],
                [bbox[2], bbox[3]],
                [bbox[0], bbox[3]],
                [bbox[0], bbox[1]],
                [bbox[2], bbox[1]],
            ]
        ],
    }


def geo_bbox(
    min_lon, min_lat, max_lon, max_lat, src_crs="EPSG:4326", dst_crs="EPSG:4326"
):
    bbox = [min_lon, min_lat, max_lon, max_lat]
    bbox = bbox_to_geometry(bbox)
    bbox = shapely.geometry.shape(bbox)
    return gpd.GeoDataFrame(geometry=[bbox], crs=src_crs).to_crs(dst_crs)
