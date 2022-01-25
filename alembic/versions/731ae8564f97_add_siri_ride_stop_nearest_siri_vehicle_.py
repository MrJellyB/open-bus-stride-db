"""add siri_ride_stop.nearest_siri_vehicle_location_id

Revision ID: 731ae8564f97
Revises: 57ce9e6f947d
Create Date: 2022-01-25 11:08:20.440830+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '731ae8564f97'
down_revision = '57ce9e6f947d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('siri_ride_stop', sa.Column('nearest_siri_vehicle_location_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('siri_ride_stop', 'nearest_siri_vehicle_location_id')
    # ### end Alembic commands ###
