PORTNAME=	schismtracker
PORTVERSION=	20221020
CATEGORIES=	audio

MAINTAINER=	ehaupt@FreeBSD.org
COMMENT=	Module tracker editor/player resembling impulse tracker
WWW=		https://schismtracker.org/

LICENSE=	GPLv2

ONLY_FOR_ARCHS=	amd64 armv7 i386 powerpc powerpc64 powerpc64le

USES=		autoreconf compiler:c++11-lib desktop-file-utils localbase \
		python sdl xorg
USE_GITHUB=	yes
USE_SDL=	sdl2
USE_XORG=	x11 xext xv

GNU_CONFIGURE=	yes

# if you touch these make sure configure finds X11/XKBlib.h presence
LDFLAGS+=	`sdl2-config --libs`
LIBS+=		-lm -lX11

PLIST_FILES=	bin/schismtracker \
		man/man1/schismtracker.1.gz \
		share/applications/schism.desktop \
		share/pixmaps/schism-icon-128.png \
		share/pixmaps/schism-itf-icon-128.png

post-patch:
	@${REINPLACE_CMD} \
		-e "s|^\(AC_INIT.*\)\[last_git_commit\]|\1${PORTVERSION}|" \
		-e '/^m4_define.*last_git_commit.*git/d' \
			${WRKSRC}/configure.ac
	@${REINPLACE_CMD} -e '/^schismtracker_LDADD/d' ${WRKSRC}/Makefile.am

post-install:
	${INSTALL_DATA} ${WRKSRC}/sys/fd.org/*.desktop ${STAGEDIR}${DESKTOPDIR}
	${INSTALL_DATA} ${WRKSRC}/icons/schism-icon-128.png \
		${WRKSRC}/icons/schism-itf-icon-128.png \
		${STAGEDIR}${PREFIX}/share/pixmaps

.include <bsd.port.mk>
