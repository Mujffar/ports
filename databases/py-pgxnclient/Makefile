PORTNAME=	pgxnclient
PORTVERSION=	1.3.2
PORTREVISION=	1
CATEGORIES=	databases python
MASTER_SITES=	CHEESESHOP

MAINTAINER=	lwhsu@FreeBSD.org
COMMENT=	Command line tool to interact with the PostgreSQL Extension Network
WWW=		https://pgxn.github.io/pgxnclient/

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytest-runner>=0:devel/py-pytest-runner@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}six>0:devel/py-six@${PY_FLAVOR}

USES=		python shebangfix
USE_PYTHON=	autoplist concurrent distutils optsuffix
SHEBANG_FILES=	pgxnclient/libexec/pgxn-*
NO_ARCH=	yes

.include <bsd.port.mk>
