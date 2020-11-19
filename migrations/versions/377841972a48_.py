"""empty message

Revision ID: 377841972a48
Revises: 957f9d6b8756
Create Date: 2020-11-19 17:24:14.939498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377841972a48'
down_revision = '957f9d6b8756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contest_info', sa.Column('storedDate', sa.String(length=100, collation='utf8_unicode_ci'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contest_info', 'storedDate')
    # ### end Alembic commands ###
