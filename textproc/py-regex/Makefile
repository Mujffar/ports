PORTNAME=	regex
DISTVERSION=	2022.9.13
CATEGORIES=	textproc python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	fax@nohik.ee
COMMENT=	Alternative regular expression module, to replace re
WWW=		https://github.com/mrabarnett/mrab-regex

LICENSE=	PSFL

USES=		python:3.6+
USE_PYTHON=	autoplist distutils pytest # 1 test fails, see https://github.com/mrabarnett/mrab-regex/issues/482

TEST_ENV=	${MAKE_ENV} PYTHONPATH=${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}

post-install:
	${STRIP_CMD} ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/regex/_regex*.so

.include <bsd.port.mk>
