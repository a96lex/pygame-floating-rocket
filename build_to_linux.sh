# linux
pyinstaller main.py --onefile --noconsole
mv dist/main linux_build
rm -r build
rm *.spec
rm -r dist
chmod +x linux_build