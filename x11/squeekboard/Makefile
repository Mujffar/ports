PORTNAME=	squeekboard
DISTVERSIONPREFIX=	v
DISTVERSION=	1.17.1
PORTREVISION=	6
CATEGORIES=	x11 wayland

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	On-screen keyboard for Wayland
WWW=		https://gitlab.gnome.org/World/Phosh/squeekboard

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

BROKEN_FreeBSD_12_powerpc64=	fails to compile: rs.e2mg9us3-cgu.14:(.text.imservice_handle_commit_state+0x228): undefined reference to 'eekboard_context_service_show_keyboard'
BROKEN_FreeBSD_13_powerpc64=	fails to link: ld: error: undefined symbol: eekboard_context_service_get_overlay

BUILD_DEPENDS=	wayland-protocols>=1.12:graphics/wayland-protocols
LIB_DEPENDS=	libfeedback-0.0.so:accessibility/feedbackd \
		libwayland-client.so:graphics/wayland \
		libcroco-0.6.so:textproc/libcroco \
		libxkbcommon.so:x11/libxkbcommon
RUN_DEPENDS=	gsettings-desktop-schemas>0:devel/gsettings-desktop-schemas

USES=		cargo compiler:c11 gettext-tools gnome meson pkgconfig python:build shebangfix
USE_GITLAB=	yes
USE_GNOME=	cairo gdkpixbuf2 gnomedesktop3 gtk30
GL_SITE=	https://gitlab.gnome.org
GL_ACCOUNT=	World/Phosh
GL_COMMIT=	2faa98d85f1142383ec8ad1487616c1a7ad1882f
SHEBANG_FILES=	tools/entry.py
MAKE_ENV=	${CARGO_ENV}
CARGO_BUILD=	no
CARGO_INSTALL=	no
CARGO_TEST=	no
TARGET_ORDER_OVERRIDE=	750:cargo-configure
CARGO_CARGOTOML=	${BUILD_WRKSRC}/Cargo.toml
MESON_ARGS=	-Dstrict=false
MESON_ARGS+=	-Donline=false # XXX Cargo.lock
PLIST_FILES=	bin/${PORTNAME} \
		bin/${PORTNAME}-entry \
		bin/${PORTNAME}-test-layout \
		share/applications/sm.puri.Squeekboard.desktop \
		share/locale/ca/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/de/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/fa/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/fi/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/fur/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/gl/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/he/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/nl/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/pt_BR/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/ro/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/sl/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/sv/LC_MESSAGES/${PORTNAME}.mo \
		share/locale/uk/LC_MESSAGES/${PORTNAME}.mo \
		${NULL}

post-patch:
# Make each cargo subcommand very verbose
	@${REINPLACE_CMD} -e '/^cargo/s/"$$@"/--verbose --verbose &/' \
		${WRKSRC}/cargo.sh

post-configure:
# Provide preprocessed Cargo.toml for USES=cargo
	@${DO_MAKE_BUILD} -C ${BUILD_WRKSRC} Cargo.toml

.include <bsd.port.mk>
