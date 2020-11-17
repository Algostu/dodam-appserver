"""empty message

Revision ID: dab351751e0f
Revises: c0fb242c5961
Create Date: 2020-11-18 00:43:36.336551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab351751e0f'
down_revision = 'c0fb242c5961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('classNum', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_info', 'classNum')
    # ### end Alembic commands ###
