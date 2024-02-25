---

# Phone Number Information Retrieval

This repository contains Python scripts for retrieving information about phone numbers using the `phonenumbers` library and visualizing the location on a map using `folium`.

## Scripts

### `phone_info.py`

This script retrieves information about a phone number such as its location and service provider.

1. **Usage**:
    - Replace `number` in `myNumber.py` with the desired phone number.
    - Ensure you have an API key for OpenCage Geocode and replace `'2ef0cb1afd864632843a41fa6918ebbe'` with your key.
    - Run the script.

2. **Dependencies**:
    - `phonenumbers`
    - `folium`
    - `opencage`

### `test.py`

This script is similar to `phone_info.py` and retrieves information about a phone number.

1. **Usage**:
    - Replace `number` in `test.py` with the desired phone number.
    - Run the script.

2. **Dependencies**:
    - `phonenumbers`

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/Rajatgde/phone-number-info.git
    ```

2. Navigate to the repository:

    ```bash
    cd phone-number-info
    ```

3. Run the desired script:

    ```bash
    python phone_info.py
    ```

    or

    ```bash
    python test.py
    ```

## Contributing

Contributions are welcome! If you find any issues or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
