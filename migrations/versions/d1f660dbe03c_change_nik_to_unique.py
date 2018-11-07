"""change nik to unique

Revision ID: d1f660dbe03c
Revises: aaee3e81cc53
Create Date: 2018-11-07 13:27:30.178761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f660dbe03c'
down_revision = 'aaee3e81cc53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'data_catin', ['NIK_catin_perempuan'])
    op.create_unique_constraint(None, 'data_catin', ['NIK_catin_laki_laki'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'data_catin', type_='unique')
    op.drop_constraint(None, 'data_catin', type_='unique')
    # ### end Alembic commands ###