
class Listado:
    def __init__(self):
        self.listaDespachos=[]





    #despacha un producto, cambiando su estado de entregado
    def despacharProducto(self, despacho):
        despacho.setDespacho(True)

    #agrega un nuevo despacho a la lista de despachos
    def agregarDespacho(self, despacho):
        self.listaDespachos.append(despacho)

    #elimina un despacho de la lista de despachos
    def eliminarDespacho(self, despacho):
        self.listaDespachos.remove(despacho)

    #busca un despacho en base a al codigo del producto
    def busarDespachoCodigo(self, codigo):
        for despacho in self.listaDespachos:
            if despacho.getProducto().getCodigo() == codigo:
                return despacho

    #busca un despacho en base al rut del cliente
    def buscarDespachoRut(self, rut):
        for despacho in self.listaDespachos:
            if despacho.getCliente().getRut() == rut:
                return despacho

    #muestra los despachos
    def mostrarDespachos(self):
        for despacho in self.listaDespachos:
            informacion="Nombre cliente: " + despacho.getCliente().getNombre() + "Rut cliente: " + despacho.getCliente().getRut() + "Producto: " + despacho.getProducto().getDescripcion() + "Codigo: " + despacho.getProducto().getCodigo() + "Transporte: " + despacho.getTransporte().getTipo() +  "Nombre destinatario: " + despacho.getDestinatario().getNombre() + "Direccion dest: " + despacho.getDestinatario().getDireccionEntrega() + "Fecha de registro: " + despacho.getFecha() + "Estado del despacho: " + despacho.verificarEntrega()
            print(informacion)

    def getLista(self):
        return self.listaDespachos

