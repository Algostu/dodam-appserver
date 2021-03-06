"""update cafeteria

Revision ID: 1012a87c15ba
Revises: 9e58451eef81
Create Date: 2020-10-21 15:15:22.583113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1012a87c15ba'
down_revision = '9e58451eef81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cafeteria_info', sa.Column('month', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cafeteria_info', 'month')
    # ### end Alembic commands ###
