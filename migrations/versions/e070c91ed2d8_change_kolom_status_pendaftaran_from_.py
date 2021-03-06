"""change kolom status pendaftaran from tabl user to table datacatin

Revision ID: e070c91ed2d8
Revises: a197687400d8
Create Date: 2018-11-08 02:38:21.491834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e070c91ed2d8'
down_revision = 'a197687400d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_catin', sa.Column('status_pendaftaran', sa.Enum('Sedang di proses', 'Diterima', name='status_pendaftaran'), nullable=True))
    op.drop_column('user', 'status_pendaftaran')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status_pendaftaran', postgresql.ENUM('Sedang di proses', 'Diterima', name='status_pendaftaran'), autoincrement=False, nullable=True))
    op.drop_column('data_catin', 'status_pendaftaran')
    # ### end Alembic commands ###
