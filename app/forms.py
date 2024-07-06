from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SearchField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class TalentoForm(FlaskForm):
    nome = SubmitField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired(),NumberRange(min=0)])
    profissao = StringField('Profissão', validators=[DataRequired()])
    objetivos =  TextAreaField('Objetivos',validators={DataRequired()})
    status_trabalho = SearchField('Status de Trabalho', choices=[('empregado', 'Empregrado'),('desempregado', 'Desempregado')])
    area_formação = StringField('Área de formação', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')