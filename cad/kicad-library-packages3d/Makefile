PORTNAME=	kicad
PORTVERSION=	6.0.9
CATEGORIES=	cad
MASTER_SITES=	https://gitlab.com/kicad/libraries/${PORTNAME}-packages3D/-/archive/${DISTVERSION}/
PKGNAMESUFFIX=	-library-packages3d
DISTNAME=	${PORTNAME}-packages3D-${DISTVERSION}

MAINTAINER=	cmt@FreeBSD.org
COMMENT=	Official KiCad 3D model libraries for rendering and MCAD integration
WWW=		https://gitlab.com/kicad/libraries/kicad-packages3D

LICENSE=	GPLv2

RUN_DEPENDS=	kicad:cad/kicad

USES=		cmake tar:bz2

CONFLICTS_INSTALL=	kicad-library-packages3d-devel # share/kicad/3dmodels/Battery.3dshapes/BatteryHolder_Bulgin_BX0036_1xC.step

CMAKE_ARGS=	-DLOCALBASE="${LOCALBASE}" \
		-DCMAKE_BUILD_TYPE="Release" \
		-DKICAD_TESTING_VERSION=ON \
		-DKICAD_BUILD_VERSION=${DISTVERSION}
INSTALL_TARGET=	install

NO_ARCH=	yes

.include <bsd.port.mk>
