class MulticonjuntoOrdenado():
   
    def __init__(self):
        """
        Inicializacion del Multiconjunto Ordenado
        """
        self.elemento = []

    def ordenar(self):
        self.quicksort(self.elemento, 0, len(self.elemento)-1)

    def quicksort(self, unaLista, primero, ultimo):
        if primero < ultimo:
            puntoDivision = self.particion(unaLista, primero, ultimo)
            self.quicksort(unaLista, primero, puntoDivision-1)
            self.quicksort(unaLista, puntoDivision + 1, ultimo)
    
    def particion(self, unaLista, primero, ultimo):
        valorPivote = unaLista[primero][0]
        marcaIzq = primero + 1
        marcaDer = ultimo
        hecho = False
        while not hecho:
            while marcaIzq <= marcaDer and unaLista[marcaIzq][0] <= valorPivote:
                marcaIzq = marcaIzq + 1
            while unaLista[marcaDer][0] >= valorPivote and marcaDer >= marcaIzq:
                marcaDer = marcaDer - 1
            if marcaDer < marcaIzq:
                hecho = True
            else:
                temp = unaLista[marcaIzq]
                unaLista[marcaIzq] = unaLista[marcaDer]
                unaLista[marcaDer] = temp
        temp = unaLista[primero]
        unaLista[primero] = unaLista[marcaDer]
        unaLista[marcaDer] = temp
        return marcaDer
    
    def agregar(self, elem):
        """
        Agregar un elemento al multiconjunto
        recuerde que debe quedar en orden
        """
        if self.existe(elem):
            indice = self.devolver_indice(elem)
            self.elemento[indice] = (elem, self.elemento[indice][1] + 1)
        else:
            self.elemento.append((elem,1))
            self.ordenar()

    def quitar(self, elem):
        """
        Borra una ocurrencia del elemento en el multiconjunto
        """
        if self.existe(elem):
            lugar = self.devolver_indice(elem)
            if self.repeticiones_e(elem) > 1:
                self.elemento[lugar] = (self.elemento[lugar][0], self.elemento[lugar][1] - 1)
            else:
                self.eliminar(elem)
    
    def eliminar(self, elem):
         if self.existe(elem):
            del(self.elemento[self.devolver_indice(elem)])

    def busqueda_binaria(self, elem, l: []):
        puntoMedio = len(l) // 2
        if l == []:
            return False
        else:
            if elem == l[puntoMedio][0]:
                return True
            elif elem < l[puntoMedio][0]:
                return self.busqueda_binaria(elem, l[:puntoMedio])
            else:
                return self.busqueda_binaria(elem, l[puntoMedio + 1:])

    def existe(self, elem)->bool:
        """
        Verifica que exista el elemento en el multiconjunto
        """
        return self.busqueda_binaria(elem, self.elemento)


    def primero(self):
        """
        Devuelve el primer elemento del multiconjunto
        """
        return self.elemento[0][0]

    def ultimo(self):
        """
        Devuelve el ultimo elemento del multiconjunto
        """
        return self.elemento[-1][0]

    def devolver_indice(self,elem):
        """
        Devuelve en que orden del multiconjunto se encuentra e
        """
        indice = None
        if self.existe(elem):
            #se pone en una tupla el objeto filter con la tupla buscada
            tupla = tuple(filter(lambda x: x[0] == elem, self.elemento))
            #asigno a indice el numero de la tupla devuelta por filter
            indice = self.elemento.index(tupla[0])
        return indice

    def repeticiones_e(self, elem)->int:
        """
        Cantidad de veces repetidas que aparece el elemento e en el multiconjunto
        """
        if self.existe(elem):
            lugar = self.devolver_indice(elem)
            return self.elemento[lugar][1]
        else:
            return 0

    def devolver_elemento(self,i:int): 
        """
        Devolveme el elemento que esta en el lugar i
        """
        return self.elemento[i][0]

    def es_vacia(self)->bool:
        """
        Devuelve si el multiconjunto es el vacio
        """
        return (self.elemento == [])

    def tamanio(self)->int:
        """
        Devuelve la cantidad de elementos diferentes del multiconjunto
        """
        return len(self.elemento)


    def tamanio_rep(self)-> int:
        """
        Devuelve la cantidad de elementos del multiconjunto contando repeticiones
        """
  
        acumulador = 0 
        for i in self.elemento:
           acumulador += i[1]
        return acumulador 


    def __str__(self):
        """
        Muestra el multiconjunto (hace el print del multiconjunto) (traduccion a string)
        """
        return f'{self.elemento}'

#tests

m = MulticonjuntoOrdenado() # m = {}

assert True == m.es_vacia(), "Multiconjunto es vacio"
m.agregar(1) # m = {1}
assert False == m.es_vacia(), "Multiconjunto no es vacio"
assert 1 == m.tamanio(), "Tamanio del multiconjunto es 1"
assert True == m.existe(1), "El elemento 1 existe en el multiconjunto"
assert False == m.existe(-1), "El elemento -1 existe en el multiconjunto"
m.agregar(1) # m = {1,1}
m.agregar(1) # m = {1,1,1}
assert m.tamanio() == 1, "El multiconjunto tiene un elemento"
assert m.tamanio_rep() == 3, "El multiconjunto tiene un elemento"
assert 3 == m.repeticiones_e(1), "Cantidad de repeticiones del elemento 1 es 3"
assert 0 == m.repeticiones_e(20), "Cantidad de repeticiones del elemento 20 es 0"
m.agregar(2) # m = {1,1,1,2}
m.agregar(3) # m = {1,1,1,2,3}
m.agregar(2) # m = {1,1,1,2,2,3}
assert 2 == m.repeticiones_e(2), "Cantidad de repeticiones del elemento 2 es 2"
m.agregar(5) # m = {1,1,1,2,2,3,5}
assert 5 == m.ultimo(), "El ultimo elemento del multiconjunto es 5"
assert 1 == m.primero(), "El primer elemento del multiconjunto es 1"
m.agregar(3) # m = {1,1,1,2,2,3,3,5}
m.quitar(3) # m = {1,1,1,2,2,3,5}
assert True == m.existe(3), "Borramos solo una ocurrenicia de 3"
assert 1 == m.repeticiones_e(3), "Cantidad de repeticiones del elemento 3 es 1"
m.quitar(3) # m = {1,1,1,2,2,5}
assert False == m.existe(3), "No existe el elemento 3"
m.agregar(1) # m = {1,1,1,1,2,2,5}
m.agregar(15) # m = {1,1,1,1,2,2,5,15}
m.agregar(3) # m = {1,1,1,1,2,2,3,5,15}
m.agregar(20) # m = {1,1,1,1,2,2,3,5,15,20}
m.agregar(18) # m = {1,1,1,1,2,2,3,5,15,18,20}
m.agregar(11) # m = {1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(0) # m = {0,1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(10) # m = {0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert 10 == m.tamanio(), "El multiconjunto tiene 10 elementos distintos"
assert 14 == m.tamanio_rep(), "El multiconjunto tiene 14 elementos contando repeticiones"
assert 5 == m.devolver_indice(10), "El 10 esta en el indice 5"
assert 11 == m.devolver_elemento(6), "El elemento del indice 6 es el 11"
m.agregar(-1) # m = {-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-20) # m = {-20,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert False == m.existe(22), "No existe el elemento 22"
assert 4 == m.repeticiones_e(1), "Cantidad de repeticiones del 1 es 4"
assert -20 == m.primero(), "El primer elemento del multiconjunto es -20"
assert 20 == m.ultimo(), "El ultimo elemento del multiconjunto es 20"