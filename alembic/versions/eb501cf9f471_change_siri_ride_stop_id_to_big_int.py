"""change siri_ride_stop_id to big int

Revision ID: eb501cf9f471
Revises: a851bbd0b02d
Create Date: 2024-10-24 17:16:40.993722+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = 'eb501cf9f471'
down_revision = 'a851bbd0b02d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('siri_vehicle_location', 'siri_ride_stop_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('siri_ride_stop', 'id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.execute('ALTER SEQUENCE siri_ride_stop_id_seq AS BIGINT')
    op.execute('SELECT setval(\'siri_ride_stop_id_seq\', 2147483431)')


def downgrade():
    raise Exception('Cannot downgrade')
