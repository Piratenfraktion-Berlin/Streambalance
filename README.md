# Streambalance

This is a stream balancer for streams based on Django. It has a public interface for letting people know how many listeners and how many free slots are available. Its currently used on http://stream.piratenfraktion-berlin.de and is considered to be an alpha version.

## Used projects

The interface is based on Twitter Bootsrap which can be found [here](http://twitter.github.com/bootstrap/) 

We also use a slightly modified version of icecast_balancer a Djago App by [FladischerMichael](http://wiki.fladi.at/bin/view/Projects/DjangoIcecastBalancer)

## Status

This project is a working alpha and isn't well engineerd at all. Our target is to make it possible for server owners to add and remove their server over a webinterface and that stream broadcasters can add their stream to be balanced by this service.

## Licence

As always this project is licenced [BSD 2-Clause](http://www.opensource.org/licenses/BSD-2-Clause)
