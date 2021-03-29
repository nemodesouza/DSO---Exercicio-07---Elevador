from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
  def __init__(self):
    self.__elevador = None


  @property
  def elevador(self) -> Elevador:
    return self.__elevador


  def subir(self) -> str:
    try:
      self.__elevador.subir()
    except Exception as e:
        print(e)

  def descer(self) -> str:
    try:
      self.__elevador.descer()
    except Exception as e:
        print(e)
  
  def entra_pessoa(self) -> str:
    try:
      self.__elevador.entra_pessoa()
    except Exception as e:
        print(e)

  def sai_pessoa(self) -> str:
    try:
      self.__elevador.sai_pessoa()
    except Exception as e:
        print(e)
        
  
  def inicializar_elevador(self, andar_atual:int, total_andares_predio: int,\
      capacidade: int, total_pessoas: int): #verificar se o espaço não vai matar o depurador
      if isinstance (andar_atual, int) and isinstance (total_andares_predio, int) and\
      isinstance (capacidade, int) and isinstance (total_pessoas, int) and andar_atual >= 0 and total_andares_predio >= 0 and capacidade >= 0 and\
      total_pessoas >= 0 and andar_atual <= total_andares_predio and total_pessoas <= capacidade:
        self.__elevador = Elevador(andar_atual, total_andares_predio, \
        capacidade, total_pessoas)
      else:
        raise ComandoInvalidoException

