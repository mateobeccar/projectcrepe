"""empty message

Revision ID: 2d8d3b10ff1
Revises: 51f5ccfba190
Create Date: 2017-03-18 11:53:13.545407

"""

# revision identifiers, used by Alembic.
revision = '2d8d3b10ff1'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('movies')
    op.drop_table('people')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('first_name', sa.CHAR(), nullable=True),
    sa.Column('last_name', sa.CHAR(length=50), nullable=True),
    sa.Column('gender', sa.CHAR(length=6), nullable=True)
    )
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.CHAR(length=100), nullable=False),
    sa.Column('mpaa', sa.INTEGER(), nullable=True),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.Column('length', sa.INTEGER(), nullable=True),
    sa.Column('budget', sa.INTEGER(), nullable=True),
    sa.Column('critic_average', sa.CHAR(length=10), nullable=True),
    sa.Column('action', sa.BOOLEAN(), nullable=True),
    sa.Column('animation', sa.BOOLEAN(), nullable=True),
    sa.Column('comedy', sa.BOOLEAN(), nullable=True),
    sa.Column('drama', sa.BOOLEAN(), nullable=True),
    sa.Column('documentary', sa.BOOLEAN(), nullable=True),
    sa.Column('romance', sa.BOOLEAN(), nullable=True),
    sa.Column('short', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('person_id', sa.INTEGER(), nullable=True),
    sa.Column('movie_id', sa.INTEGER(), nullable=True),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], )
    )
    ### end Alembic commands ###
