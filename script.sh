# wget -O ~/.vocab "https://goo.gl/N4EiTq" --no-check-certificate
# wget -O ~/.vocabscript "https://goo.gl/gI7xKQ" --no-check-certificate
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	OSBASHRC=bashrc
elif [[ "$OSTYPE" == "darwin"* ]]; then
	OSBASHRC=bash_profile
fi

if ! grep -Fxq '~/.svocab' ~/.$OSBASHRC; then
	echo $'\nchmod +x ~/.svocab\n~/.svocab\nalias clear="clear;~/.svocab"' >> ~/.$OSBASHRC
fi

OSBASHRC="zshrc"
if [[ -f ~/.$OSBASHRC ]]; then
	if ! grep -Fxq '~/.svocab' ~/.$OSBASHRC; then
		echo $'\nchmod +x ~/.svocab\n~/.svocab\nalias clear="clear;~/.svocab"' >> ~/.$OSBASHRC
	fi
fi
