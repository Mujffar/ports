PORTNAME=	lazygit
DISTVERSIONPREFIX=	v
DISTVERSION=	0.36.0
PORTREVISION=	0
CATEGORIES=	devel

MAINTAINER=	meta@FreeBSD.org
COMMENT=	Simple terminal UI for git commands
WWW=		https://github.com/jesseduffield/lazygit

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules
USE_GITHUB=	yes

GH_ACCOUNT=	jesseduffield
GH_TUPLE=	\
		OpenPeeDeeP:xdg:v1.0.0:openpeedeep_xdg/vendor/github.com/OpenPeeDeeP/xdg \
		atotto:clipboard:v0.1.2:atotto_clipboard/vendor/github.com/atotto/clipboard \
		aybabtme:humanlog:v0.4.1:aybabtme_humanlog/vendor/github.com/aybabtme/humanlog \
		cli:safeexec:v1.0.0:cli_safeexec/vendor/github.com/cli/safeexec \
		cloudfoundry:jibber_jabber:bcc4c8345a21:cloudfoundry_jibber_jabber/vendor/github.com/cloudfoundry/jibber_jabber \
		creack:pty:v1.1.11:creack_pty/vendor/github.com/creack/pty \
		davecgh:go-spew:v1.1.1:davecgh_go_spew/vendor/github.com/davecgh/go-spew \
		emirpasic:gods:v1.12.0:emirpasic_gods/vendor/github.com/emirpasic/gods \
		fatih:color:v1.9.0:fatih_color/vendor/github.com/fatih/color \
		fsmiamoto:git-todo-parser:v0.0.2:fsmiamoto_git_todo_parser/vendor/github.com/fsmiamoto/git-todo-parser \
		fsnotify:fsnotify:v1.4.7:fsnotify_fsnotify/vendor/github.com/fsnotify/fsnotify \
		gdamore:encoding:v1.0.0:gdamore_encoding/vendor/github.com/gdamore/encoding \
		gdamore:tcell:v2.5.3:gdamore_tcell_v2/vendor/github.com/gdamore/tcell/v2 \
		go-errors:errors:v1.4.2:go_errors_errors/vendor/github.com/go-errors/errors \
		go-git:gcfg:v1.5.0:go_git_gcfg/vendor/github.com/go-git/gcfg \
		go-git:go-billy:v5.0.0:go_git_go_billy_v5/vendor/github.com/go-git/go-billy/v5 \
		go-logfmt:logfmt:v0.5.0:go_logfmt_logfmt/vendor/github.com/go-logfmt/logfmt \
		go-warnings:warnings:v0.1.2:go_warnings_warnings/vendor/gopkg.in/warnings.v0 \
		go-yaml:yaml:v3.0.1:go_yaml_yaml/vendor/gopkg.in/yaml.v3 \
		gobwas:glob:v0.2.3:gobwas_glob/vendor/github.com/gobwas/glob \
		golang:crypto:7f63de1d35b0:golang_crypto/vendor/golang.org/x/crypto \
		golang:exp:8dddf5d87bd8:golang_exp/vendor/golang.org/x/exp \
		golang:net:0a1ea396d57c:golang_net/vendor/golang.org/x/net \
		golang:sys:95e765b1cc43:golang_sys/vendor/golang.org/x/sys \
		golang:term:7a66f970e087:golang_term/vendor/golang.org/x/term \
		golang:text:v0.3.8:golang_text/vendor/golang.org/x/text \
		google:go-cmp:v0.5.6:google_go_cmp/vendor/github.com/google/go-cmp \
		gookit:color:v1.4.2:gookit_color/vendor/github.com/gookit/color \
		imdario:mergo:v0.3.11:imdario_mergo/vendor/github.com/imdario/mergo \
		integrii:flaggy:v1.4.0:integrii_flaggy/vendor/github.com/integrii/flaggy \
		jbenet:go-context:d14ea06fba99:jbenet_go_context/vendor/github.com/jbenet/go-context \
		jesseduffield:generics:727e535cbe68:jesseduffield_generics/vendor/github.com/jesseduffield/generics \
		jesseduffield:go-git:fdd53fef665d:jesseduffield_go_git_v5/vendor/github.com/jesseduffield/go-git/v5 \
		jesseduffield:gocui:16c24668f71c:jesseduffield_gocui/vendor/github.com/jesseduffield/gocui \
		jesseduffield:kill:bfbe04675d10:jesseduffield_kill/vendor/github.com/jesseduffield/kill \
		jesseduffield:lazycore:03d2e40243c5:jesseduffield_lazycore/vendor/github.com/jesseduffield/lazycore \
		jesseduffield:minimal:9cde264e6b1e:jesseduffield_minimal_gitignore/vendor/github.com/jesseduffield/minimal \
		jesseduffield:yaml:v2.1.0:jesseduffield_yaml/vendor/github.com/jesseduffield/yaml \
		kardianos:osext:2bc1f35cddc0:kardianos_osext/vendor/github.com/kardianos/osext \
		kevinburke:ssh_config:01f96b0aa0cd:kevinburke_ssh_config/vendor/github.com/kevinburke/ssh_config \
		konsorten:go-windows-terminal-sequences:v1.0.2:konsorten_go_windows_terminal_sequences/vendor/github.com/konsorten/go-windows-terminal-sequences \
		kr:logfmt:b84e30acd515:kr_logfmt/vendor/github.com/kr/logfmt \
		kylelemons:godebug:v1.1.0:kylelemons_godebug/vendor/github.com/kylelemons/godebug \
		kyokomi:emoji:v2.2.8:kyokomi_emoji_v2/vendor/github.com/kyokomi/emoji/v2 \
		lucasb-eyer:go-colorful:v1.2.0:lucasb_eyer_go_colorful/vendor/github.com/lucasb-eyer/go-colorful \
		mattn:go-colorable:v0.1.11:mattn_go_colorable/vendor/github.com/mattn/go-colorable \
		mattn:go-isatty:v0.0.14:mattn_go_isatty/vendor/github.com/mattn/go-isatty \
		mattn:go-runewidth:v0.0.14:mattn_go_runewidth/vendor/github.com/mattn/go-runewidth \
		mgutz:str:v1.2.0:mgutz_str/vendor/github.com/mgutz/str \
		mitchellh:go-homedir:v1.1.0:mitchellh_go_homedir/vendor/github.com/mitchellh/go-homedir \
		onsi:ginkgo:v1.10.3:onsi_ginkgo/vendor/github.com/onsi/ginkgo \
		onsi:gomega:v1.7.1:onsi_gomega/vendor/github.com/onsi/gomega \
		ozeidan:fuzzy-patricia:v3.0.0:ozeidan_fuzzy_patricia/vendor/gopkg.in/ozeidan/fuzzy-patricia.v3 \
		petermattis:goid:b0b1615b78e5:petermattis_goid/vendor/github.com/petermattis/goid \
		pmezard:go-difflib:v1.0.0:pmezard_go_difflib/vendor/github.com/pmezard/go-difflib \
		rivo:uniseg:v0.4.2:rivo_uniseg/vendor/github.com/rivo/uniseg \
		sahilm:fuzzy:v0.1.0:sahilm_fuzzy/vendor/github.com/sahilm/fuzzy \
		samber:lo:v1.31.0:samber_lo/vendor/github.com/samber/lo \
		sanity-io:litter:v1.5.2:sanity_io_litter/vendor/github.com/sanity-io/litter \
		sasha-s:go-deadlock:v0.3.1:sasha_s_go_deadlock/vendor/github.com/sasha-s/go-deadlock \
		sergi:go-diff:v1.1.0:sergi_go_diff/vendor/github.com/sergi/go-diff \
		sirupsen:logrus:v1.4.2:sirupsen_logrus/vendor/github.com/sirupsen/logrus \
		spkg:bom:59b7046e48ad:spkg_bom/vendor/github.com/spkg/bom \
		stretchr:testify:v1.8.0:stretchr_testify/vendor/github.com/stretchr/testify \
		xanzy:ssh-agent:v0.2.1:xanzy_ssh_agent/vendor/github.com/xanzy/ssh-agent \
		xo:terminfo:ca9a967f8778:xo_terminfo/vendor/github.com/xo/terminfo

GO_PKGNAME=	github.com/${GH_ACCOUNT}/${PORTNAME}

PLIST_FILES=	bin/${PORTNAME}

.include <bsd.port.mk>
