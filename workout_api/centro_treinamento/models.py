from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario_id: Mapped[int] = mapped_column(Integer, ForeignKey('atletas.pk_id'), nullable=False)
    atleta_id: Mapped[int] = mapped_column(Integer, ForeignKey('atletas.pk_id'), nullable=False)

    proprietario: Mapped['AtletaModel'] = relationship("AtletaModel", foreign_keys=[proprietario_id], back_populates='centro_treinamento_proprietario')
    atleta: Mapped['AtletaModel'] = relationship("AtletaModel", foreign_keys=[atleta_id], back_populates='centro_treinamento_atleta')
