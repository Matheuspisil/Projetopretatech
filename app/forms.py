from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, NumberRange, Email

class TalentoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0)])
    profissao = StringField('Profissão', validators=[DataRequired()])
    objetivos = TextAreaField('Objetivos', validators=[DataRequired()])
    status_trabalho = SelectField('Status de Trabalho', choices=[('empregado', 'Empregado'), ('desempregado', 'Desempregado')], validators=[DataRequired()])
    area_formacao = SelectField('Área de Formação', choices=[('exatas', 'Exatas'), ('humanas', 'Humanas'), ('ciencias', 'Ciências'), ('tecnologia', 'Tecnologia'), ('outras', 'Outras')], validators=[DataRequired()])
    cargo_pretendido = SelectMultipleField('Cargo Pretendido', choices=[], validators=[DataRequired()])  # As opções serão preenchidas dinamicamente no template
    cidade = StringField('Cidade', validators=[DataRequired()])
    bairro = StringField('Bairro', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    github = StringField('GitHub')
    linkedin = StringField('LinkedIn')
    submit = SubmitField('Cadastrar')
