#!/usr/bin/env python
import Pyro.naming
import Pyro.core
import chain

this = "B"
next = "C"

servername="example.chain."+this

daemon=Pyro.core.Daemon()
obj=chain.Chain(this,next)
uri=daemon.register(obj)
ns=Pyro.naming.locateNS()
ns.remove(servername)
ns.register(servername,uri)

# enter the service loop.
print 'Server started',this
daemon.requestLoop()
