"""artifact table: add file_size_bytes

Revision ID: 5b7ef0b1e875
Revises: b40098600646
Create Date: 2022-06-30 14:21:12.687380+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '5b7ef0b1e875'
down_revision = 'b40098600646'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artifact', sa.Column('file_size_bytes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artifact', 'file_size_bytes')
    # ### end Alembic commands ###
