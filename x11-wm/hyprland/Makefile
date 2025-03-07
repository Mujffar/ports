PORTNAME=	hyprland
DISTVERSIONPREFIX=	v
DISTVERSION=	0.18.0beta
CATEGORIES=	x11-wm wayland

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	Dynamic tiling Wayland compositor that doesn't sacrifice on its looks #'
WWW=		https://hyprland.org/

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	evdev-proto>0:devel/evdev-proto \
		wayland-protocols>=1.25:graphics/wayland-protocols \
		wlroots>=0.16.0<0.17.0:x11-toolkits/wlroots
LIB_DEPENDS=	libwayland-server.so:graphics/wayland \
		libwlroots.so:x11-toolkits/wlroots \
		libinput.so:x11/libinput \
		libxkbcommon.so:x11/libxkbcommon

USES=		compiler:c++11-lib gl gnome meson pkgconfig xorg
USE_GCC=	12+:build
USE_GITHUB=	yes
USE_GL=		egl gl
USE_GNOME=	cairo
USE_XORG=	pixman
GH_ACCOUNT=	hyprwm
GH_PROJECT=	Hyprland
LDFLAGS+=	-static-libstdc++ -static-libgcc # avoid libc++ conflict

OPTIONS_DEFINE=	X11
OPTIONS_DEFAULT=X11

X11_USE=		XORG=xcb
X11_MESON_ENABLED=	xwayland

post-patch:
# Extract (snapshot) version from the port instead of meson.build
	@${REINPLACE_CMD} -i .nogit -e "/GIT_BRANCH/s/run_command.*/'main'/" \
		-e "/GIT_COMMIT_HASH/s/run_command.*/'${DISTVERSIONFULL}'/" \
		-e "/GIT_COMMIT_MESSAGE/s/run_command.*/'<unknown>'/" \
		-e "/GIT_DIRTY/s/run_command.*/'portbld'/" \
		${WRKSRC}/meson.build
# Respect PREFIX for wallpapers
	@${REINPLACE_CMD} 's,/usr/share,${DATADIR:H},' \
		${WRKSRC}/src/render/OpenGL.cpp

.include <bsd.port.mk>
