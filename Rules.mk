# dotmpe docutils extension Makefile rules
#
include                $(MK_SHARE)Core/Main.dirstack.mk
MK                  += $/Rules.mk
#      ------------ -- 


PACK := docutils-ext.mpe

PY_TEST_$d					:= test/main.py

# Set targets to create documentation upon build
PIC_$d 				:= $(wildcard $/doc/*.pic)
PIC_PNG_$d 			:= $(PIC_$d:$/%.pic=$B%.png)
PIC_SVG_$d 			:= $(PIC_$d:$/%.pic=$B%.png)

RST_$d				:= $(wildcard $/*.rst $/doc/*.rst)
#XML_$d				:= $(RST_$d:$/%.rst=$B%.xml)
XHT_$d				:= $(RST_$d:$/%.rst=$B%.xhtml)

$(XHT_$d)  $(XML_$d)  $(PIC_PNG_$d)  $(PIC_SVG_$d) : $/Rules.mk


# Local to Global

SRC					+= \
							 $(PIC_$d) \
							 $(RST_$d)
TRGT				+= \
							 $(XHT_$d) \
							 $(XML_$d) \
							 $(PIC_PNG_$d) \
							 $(PIC_SVG_$d)
CLN 				+= \
							 $(XHT_$d) \
							 $(XML_$d) \
							 $(PIC_PNG_$d) \
							 $(PIC_SVG_$d) \
							 $(shell find ./test ./dotmpe -iname '*.pyc')
TEST				+= \
							 test_$d

.PHONY: 			 test_$d


#clean: clean-pyc
#	@-rm README.xml README.xhtml
#
#clean-pyc:
#	@-find ./ -iname "*.pyc" | while read c; do rm "$$c"; done;


test_$d: M :=
test_$d: D := $d
test_$d:
	@$(ll) attention "$@" "Testing modules listed in" test/main.list;
	@\
		TEST_PY=$(PY_TEST_$(D));\
		test -n "$M" && TEST_PY_ARGV="$M" \
			|| TEST_PY_ARGV="$(call f_getlines,test/main.list)";\
		TEST_LIB=dotmpe;\
		PYTHONPATH=$$PYTHONPATH:test; \
		$(test-python) 2> test.log;
	@\
		if [ -n "$$(tail -1 test.log|grep OK)" ]; then \
			$(ll) Success "$@" "see" test.log; \
		else \
			$(ll) Errors "$@" "$$(tail -1 test.log)"; \
			$(ll) Errors "$@" see test.log; \
		fi;\
		DATE=$$(date +%s);\
		HOST=$$(hostname -s);\
		BRANCH=$$(git status | grep On.branch | sed 's/.*On branch //');\
		REV=$$(git show | grep ^commit | sed 's/commit //');\
		TOTAL=$$(grep '^Ran..*tests.in' test.log | sed 's/Ran.\([0-9]*\).tests.*$$/\1/');\
		LOGTAIL=$$(tail -1 test.log);\
		if echo $$LOGTAIL | grep -q errors;then\
		ERRORS=$$(echo $$(echo $$LOGTAIL | sed -e 's/.*errors\=\([0-9]*\).*/\1/'));\
	    else ERRORS=0;fi;\
		if echo $$LOGTAIL | grep -q failures;then\
		FAILURES=$$(echo $$(echo $$LOGTAIL | sed -e 's/.*failures\=\([0-9]*\).*/\1/'));\
        else FAILURES=0; fi;\
		PASSED=$$(( $$TOTAL - $$ERRORS - $$FAILURES ));\
		echo $$DATE, $$HOST, $$BRANCH, $$REV, test, $$PASSED, $$ERRORS, $$FAILURES >> test-results.tab
	@\
	L=$$(ls var/|grep \.log);\
		[ "$$(echo $$L|wc -w)" -gt 0 ] && { $(ll) Errors "$@" "in testfiles" "$$(echo $$L)"; } || { echo -n; }
	@$(ll) Done "$@" "see coverage with 'make test-coverage'" ;


# XXX: old, using test-python above now
test_old:
	@$(ll) attention "$@" "Testing modules listed in" test/main.list;
	@-test_listing=test/main.list;\
		test_mods=$$(cat $$test_listing|grep -v '^#'|grep -v '^$$');\
		test_listing=$$test_listing coverage run test/main.py $$test_mods \
		             2> test.log
	@if [ -n "$$(tail -1 test.log|grep OK)" ]; then \
	    $(ll) Success "$@" "see unit result in" test.log; \
	else \
	    $(ll) Errors "$@" "$$(tail -1 test.log)"; \
	    $(ll) Errors "$@" "see unit result in" test.log; \
	fi;


test-coverage::
	@coverage report --include="test/*,dotmpe/*"

#test-atlassian
test-common::
	@\
		$(ll) attention "$@" "Running 'common' test-suite" "test/main.py"; \
		python test/main.py common

#test-rstwriter
test-form::
	@\
		$(ll) attention "$@" "Testing 'rst-form' reader" "tools/rst-form.py"; \
		python tools/rst-form.py examples/form.rst



TEST_RST_$d      := $(wildcard var/test-rst.*.rst)
TEST_RST_XML_$d  := $(TEST_RST_$d:%.rst=%.xml)

var-testfiles.log: $(TEST_RST_XML_$d)
	@\
		$(ll) attention "$@" "All XML files built, removing valid ones. "; \
		for x in var/*.xml; do echo $$x; stat $$x.*.log > /dev/null 2> /dev/null || rm $$x ; done;
	@\
	L=$$(ls var/|grep \.log);\
	    for l in $$L; do echo $$l >> $@; cat var/$$l >> $@;echo >> $@;done;\
		[ "$$(echo $$L|wc -w)" -gt 0 ] && { $(ll) Errors "$@" "in testfiles" "$$(echo $$L)"; } || { $(ll) OK "$@"; }

var/%.xml: var/%.rst
	@\
	$(ll) file_target "$@" "Generating.." "$^" ;\
	./tools/rst2xml "$<" | tidy -w 0 -i -xml -q > "$@" 2> "$@.du.log"; \
	[ -s "$@.du.log" ] && { \
		$(ll) file_error "$@" "Warnings, see" $@.du.log; \
	} || { \
		rm "$@.du.log"; \
		xmllint --valid --noout $@ 2> $@.dtd.log; \
		[ -s "$@.dtd.log" ] && { \
		  $(ll) file_error "$@" "DTD validation warnings, see" "$@.dtd.log"; \
		} || { \
		  rm "$@.dtd.log"; \
		  $(ll) file_ok "$@"; \
		} \
	}

define build-pretty
	$(ll) file_target "$@" "Generating.." "$^" ;\
	./tools/rst2pprint "$<" "$@" 2> "$@.log" ;\
	[ -s "$@.log" ] && { \
		$(ll) file_error "$@" "Warnings, see" test.log; \
	} || { \
		rm "$@.log"; \
		$(ll) file_ok "$@"; \
	}
endef

var/%.pxml: var/%.rst
	@\
	$(build-pretty)

var/%.pxml: var/%.txt
	@\
	$(build-pretty)

#$B%.xml: $/%.rst    
#	@-./dotmpe-doctree.py --traceback $< $@ 
#	@-tidy -q -xml -utf8 -w 0 -i -m $@
#
#$B%.xhtml: $/%.rst    
#	@-./dotmpe-doc.py -d -t -g --link-stylesheet --stylesheet=/style/default $< $@  
#	@-tidy -q -xml -utf8 -w 0 -i -m $@
#

#      ------------ -- 
include                $(MK_SHARE)Core/Main.dirstack-pop.mk
# vim:noet:
