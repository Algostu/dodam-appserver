"""update artilce table to include nickname

Revision ID: 6d3ff436b81b
Revises: f8fc0a8b01b2
Create Date: 2020-10-08 17:19:27.636657

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6d3ff436b81b'
down_revision = 'f8fc0a8b01b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article_all', sa.Column('nickName', sa.String(length=20, collation='utf8_unicode_ci'), nullable=False))
    op.drop_column('article_all', 'isAnonymous')
    op.add_column('article_region', sa.Column('nickName', sa.String(length=20, collation='utf8_unicode_ci'), nullable=False))
    op.drop_column('article_region', 'isAnonymous')
    op.add_column('article_school', sa.Column('nickName', sa.String(length=20, collation='utf8_unicode_ci'), nullable=False))
    op.drop_column('article_school', 'isAnonymous')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article_school', sa.Column('isAnonymous', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('article_school', 'nickName')
    op.add_column('article_region', sa.Column('isAnonymous', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('article_region', 'nickName')
    op.add_column('article_all', sa.Column('isAnonymous', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('article_all', 'nickName')
    # ### end Alembic commands ###