"""change_gtfs_ride_stop_id_to_bigint

Revision ID: a851bbd0b02d
Revises: 7e9880e6fcf6
Create Date: 2023-12-03 06:46:20.529519+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = 'a851bbd0b02d'
down_revision = '7e9880e6fcf6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('gtfs_ride', 'first_gtfs_ride_stop_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('gtfs_ride', 'last_gtfs_ride_stop_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('gtfs_ride_stop', 'id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.execute('ALTER SEQUENCE gtfs_ride_stop_id_seq AS BIGINT')
    op.execute('SELECT setval(\'gtfs_ride_stop_id_seq\', 2147483648)')


def downgrade():
    raise Exception('Cannot downgrade')
