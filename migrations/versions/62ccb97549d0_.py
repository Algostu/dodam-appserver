"""empty message

Revision ID: 62ccb97549d0
Revises: 527c0aa424d8
Create Date: 2020-09-30 20:14:54.260783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62ccb97549d0'
down_revision = '527c0aa424d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school_info', sa.Column('address', sa.String(length=50, collation='utf8_unicode_ci'), nullable=True))
    op.add_column('school_info', sa.Column('contact', sa.String(length=20, collation='utf8_unicode_ci'), nullable=True))
    op.add_column('school_info', sa.Column('gender', sa.Integer(), nullable=True))
    op.add_column('school_info', sa.Column('homePage', sa.String(length=50, collation='utf8_unicode_ci'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('school_info', 'homePage')
    op.drop_column('school_info', 'gender')
    op.drop_column('school_info', 'contact')
    op.drop_column('school_info', 'address')
    # ### end Alembic commands ###
