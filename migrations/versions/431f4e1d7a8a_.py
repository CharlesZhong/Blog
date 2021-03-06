"""empty message

Revision ID: 431f4e1d7a8a
Revises: 2b586bd1437e
Create Date: 2015-05-08 01:06:57.152959

"""

# revision identifiers, used by Alembic.
revision = '431f4e1d7a8a'
down_revision = '2b586bd1437e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'location')
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'avatar_hash')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###
