# Contributor: Roberto Gea (Alquimista) <alquimistaotaku@gmail.com>

_name=scru
pkgname=${_name}-hg
pkgver=1
pkgrel=1
pkgdesc="Screenshot Uploader"
arch=(any)
url="https://bitbucket.org/alquimista"
license=("MIT")
depends=("python2" "scrot")
makedepends=("python2-distribute" "mercurial")
optdepnds=("python2-notify: soporte para notificaciones")
source=(http://bitbucket.org/itkach/${pkgname}/get/${pkgver}.tar.bz2)
options=(!emptydirs)
md5sums=() #generate with 'makepkg -g'


build() {
	cd $srcdir/$pkgname
	python setup.py install --root=$pkgdir/ || return 1
}

