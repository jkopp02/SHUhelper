"""empty message

Revision ID: 96ca28ceda78
Revises: 4bda8c281f13
Create Date: 2018-05-29 14:39:03.068094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96ca28ceda78'
down_revision = '4bda8c281f13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_class', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('student_class', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('student_class', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student_class', 'updated_at')
    op.drop_column('student_class', 'is_deleted')
    op.drop_column('student_class', 'created_at')
    # ### end Alembic commands ###
