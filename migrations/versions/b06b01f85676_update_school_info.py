"""update school info

Revision ID: b06b01f85676
Revises: 5fb4f46e56b3
Create Date: 2020-10-01 17:31:46.970397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b06b01f85676'
down_revision = '5fb4f46e56b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school_info', sa.Column('regionName', sa.String(length=100, collation='utf8_unicode_ci'), nullable=True))
    op.add_column('school_info', sa.Column('townName', sa.String(length=100, collation='utf8_unicode_ci'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('school_info', 'townName')
    op.drop_column('school_info', 'regionName')
    # ### end Alembic commands ###