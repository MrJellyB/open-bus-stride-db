from .base import Base

import sqlalchemy.orm


class Route(Base):
    __tablename__ = 'route'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    min_date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    max_date = sqlalchemy.Column(sqlalchemy.Date, index=True)
    line_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    operator_ref = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    siri_published_line_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_short_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_long_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_mkt = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_direction = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_alternative = sqlalchemy.Column(sqlalchemy.String)
    gtfs_agency_name = sqlalchemy.Column(sqlalchemy.String)
    gtfs_route_type = sqlalchemy.Column(sqlalchemy.String)
    is_from_gtfs = sqlalchemy.Column(sqlalchemy.Boolean, index=True)
    route_stops = sqlalchemy.orm.relationship('RouteStop', back_populates='route')
    rides = sqlalchemy.orm.relationship('Ride', back_populates='route')
