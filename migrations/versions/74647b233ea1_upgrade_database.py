"""upgrade database

Revision ID: 74647b233ea1
Revises: 91054541ff7b
Create Date: 2020-10-28 18:41:43.897788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74647b233ea1'
down_revision = '91054541ff7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_report',
    sa.Column('reportID', sa.Integer(), nullable=False),
    sa.Column('articleID', sa.Integer(), nullable=True),
    sa.Column('communityID', sa.Integer(), nullable=True),
    sa.Column('articleType', sa.String(length=50, collation='utf8_unicode_ci'), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=50, collation='utf8_unicode_ci'), nullable=True),
    sa.Column('content', sa.String(length=5000, collation='utf8_unicode_ci'), nullable=True),
    sa.Column('reportNum', sa.Integer(), nullable=True),
    sa.Column('reportUser', sa.String(length=50, collation='utf8_unicode_ci'), nullable=True),
    sa.PrimaryKeyConstraint('reportID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_report')
    # ### end Alembic commands ###
