source_path="$HOME/mainchain"
testnet_builder_path="$source_path/testnet-builder"
testnet_builder_data="$testnet_builder_path/data"
trustnote_headless_path="$testnet_builder_path/trustnote-headless"
config_path="$HOME/.config"

cp -r "$testnet_builder_path/genesis-scripts/"* "$trustnote_headless_path/play/"
mkdir "$testnet_builder_data"

cd "$trustnote_headless_path/play/"
node create_allConfig.js
cd $HOME

mkdir "$config_path/headless15"
cp -r "$testnet_builder_data/headless15/"* "$config_path/headless15"
chown -R houfa:houfa "$config_path/headless15"
chown -R houfa:houfa "$trustnote_headless_path"