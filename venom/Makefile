
branch:=$(shell git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/')

tag_prefix:=${branch}.$(shell date +"%y%m%d").
last_tag_of_today:=$(shell git tag | grep "^${tag_prefix}" | tail -n 1 | sed "s/^${tag_prefix}//")

ifneq ("${last_tag_of_today}","")
	tag:=${tag_prefix}$(shell printf "%02d" $(shell echo "${last_tag_of_today} + 1" | bc))
else
	tag:=${tag_prefix}01
endif

.PHONY: tag

tag:
	git tag -a ${tag} -mx 
	git push origin ${tag}
