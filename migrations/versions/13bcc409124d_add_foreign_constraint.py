"""add foreign constraint

Revision ID: 13bcc409124d
Revises: d53b1b2f943f
Create Date: 2020-10-06 08:42:01.413981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bcc409124d'
down_revision = 'd53b1b2f943f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reply', sa.Column('userID', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_reply_userID'), 'reply', ['userID'], unique=False)
    op.create_foreign_key(None, 'reply', 'user_info', ['userID'], ['userID'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reply', type_='foreignkey')
    op.drop_index(op.f('ix_reply_userID'), table_name='reply')
    op.drop_column('reply', 'userID')
    # ### end Alembic commands ###