# Contributor: Roberto Gea (Alquimista) <alquimistaotaku@gmail.com>

pkgname=scru-hg
pkgver=1.0.0
pkgrel=1
pkgdesc="Screenshot Uploader"
arch=(any)
url=""
license=("MIT")
depends=("python2, scrot")
makedepends=("python2-distribute")
optdepnds=("python2-notify: soporte para notificaciones")
provides=()
conflicts=()
replaces=()
backup=()
source=(https://bitbucket.org/alquimista/scru/get/tip.tar.gz)
options=(!emptydirs)
install=
package() {
  cd $srcdir/$pkgname-$pkgver
  python setup.py install --root=$pkgdir/ --optimize=1
  
  install -D -m644 $srcdir/LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
