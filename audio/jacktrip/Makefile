PORTNAME=	jacktrip
DISTVERSIONPREFIX=	v
DISTVERSION=	1.6.6
CATEGORIES=	audio

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	Multi-machine audio network performance over the Internet
WWW=		https://github.com/jacktrip/jacktrip

LICENSE=	MIT GPLv3
LICENSE_COMB=	multi

BUILD_DEPENDS=	help2man:misc/help2man
LIB_DEPENDS=	libjack.so:audio/jack \
		librtaudio.so:audio/rtaudio

USES=		meson compiler:c++17-lang gl pkgconfig qt:5
USE_QT=		core declarative gui network networkauth quickcontrols2 svg websockets widgets buildtools:build
USE_GL=		gl

USE_GITHUB=	yes
GH_TUPLE=	flathub:shared-modules:2c3a597:shared_modules/linux/flatpak/shared-modules \
		x42:weakjack:cddbeec:weakjack/externals/weakjack

#CXXFLAGS+=	`pkg-config --cflags rtaudio`
#LDFLAGS+=	`pkg-config --libs rtaudio`

QMAKE_SOURCE_PATH=	${PORTNAME}.pro

PLIST_FILES=	bin/${PORTNAME} \
		man/man1/jacktrip.1.gz

.include <bsd.port.mk>
