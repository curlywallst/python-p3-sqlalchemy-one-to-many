"""Create Game Model

Revision ID: 085d2b8ebe6a
Revises: 0d06d41c7860
Create Date: 2022-10-05 17:50:19.798924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '085d2b8ebe6a'
down_revision = '0d06d41c7860'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('game_title', sa.String(), nullable=True),
    sa.Column('game_genre', sa.String(), nullable=True),
    sa.Column('game_platform', sa.String(), nullable=True),
    sa.Column('game_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('game_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
