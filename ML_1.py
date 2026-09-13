{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNkYuOJnHdsEW/x6VZwra8a",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dipaliishi/ML-Practicals/blob/Python/ML_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ptD8EAHlZB1L"
      },
      "outputs": [],
      "source": [
        "#import required libraries\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2]Data Collection"
      ],
      "metadata": {
        "id": "4QIHsM6rZmHx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Create dataset\n",
        "data={\n",
        "    \"study_Hours\":[1,2,3,4,5,6,7,8,9,10],\n",
        "    \"Attendance\":[60,85,70,95,65,80,90,75,88,72],\n",
        "    \"Marks\":[32,42,47,58,61,67,76,79,88,91]\n",
        "}\n",
        "#Convert dict into DataFrame\n",
        "df=pd.DataFrame(data)\n",
        "print(df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GZZhLFfRZqjh",
        "outputId": "6d1d8aea-2bd4-4cba-c38d-5b9597a2ef1b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   study_Hours  Attendance  Marks\n",
            "0            1          60     32\n",
            "1            2          85     42\n",
            "2            3          70     47\n",
            "3            4          95     58\n",
            "4            5          65     61\n",
            "5            6          80     67\n",
            "6            7          90     76\n",
            "7            8          75     79\n",
            "8            9          88     88\n",
            "9           10          72     91\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "EDA And Preprocessing"
      ],
      "metadata": {
        "id": "I57CfRHpbL3p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('First five rows:')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 223
        },
        "id": "eLXvz0GuZqgP",
        "outputId": "343850e3-eef6-4969-d9f6-a8aa57db14b8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First five rows:\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   study_Hours  Attendance  Marks\n",
              "0            1          60     32\n",
              "1            2          85     42\n",
              "2            3          70     47\n",
              "3            4          95     58\n",
              "4            5          65     61"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a05b0cb6-a9ae-452c-8951-693093ff137b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>study_Hours</th>\n",
              "      <th>Attendance</th>\n",
              "      <th>Marks</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>60</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>85</td>\n",
              "      <td>42</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>70</td>\n",
              "      <td>47</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>95</td>\n",
              "      <td>58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>65</td>\n",
              "      <td>61</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a05b0cb6-a9ae-452c-8951-693093ff137b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a05b0cb6-a9ae-452c-8951-693093ff137b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a05b0cb6-a9ae-452c-8951-693093ff137b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"study_Hours\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 1,\n        \"max\": 10,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          9,\n          2,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Attendance\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 60,\n        \"max\": 95,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          88,\n          85,\n          80\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Marks\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 19,\n        \"min\": 32,\n        \"max\": 91,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          88,\n          42,\n          67\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Shape of Dataset')\n",
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0MMmVD3kZkUM",
        "outputId": "4d41a3c5-07e7-4d1f-c37a-30146fa9cc3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Shape of Dataset\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10, 3)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Information:')\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-8W9hB47cXdY",
        "outputId": "16090edc-5b3f-4222-b5e1-bacae592f26e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Information:\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 10 entries, 0 to 9\n",
            "Data columns (total 3 columns):\n",
            " #   Column       Non-Null Count  Dtype\n",
            "---  ------       --------------  -----\n",
            " 0   study_Hours  10 non-null     int64\n",
            " 1   Attendance   10 non-null     int64\n",
            " 2   Marks        10 non-null     int64\n",
            "dtypes: int64(3)\n",
            "memory usage: 372.0 bytes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Statistical Analysis:\\n',df.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1U4favE6cfC-",
        "outputId": "d81881fb-40b9-4130-8718-323a9b63bf34"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Statistical Analysis:\n",
            "        study_Hours  Attendance      Marks\n",
            "count     10.00000   10.000000  10.000000\n",
            "mean       5.50000   78.000000  64.100000\n",
            "std        3.02765   11.489125  19.790289\n",
            "min        1.00000   60.000000  32.000000\n",
            "25%        3.25000   70.500000  49.750000\n",
            "50%        5.50000   77.500000  64.000000\n",
            "75%        7.75000   87.250000  78.250000\n",
            "max       10.00000   95.000000  91.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Check for null values:')\n",
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 196
        },
        "id": "xIlYRPPJcpm_",
        "outputId": "ee25c074-4928-40ec-fa72-25eeff793dee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Check for null values:\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "study_Hours    0\n",
              "Attendence     0\n",
              "Marks          0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>study_Hours</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Attendence</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Marks</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Duplicate Values\n",
        "df.duplicated().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uC-aZuFndDwO",
        "outputId": "7d2a8101-9f6f-4e89-be1d-4e6f4801e508"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.int64(0)"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.drop_duplicates()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "tEF8j27odm6W",
        "outputId": "bedba021-5d21-41ec-bf77-3d47553785fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   study_Hours  Attendance  Marks\n",
              "0            1          60     32\n",
              "1            2          85     42\n",
              "2            3          70     47\n",
              "3            4          95     58\n",
              "4            5          65     61\n",
              "5            6          80     67\n",
              "6            7          90     76\n",
              "7            8          75     79\n",
              "8            9          88     88\n",
              "9           10          72     91"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-86a39857-5a7f-49aa-a68a-d9c50daed2d5\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>study_Hours</th>\n",
              "      <th>Attendance</th>\n",
              "      <th>Marks</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>60</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>85</td>\n",
              "      <td>42</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>70</td>\n",
              "      <td>47</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>95</td>\n",
              "      <td>58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>65</td>\n",
              "      <td>61</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>6</td>\n",
              "      <td>80</td>\n",
              "      <td>67</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>7</td>\n",
              "      <td>90</td>\n",
              "      <td>76</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8</td>\n",
              "      <td>75</td>\n",
              "      <td>79</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "      <td>88</td>\n",
              "      <td>88</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>10</td>\n",
              "      <td>72</td>\n",
              "      <td>91</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-86a39857-5a7f-49aa-a68a-d9c50daed2d5')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-86a39857-5a7f-49aa-a68a-d9c50daed2d5 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-86a39857-5a7f-49aa-a68a-d9c50daed2d5');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"study_Hours\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 1,\n        \"max\": 10,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          9,\n          2,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Attendance\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 60,\n        \"max\": 95,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          88,\n          85,\n          80\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Marks\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 19,\n        \"min\": 32,\n        \"max\": 91,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          88,\n          42,\n          67\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data Visualization"
      ],
      "metadata": {
        "id": "Q9Z9xAmBdsmn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Correlation Heatmap\n",
        "import seaborn as sns\n",
        "\n",
        "df_corr = df.corr()\n",
        "\n",
        "plt.figure(figsize=(6,4))\n",
        "sns.heatmap(df_corr, annot=True, cmap='Blues')\n",
        "\n",
        "plt.title('Correlation Heatmap')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "id": "lnXy2KsJdqpm",
        "outputId": "5e7590c7-b55f-4edd-fb3e-a0d6cca19b03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Correlation Heatmap')"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**A] Simple Linear Regression by Using Sckit - learn**"
      ],
      "metadata": {
        "id": "rlWSYgn9ekeX"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "7wZQG9Bge8Mt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#features Selection\n",
        "x=df[['study_Hours']]  #independent variables\n",
        "y=df['Marks']"
      ],
      "metadata": {
        "id": "eOXPw25geesO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4] Model Building"
      ],
      "metadata": {
        "id": "MVPW4pJUfvX8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Split dataset into Traning and testing set\n",
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)"
      ],
      "metadata": {
        "id": "GtOdgfTEft_9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x_test"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "QHSvG34ZfgGU",
        "outputId": "0bbe17f2-a08a-45a0-d85a-7eff0755fc5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   study_Hours\n",
              "8            9\n",
              "1            2"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0338ca98-8b58-4347-bcb6-b29951918408\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>study_Hours</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0338ca98-8b58-4347-bcb6-b29951918408')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-0338ca98-8b58-4347-bcb6-b29951918408 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-0338ca98-8b58-4347-bcb6-b29951918408');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_b572c2f3-13dd-4ebe-9aa6-1c35a706b902\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('x_test')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_b572c2f3-13dd-4ebe-9aa6-1c35a706b902 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('x_test');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "x_test",
              "summary": "{\n  \"name\": \"x_test\",\n  \"rows\": 2,\n  \"fields\": [\n    {\n      \"column\": \"study_Hours\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 4,\n        \"min\": 2,\n        \"max\": 9,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          2,\n          9\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Import Model\n",
        "from sklearn.linear_model import LinearRegression\n",
        "model=LinearRegression()\n",
        "\n",
        "#Train the Model\n",
        "model.fit(x_train, y_train)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "jadzxVYUgIOM",
        "outputId": "9bbe3900-8638-405e-8295-6d0fba9e62b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {\n",
              "  /* Definition of color scheme common for light and dark mode */\n",
              "  --sklearn-color-text: #000;\n",
              "  --sklearn-color-text-muted: #666;\n",
              "  --sklearn-color-line: gray;\n",
              "  /* Definition of color scheme for unfitted estimators */\n",
              "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
              "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
              "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
              "  --sklearn-color-unfitted-level-3: chocolate;\n",
              "  /* Definition of color scheme for fitted estimators */\n",
              "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
              "  --sklearn-color-fitted-level-1: #d4ebff;\n",
              "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
              "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
              "\n",
              "  /* Specific color for light theme */\n",
              "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
              "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-icon: #696969;\n",
              "\n",
              "  @media (prefers-color-scheme: dark) {\n",
              "    /* Redefinition of color scheme for dark theme */\n",
              "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
              "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-icon: #878787;\n",
              "  }\n",
              "}\n",
              "\n",
              "#sk-container-id-1 {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 pre {\n",
              "  padding: 0;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-hidden--visually {\n",
              "  border: 0;\n",
              "  clip: rect(1px 1px 1px 1px);\n",
              "  clip: rect(1px, 1px, 1px, 1px);\n",
              "  height: 1px;\n",
              "  margin: -1px;\n",
              "  overflow: hidden;\n",
              "  padding: 0;\n",
              "  position: absolute;\n",
              "  width: 1px;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-dashed-wrapped {\n",
              "  border: 1px dashed var(--sklearn-color-line);\n",
              "  margin: 0 0.4em 0.5em 0.4em;\n",
              "  box-sizing: border-box;\n",
              "  padding-bottom: 0.4em;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-container {\n",
              "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
              "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
              "     so we also need the `!important` here to be able to override the\n",
              "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
              "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
              "  display: inline-block !important;\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-text-repr-fallback {\n",
              "  display: none;\n",
              "}\n",
              "\n",
              "div.sk-parallel-item,\n",
              "div.sk-serial,\n",
              "div.sk-item {\n",
              "  /* draw centered vertical line to link estimators */\n",
              "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
              "  background-size: 2px 100%;\n",
              "  background-repeat: no-repeat;\n",
              "  background-position: center center;\n",
              "}\n",
              "\n",
              "/* Parallel-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item::after {\n",
              "  content: \"\";\n",
              "  width: 100%;\n",
              "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
              "  flex-grow: 1;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel {\n",
              "  display: flex;\n",
              "  align-items: stretch;\n",
              "  justify-content: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
              "  align-self: flex-end;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
              "  align-self: flex-start;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
              "  width: 0;\n",
              "}\n",
              "\n",
              "/* Serial-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-serial {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "  align-items: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  padding-right: 1em;\n",
              "  padding-left: 1em;\n",
              "}\n",
              "\n",
              "\n",
              "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
              "clickable and can be expanded/collapsed.\n",
              "- Pipeline and ColumnTransformer use this feature and define the default style\n",
              "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
              "*/\n",
              "\n",
              "/* Pipeline and ColumnTransformer style (default) */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable {\n",
              "  /* Default theme specific background. It is overwritten whether we have a\n",
              "  specific estimator or a Pipeline/ColumnTransformer */\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "/* Toggleable label */\n",
              "#sk-container-id-1 label.sk-toggleable__label {\n",
              "  cursor: pointer;\n",
              "  display: flex;\n",
              "  width: 100%;\n",
              "  margin-bottom: 0;\n",
              "  padding: 0.5em;\n",
              "  box-sizing: border-box;\n",
              "  text-align: center;\n",
              "  align-items: start;\n",
              "  justify-content: space-between;\n",
              "  gap: 0.5em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label .caption {\n",
              "  font-size: 0.6rem;\n",
              "  font-weight: lighter;\n",
              "  color: var(--sklearn-color-text-muted);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
              "  /* Arrow on the left of the label */\n",
              "  content: \"▸\";\n",
              "  float: left;\n",
              "  margin-right: 0.25em;\n",
              "  color: var(--sklearn-color-icon);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "/* Toggleable content - dropdown */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content {\n",
              "  max-height: 0;\n",
              "  max-width: 0;\n",
              "  overflow: hidden;\n",
              "  text-align: left;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content pre {\n",
              "  margin: 0.2em;\n",
              "  border-radius: 0.25em;\n",
              "  color: var(--sklearn-color-text);\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
              "  /* Expand drop-down */\n",
              "  max-height: 200px;\n",
              "  max-width: 100%;\n",
              "  overflow: auto;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
              "  content: \"▾\";\n",
              "}\n",
              "\n",
              "/* Pipeline/ColumnTransformer-specific style */\n",
              "\n",
              "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator-specific style */\n",
              "\n",
              "/* Colorize estimator box */\n",
              "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  /* The background is the default theme color */\n",
              "  color: var(--sklearn-color-text-on-default-background);\n",
              "}\n",
              "\n",
              "/* On hover, darken the color of the background */\n",
              "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "/* Label box, darken color on hover, fitted */\n",
              "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator label */\n",
              "\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  font-family: monospace;\n",
              "  font-weight: bold;\n",
              "  display: inline-block;\n",
              "  line-height: 1.2em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label-container {\n",
              "  text-align: center;\n",
              "}\n",
              "\n",
              "/* Estimator-specific */\n",
              "#sk-container-id-1 div.sk-estimator {\n",
              "  font-family: monospace;\n",
              "  border: 1px dotted var(--sklearn-color-border-box);\n",
              "  border-radius: 0.25em;\n",
              "  box-sizing: border-box;\n",
              "  margin-bottom: 0.5em;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "/* on hover */\n",
              "#sk-container-id-1 div.sk-estimator:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
              "\n",
              "/* Common style for \"i\" and \"?\" */\n",
              "\n",
              ".sk-estimator-doc-link,\n",
              "a:link.sk-estimator-doc-link,\n",
              "a:visited.sk-estimator-doc-link {\n",
              "  float: right;\n",
              "  font-size: smaller;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1em;\n",
              "  height: 1em;\n",
              "  width: 1em;\n",
              "  text-decoration: none !important;\n",
              "  margin-left: 0.5em;\n",
              "  text-align: center;\n",
              "  /* unfitted */\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted,\n",
              "a:link.sk-estimator-doc-link.fitted,\n",
              "a:visited.sk-estimator-doc-link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "/* Span, style for the box shown on hovering the info icon */\n",
              ".sk-estimator-doc-link span {\n",
              "  display: none;\n",
              "  z-index: 9999;\n",
              "  position: relative;\n",
              "  font-weight: normal;\n",
              "  right: .2ex;\n",
              "  padding: .5ex;\n",
              "  margin: .5ex;\n",
              "  width: min-content;\n",
              "  min-width: 20ex;\n",
              "  max-width: 50ex;\n",
              "  color: var(--sklearn-color-text);\n",
              "  box-shadow: 2pt 2pt 4pt #999;\n",
              "  /* unfitted */\n",
              "  background: var(--sklearn-color-unfitted-level-0);\n",
              "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted span {\n",
              "  /* fitted */\n",
              "  background: var(--sklearn-color-fitted-level-0);\n",
              "  border: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link:hover span {\n",
              "  display: block;\n",
              "}\n",
              "\n",
              "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link {\n",
              "  float: right;\n",
              "  font-size: 1rem;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1rem;\n",
              "  height: 1rem;\n",
              "  width: 1rem;\n",
              "  text-decoration: none;\n",
              "  /* unfitted */\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "#sk-container-id-1 a.estimator_doc_link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>LinearRegression</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LinearRegression.html\">?<span>Documentation for LinearRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>LinearRegression()</pre></div> </div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Predict the values\n",
        "y_pred=model.predict(x_test)\n",
        "y_pred"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kw3xyTdZgNir",
        "outputId": "9699f6d4-f4fa-4149-8ffb-f5bb7fcc6a94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([86.53448276, 41.21551724])"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#print Equation\n",
        "print('Intercept:', model.intercept_)\n",
        "print('Slope:', model.coef_[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OQPFrOoZhOOb",
        "outputId": "3e6f0539-34ba-4832-8a2c-3fb5b00e91f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intercept: 28.26724137931034\n",
            "Slope: 6.474137931034483\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**SLR Equation**\n",
        "\n",
        " *   Marks=(6.48*Study_Hours)+28.27\n",
        "\n"
      ],
      "metadata": {
        "id": "vSNHspRFiC-i"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**5] Model Evaluation**"
      ],
      "metadata": {
        "id": "oxEYoEKvHMBK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Evaluation\n",
        "from sklearn.metrics import root_mean_squared_error, r2_score,mean_squared_error\n",
        "rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n",
        "r2 = r2_score(y_test, y_pred)\n",
        "print('RMSE:', round(rmse,3))\n",
        "print('R2 Score:',round(r2,2))"
      ],
      "metadata": {
        "id": "iUQl-2ObhqNM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6d68eb4-99e2-416b-e367-f1d67c3a2b36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RMSE: 1.175\n",
            "R2 Score: 1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Regression Line\n",
        "plt.figure(figsize=(7,5))\n",
        "plt.scatter(x, y, color='blue', label='Actual Data')\n",
        "plt.plot(x_test, y_pred, color='red', label='Regression Line')\n",
        "plt.xlabel('Study Hours')\n",
        "plt.ylabel('Marks')\n",
        "plt.title('Simple Linear Regression')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "ibnUbd7Si6T5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "outputId": "29bd4236-beca-4a39-af08-47d8d18131c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 700x500 with 1 Axes>"
            ],
            "image/png": "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HQuf71dSUhI2m41Vq1al+D5eXl7p8j4pudvnvV1SUhJFihRh/vz5KT5/K8RdvHiRRo0a4ePjw9tvv02JEiVwd3dn7969vPLKK8laK9wenlKrYcOG9qsjW7VqRaVKlejYsSN79uzBycnJ/h7jxo2jatWqKR7Dy8uL69evp/m976z31nt16tTprqGvcuXKgBmKjhw5wooVK1i9ejVLlixhypQpDBs2jLfeeguA9u3b06BBA5YuXcratWsZN24cY8aMISoq6q6zc2l1t593ev0ui1hJIUwkC6pZsyYAZ86cyfD3ujUTc7tffvnlnl3OS5QogWEYhIWFUbp06Qys7v6UKFGC9evXU69evXsGp02bNnHhwgWioqJo2LChffuxY8cypC4vLy+GDx9Ot27dWLRoER06dLCfavPx8aFJkyZ3fW2RIkVwd3fn119/TfZcSttSUrhwYby9vUlMTLzne93i6enJv//9b/7973+TkJBAREQEo0aNYsiQIfZWFwEBAbzwwgu88MILnDt3jurVqzNq1Ki7hrCQkBDWr1/PpUuXHGbDbp36DQkJSdVnEckJtCZMxEIbN25M8V/0t9ZjlSlTJsNrWLZsGadOnbKPv//+e3bu3HnPmYyIiAicnZ156623ktVvGAYXLlzIsHpTo3379iQmJjJixIhkz928edPesf7WLMvtnyEhIYEpU6ZkWG0dO3YkKCiIMWPGAFCjRg1KlCjBe++9x+XLl5Ptf/78eXutTZo0YdmyZQ5rsH799ddk66juxtnZmbZt27JkyZIU25Dcei8g2c/Q1dWV8uXLYxgGN27cIDExMdnp2iJFihAYGEh8fPxda2jZsiWJiYlMnjzZYfv48eOx2WzpNoMmkh1oJkzEQn379uXq1as8+eSTlC1bloSEBLZv385///tfQkND07wI/H6ULFmS+vXr07t3b+Lj45kwYQIFCxZk8ODBd31NiRIlGDlyJEOGDOH48eO0adMGb29vjh07xtKlS3n++ed56aWX/vG9P/300xR7PvXv3/+BPlOjRo3o2bMno0ePZv/+/Tz22GPkyZOHo0eP8sUXX/Dhhx/Srl076tatS/78+enSpQv9+vXDZrMxd+7cDD3VlSdPHvr378/LL7/M6tWrad68OZ988gktWrSgQoUKdOvWjaJFi3Lq1Ck2btyIj48PX331FWDeCmnt2rXUq1eP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iIhYQCFMRERExAIKYSIiIiIWUAgTERERsYBCmIiIiIgFFMJERERELKAQJiIiImIBhTARERERCyiEiYiIiFhAIUxERETEAgphIiIiIhZQCBMRERGxgEKYiIiIiAUUwkREREQsoBAmIiIiYgGFMBERERELKISJiIiIWEAhTERERMQCCmEiIiIiFlAIExEREbGAQpiIiIiIBRTCRERERCygECYiIiJiAYUwEREREQsohImIiIhYQCFMRERExAIKYSIiIiIWUAgTERERsYBCmIiIiIgFFMJERERELKAQJiIiImIBhTARERERCyiEiYiIiFjAxeoCsrvERNiyBc6cgYAAaNAAnJ2trkpERESyOoWwBxAVBf37w8mT/9sWFAQffggREdbVJSIiIlmfTkfep6goaNfOMYABnDplbo+KsqYuERERyR4Uwu5DYqI5A2YYyZ+7tS0y0txPREREJCUKYfdhy5bkM2C3MwyIjjb3ExEREUmJQth9OHMmffcTERGR3Ech7D4EBKTvfiIiIpL7KITdhwYNzKsgbbaUn7fZIDjY3E9EREQkJQph98HZ2WxDAcmD2K3xhAnqFyYiIiJ3pxB2nyIiYPFiKFrUcXtQkLldfcJERETkXtSs9QFEREDr1uqYLyIiImmnEPaAnJ2hcWOrqxAREZHsRqcjRURERCxgaQibOnUqlStXxsfHBx8fH8LDw1m1apX9+evXr9OnTx8KFiyIl5cXbdu2JSYmxsKKRURERNKHpSEsKCiId999lz179rB7924eeeQRWrduzaFDhwAYMGAAX331FV988QWbN2/m9OnTRGjFu4iIiOQANsNI6Q6I1ilQoADjxo2jXbt2FC5cmAULFtCuXTsAfv75Z8qVK8eOHTt46KGHUnW8uLg4fH19iY2NxcfHJyNLFxERkVwuLbkjy6wJS0xMZOHChVy5coXw8HD27NnDjRs3aNKkiX2fsmXLUqxYMXbs2HHX48THxxMXF+fwEBEREclqLA9hBw8exMvLCzc3N3r16sXSpUspX748Z8+exdXVlXz58jns7+fnx9mzZ+96vNGjR+Pr62t/BAcHZ/AnEBEREUk7y0NYmTJl2L9/Pzt37qR379506dKFn3766b6PN2TIEGJjY+2P6OjodKxWREREJH1Y3ifM1dWVkiVLAlCjRg127drFhx9+yL///W8SEhK4ePGiw2xYTEwM/v7+dz2em5sbbm5uGV22iIiIyAOxfCbsTklJScTHx1OjRg3y5MnDhg0b7M8dOXKEEydOEB4ebmGFIiIiIg/O0pmwIUOG0KJFC4oVK8alS5dYsGABmzZtYs2aNfj6+tKjRw8GDhxIgQIF8PHxoW/fvoSHh6f6ykgRERGRrMrSEHbu3Dk6d+7MmTNn8PX1pXLlyqxZs4amTZsCMH78eJycnGjbti3x8fE0a9aMKVOmpOk9bnXg0FWSIiIiktFu5Y3UdADLcn3C0tvJkyd1haSIiIhkqujoaIKCgu65T44PYUlJSZw+fRpvb29sNpvV5WQrcXFxBAcHEx0drUa32Yh+btmTfm7Zj35m2VNG/9wMw+DSpUsEBgbi5HTvpfeWXx2Z0ZycnP4xicq93bq3p2Qv+rllT/q5ZT/6mWVPGflz8/X1TdV+We7qSBEREZHcQCFMRERExAIKYXJXbm5uDB8+XM1vsxn93LIn/dyyH/3Msqes9HPL8QvzRURERLIizYSJiIiIWEAhTERERMQCCmEiIiIiFlAIExEREbGAQpgkM3r0aGrVqoW3tzdFihShTZs2HDlyxOqyJA3effddbDYbkZGRVpci/+DUqVN06tSJggUL4uHhQaVKldi9e7fVZck9JCYmMnToUMLCwvDw8KBEiRKMGDEiVfcKlMzx7bff0qpVKwIDA7HZbCxbtszhecMwGDZsGAEBAXh4eNCkSROOHj2a6XUqhEkymzdvpk+fPnz33XesW7eOGzdu8Nhjj3HlyhWrS5NU2LVrFx9//DGVK1e2uhT5B3///Tf16tUjT548rFq1ip9++on333+f/PnzW12a3MOYMWOYOnUqkydP5vDhw4wZM4axY8cyadIkq0uT/3flyhWqVKnCRx99lOLzY8eOZeLEiUybNo2dO3fi6elJs2bNuH79eqbWqRYV8o/Onz9PkSJF2Lx5Mw0bNrS6HLmHy5cvU716daZMmcLIkSOpWrUqEyZMsLosuYtXX32Vbdu2sWXLFqtLkTR44okn8PPzY+bMmfZtbdu2xcPDg3nz5llYmaTEZrOxdOlS2rRpA5izYIGBgQwaNIiXXnoJgNjYWPz8/Jg9ezYdOnTItNo0Eyb/KDY2FoACBQpYXIn8kz59+vD444/TpEkTq0uRVFi+fDk1a9bkqaeeokiRIlSrVo0ZM2ZYXZb8g7p167JhwwZ++eUXAA4cOMDWrVtp0aKFxZVJahw7doyzZ886/H/S19eXOnXqsGPHjkytJcffwFseTFJSEpGRkdSrV4+KFStaXY7cw8KFC9m7dy+7du2yuhRJpd9//52pU6cycOBAXnvtNXbt2kW/fv1wdXWlS5cuVpcnd/Hqq68SFxdH2bJlcXZ2JjExkVGjRtGxY0erS5NUOHv2LAB+fn4O2/38/OzPZRaFMLmnPn368OOPP7J161arS5F7iI6Opn///qxbtw53d3ery5FUSkpKombNmrzzzjsAVKtWjR9//JFp06YphGVhixYtYv78+SxYsIAKFSqwf/9+IiMjCQwM1M9N0kSnI+WuXnzxRVasWMHGjRsJCgqyuhy5hz179nDu3DmqV6+Oi4sLLi4ubN68mYkTJ+Li4kJiYqLVJUoKAgICKF++vMO2cuXKceLECYsqktR4+eWXefXVV+nQoQOVKlXimWeeYcCAAYwePdrq0iQV/P39AYiJiXHYHhMTY38usyiESTKGYfDiiy+ydOlSvvnmG8LCwqwuSf7Bo48+ysGDB9m/f7/9UbNmTTp27Mj+/ftxdna2ukRJQb169ZK1f/nll18ICQmxqCJJjatXr+Lk5PjXp7OzM0lJSRZVJGkRFhaGv78/GzZssG+Li4tj586dhIeHZ2otOh0pyfTp04cFCxbw5Zdf4u3tbT9H7uvri4eHh8XVSUq8vb2Trdnz9PSkYMGCWsuXhQ0YMIC6devyzjvv0L59e77//numT5/O9OnTrS5N7qFVq1aMGjWKYsWKUaFCBfbt28cHH3xA9+7drS5N/t/ly5f59ddf7eNjx46xf/9+ChQoQLFixYiMjGTkyJGUKlWKsLAwhg4dSmBgoP0KykxjiNwBSPExa9Ysq0uTNGjUqJHRv39/q8uQf/DVV18ZFStWNNzc3IyyZcsa06dPt7ok+QdxcXFG//79jWLFihnu7u5G8eLFjddff92Ij4+3ujT5fxs3bkzx77EuXboYhmEYSUlJxtChQw0/Pz/Dzc3NePTRR40jR45kep3qEyYiIiJiAa0JExEREbGAQpiIiIiIBRTCRERERCygECYiIiJiAYUwEREREQsohImIiIhYQCFMRERExAIKYSIiIiIWUAgTkVyhcePGREZGWl2GiIidQpiIWOL8+fP07t2bYsWK4ebmhr+/P82aNWPbtm32fWw2G8uWLbOuyNscP34cm83G/v37kz2ngCci90M38BYRS7Rt25aEhATmzJlD8eLFiYmJYcOGDVy4cMHq0rKkhIQEXF1drS5DRNKRZsJEJNNdvHiRLVu2MGbMGB5++GFCQkKoXbs2Q4YM4V//+hcAoaGhADz55JPYbDb7uGvXrrRp08bheJGRkTRu3Ng+vnLlCp07d8bLy4uAgADef/99h/3ffvttKlasmKyuqlWrMnTo0Af+fH///TedO3cmf/785M2blxYtWnD06FH782+++SZVq1Z1eM2ECRPsnxH+9zlHjRpFYGAgZcqUAWDKlCmUKlUKd3d3/Pz8aNeu3QPXKyLWUAgTkUzn5eWFl5cXy5YtIz4+PsV9du3aBcCsWbM4c+aMfZwaL7/8Mps3b+bLL79k7dq1bNq0ib1799qf7969O4cPH3Y45r59+/jhhx/o1q3bfX6q/+natSu7d+9m+fLl7NixA8MwaNmyJTdu3EjTcTZs2MCRI0dYt24dK1asYPfu3fTr14+3336bI0eOsHr1aho2bPjA9YqINXQ6UkQynYuLC7Nnz+a5555j2rRpVK9enUaNGtGhQwcqV64MQOHChQHIly8f/v7+qT725cuXmTlzJvPmzePRRx8FYM6cOQQFBdn3CQoKolmzZsyaNYtatWoBZthr1KgRxYsXv+fx69ati5OT479fr127Zp/ZOnr0KMuXL2fbtm3UrVsXgPnz5xMcHMyyZct46qmnUv1ZPD09+eSTT+ynIaOiovD09OSJJ57A29ubkJAQqlWrlurjiUjWopkwEbFE27ZtOX36NMuXL6d58+Zs2rSJ6tWrM3v27Ac67m+//UZCQgJ16tSxbytQoID9dN4tzz33HJ9//jnXr18nISGBBQsW0L179388/n//+1/279/v8KhZs6b9+cOHD+Pi4uLw/gULFqRMmTIcPnw4TZ+lUqVKDuvAmjZtSkhICMWLF+eZZ55h/vz5XL16NU3HFJGsQyFMRCzj7u5O06ZNGTp0KNu3b6dr164MHz78nq9xcnLCMAyHbWk9zQfQqlUr3NzcWLp0KV999RU3btxI1fqq4OBgSpYs6fDw8PBI03un9jN4eno6jL29vdm7dy+ff/45AQEBDBs2jCpVqnDx4sU0vb+IZA0KYSKSZZQvX54rV67Yx3ny5CExMdFhn8KFC3PmzBmHbbe3jShRogR58uRh586d9m1///03v/zyi8NrXFxc6NKlC7NmzWLWrFl06NAhzWEqJeXKlePmzZsO73/hwgWOHDlC+fLl7Z/h7NmzDkEspdYXKXFxcaFJkyaMHTuWH374gePHj/PNN988cN0ikvm0JkxEMt2FCxd46qmn6N69O5UrV8bb25vdu3czduxYWrdubd8vNDSUDRs2UK9ePdzc3MifPz+PPPII48aN47PPPiM8PJx58+bx448/2tdGeXl50aNHD15++WUKFixIkSJFeP3115Ot4wJ49tlnKVeuHIBDf7IHUapUKVq3bs1zzz3Hxx9/jLe3N6+++ipFixa1f7bGjRtz/vx5xo4dS7t27Vi9ejWrVq3Cx8fnnsdesWIFv//+Ow0bNiR//vysXLmSpKSkZKdaRSR70EyYiGQ6Ly8v6tSpw/jx42nYsCEVK1Zk6NChPPfcc0yePNm+3/vvv8+6desIDg62h6xmzZoxdOhQBg8eTK1atbh06RKdO3d2OP64ceNo0KABrVq1okmTJtSvX58aNWokq6NUqVLUrVuXsmXLOqzhelCzZs2iRo0aPPHEE4SHh2MYBitXriRPnjyAOVs2ZcoUPvroI6pUqcL333/PSy+99I/HzZcvH1FRUTzyyCOUK1eOadOm8fnnn1OhQoV0q11EMo/NuHNhgohILmEYBqVKleKFF15g4MCBVpcjIrmMTkeKSK50/vx5Fi5cyNmzZ9OlN5iISFophIlIrlSkSBEKFSrE9OnTyZ8/v9XliEgupBAmIrmSVmKIiNW0MF9ERETEAgphIiIiIhZQCBMRERGxgEKYiIiIiAUUwkREREQsoBAmIiIiYgGFMBERERELKISJiIiIWOD/AFd4sl3hycnzAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " **Residual Plot**"
      ],
      "metadata": {
        "id": "ucqils62IEq3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "residuals = y_test - y_pred\n",
        "plt.figure(figsize=(7,5))\n",
        "plt.scatter(y_pred, residuals, color='green')\n",
        "plt.axhline(y=0, color='red', linestyle='--')\n",
        "plt.xlabel('Predicted Values')\n",
        "plt.ylabel('Residuals')\n",
        "plt.title('Residual Plot')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "id": "fqVOTs-PID_b",
        "outputId": "3d100f0d-cf07-4f53-cc2c-b2e3def7ac99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 700x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmUAAAHWCAYAAAA2Of5hAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAPItJREFUeJzt3X1cVHX+///nADKgCKgIKKFoampeJitfNFM3zMyPZa7pagla1lq2knSh7q5XXUjaWnahUpZamaWZuaau5VKapuVV1Naa1wUpoFYyXqIy798f/hydAAMcmEM87rfbud2Y93mdc17DYcan55w5YzPGGAEAAMCrfLzdAAAAAAhlAAAAlkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAH53Jk2aJJvNVqJam82mSZMmlWs/3bp1U7du3Sy7PgDWQCgDUG7mz58vm83mmvz8/BQVFaWhQ4fqwIED3m7PcmJiYtx+X+Hh4erSpYvef/99j6z/5MmTmjRpktauXeuR9QHwLEIZgHL3+OOP680331RaWpp69eqlBQsWqGvXrjp9+nS5bO8f//iHTp06VS7rLm/t2rXTm2++qTfffFOPPPKIDh48qH79+iktLe2K133y5ElNnjyZUAZYlJ+3GwDw+9erVy/FxsZKkoYPH66wsDBNnTpVy5cv14ABAzy+PT8/P/n5Vc63t6ioKN11112ux4mJiWrSpImee+45jRgxwoudAShvHCkDUOG6dOkiSdq7d6/b+Hfffaf+/furdu3aCggIUGxsrJYvX+5Wc/bsWU2ePFlNmzZVQECA6tSpo+uvv15r1qxx1RR1TVl+fr5Gjx6tunXrqmbNmrr11lv1448/Fupt6NChiomJKTRe1DrnzZunP/7xjwoPD5fdblfLli01e/bsUv0ufktkZKRatGih/fv3X7bu0KFDuueeexQREaGAgAC1bdtWr7/+umv+999/r7p160qSJk+e7DpFWt7X0wEoucr5X0kAldr3338vSapVq5Zr7Ntvv1Xnzp0VFRWlsWPHqkaNGlq8eLH69u2r9957T7fffruk8+EoNTVVw4cPV8eOHeVwOLR161Zt375dPXr0KHabw4cP14IFCzR48GB16tRJH3/8sXr37n1Fz2P27Nm69tprdeutt8rPz08ffPCBHnjgATmdTo0cOfKK1n3B2bNnlZWVpTp16hRbc+rUKXXr1k179uzRgw8+qEaNGundd9/V0KFDdfToUSUnJ6tu3bqaPXu27r//ft1+++3q16+fJKlNmzYe6ROABxgAKCfz5s0zksx//vMfc/jwYZOVlWWWLFli6tata+x2u8nKynLV3njjjaZ169bm9OnTrjGn02k6depkmjZt6hpr27at6d2792W3O3HiRHPp21tGRoaRZB544AG3usGDBxtJZuLEia6xpKQk07Bhw99cpzHGnDx5slBdz549TePGjd3Gunbtarp27XrZno0xpmHDhuamm24yhw8fNocPHzZfffWV+fOf/2wkmb/+9a/Frm/GjBlGklmwYIFr7MyZMyY+Pt4EBQUZh8NhjDHm8OHDhZ4vAOvg9CWAcpeQkKC6desqOjpa/fv3V40aNbR8+XJdddVVkqSff/5ZH3/8sQYMGKBjx47pyJEjOnLkiH766Sf17NlTu3fvdn1aMzQ0VN9++612795d4u2vWrVKkjRq1Ci38YceeuiKnldgYKDr57y8PB05ckRdu3bVvn37lJeXV6Z1fvTRR6pbt67q1q2rtm3b6t1339WQIUM0derUYpdZtWqVIiMjNWjQINdYtWrVNGrUKB0/flzr1q0rUy8AKhanLwGUu5kzZ6pZs2bKy8vT3Llz9emnn8put7vm79mzR8YYjR8/XuPHjy9yHYcOHVJUVJQef/xx3XbbbWrWrJlatWqlm2++WUOGDLnsabgffvhBPj4+uvrqq93Gr7nmmit6Xp999pkmTpyoTZs26eTJk27z8vLyFBISUup1xsXF6cknn5TNZlP16tXVokULhYaGXnaZH374QU2bNpWPj/v/s1u0aOGaD8D6CGUAyl3Hjh1dn77s27evrr/+eg0ePFg7d+5UUFCQnE6nJOmRRx5Rz549i1xHkyZNJEk33HCD9u7dq3/961/66KOP9Oqrr+q5555TWlqahg8ffsW9FnfT2YKCArfHe/fu1Y033qjmzZvr2WefVXR0tPz9/bVq1So999xzrudUWmFhYUpISCjTsgAqN0IZgArl6+ur1NRUde/eXS+99JLGjh2rxo0bSzp/yq0kgaR27doaNmyYhg0bpuPHj+uGG27QpEmTig1lDRs2lNPp1N69e92Oju3cubNQba1atXT06NFC478+2vTBBx8oPz9fy5cvV4MGDVzjn3zyyW/272kNGzbU119/LafT6Xa07LvvvnPNl4oPnACsgWvKAFS4bt26qWPHjpoxY4ZOnz6t8PBwdevWTS+//LKys7ML1R8+fNj1808//eQ2LygoSE2aNFF+fn6x2+vVq5ck6YUXXnAbnzFjRqHaq6++Wnl5efr6669dY9nZ2YXuqu/r6ytJMsa4xvLy8jRv3rxi+ygvt9xyi3JycrRo0SLX2Llz5/Tiiy8qKChIXbt2lSRVr15dkooMnQC8jyNlALzi0Ucf1R133KH58+drxIgRmjlzpq6//nq1bt1a9957rxo3bqzc3Fxt2rRJP/74o7766itJUsuWLdWtWzd16NBBtWvX1tatW7VkyRI9+OCDxW6rXbt2GjRokGbNmqW8vDx16tRJ6enp2rNnT6HaP//5zxozZoxuv/12jRo1SidPntTs2bPVrFkzbd++3VV30003yd/fX3369NFf/vIXHT9+XHPmzFF4eHiRwbI83XfffXr55Zc1dOhQbdu2TTExMVqyZIk+++wzzZgxQzVr1pR0/oMJLVu21KJFi9SsWTPVrl1brVq1UqtWrSq0XwDF8PbHPwH8fl24JcaWLVsKzSsoKDBXX321ufrqq825c+eMMcbs3bvXJCYmmsjISFOtWjUTFRVl/u///s8sWbLEtdyTTz5pOnbsaEJDQ01gYKBp3ry5eeqpp8yZM2dcNUXdvuLUqVNm1KhRpk6dOqZGjRqmT58+Jisrq8hbRHz00UemVatWxt/f31xzzTVmwYIFRa5z+fLlpk2bNiYgIMDExMSYqVOnmrlz5xpJZv/+/a660twS47du91Hc+nJzc82wYcNMWFiY8ff3N61btzbz5s0rtOzGjRtNhw4djL+/P7fHACzGZswlx94BAADgFVxTBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwgCp381in06mDBw+qZs2afOUIAAAod8YYHTt2TPXr13f7KrRfq3Kh7ODBg4qOjvZ2GwAAoIrJysrSVVddVez8KhfKLnzdSFZWloKDg73cDQAA+L1zOByKjo52ZZDiVLlQduGUZXBwMKEMAABUmN+6bIoL/QEAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAAAAFkAoAwAAsABCGQAAgAUQygAAACygyt3RHwAAQJIKnAVan7le2ceyVa9mPXVp0EW+Pr5e64dQBgAAqpylO5YqeXWyfnT86Bq7KvgqPX/z8+rXop9XeuL0JQAAqFKW7liq/ov7uwUySTrgOKD+i/tr6Y6lXumLUAYAAKqMAmeBklcny8gUmndh7KHVD6nAWVDRrRHKAABA1bE+c32hI2SXMjLKcmRpfeb6CuzqPEIZAACoMrKPZXu0zpMIZQAAoMqoV7OeR+s8iVAGAACqjC4Nuuiq4Ktkk63I+TbZFB0crS4NulRwZ4QyAABQhfj6+Or5m5+XpELB7MLjGTfP8Mr9yghlAACgSunXop+WDFiiqOAot/Grgq/SkgFLvHafMpsxpvBnQn/HHA6HQkJClJeXp+DgYG+3AwAAvKSi7uhf0uzBHf0BAECV5Ovjq24x3bzdhgunLwEAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAArwayj799FP16dNH9evXl81m07Jly0q87GeffSY/Pz+1a9eu3PoDAACoKF4NZSdOnFDbtm01c+bMUi139OhRJSYm6sYbbyynzgAAACqWV+9T1qtXL/Xq1avUy40YMUKDBw+Wr69vqY6uAQAAWFWlu6Zs3rx52rdvnyZOnFii+vz8fDkcDrcJAADAaipVKNu9e7fGjh2rBQsWyM+vZAf5UlNTFRIS4pqio6PLuUsAAIDSqzShrKCgQIMHD9bkyZPVrFmzEi83btw45eXluaasrKxy7BIAAKBsKs13Xx47dkxbt27Vl19+qQcffFCS5HQ6ZYyRn5+fPvroI/3xj38stJzdbpfdbq/odgEAAEql0oSy4OBg/fe//3UbmzVrlj7++GMtWbJEjRo18lJnAAAAV86roez48ePas2eP6/H+/fuVkZGh2rVrq0GDBho3bpwOHDigN954Qz4+PmrVqpXb8uHh4QoICCg0DgAAUNl4NZRt3bpV3bt3dz1OSUmRJCUlJWn+/PnKzs5WZmamt9oDAACoMDZjjPF2ExXJ4XAoJCREeXl5Cg4O9nY7AADgd66k2aPSfPoSAADg94xQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACvBrKPv30U/Xp00f169eXzWbTsmXLLlu/dOlS9ejRQ3Xr1lVwcLDi4+P14YcfVkyzAAAA5ciroezEiRNq27atZs6cWaL6Tz/9VD169NCqVau0bds2de/eXX369NGXX35Zzp0CAACUL5sxxni7CUmy2Wx6//331bdv31Itd+2112rgwIGaMGFCieodDodCQkKUl5en4ODgMnQKAABQciXNHn4V2JPHOZ1OHTt2TLVr1y62Jj8/X/n5+a7HDoejIloDAAAolUp9of8///lPHT9+XAMGDCi2JjU1VSEhIa4pOjq6AjsEAAAomUobyhYuXKjJkydr8eLFCg8PL7Zu3LhxysvLc01ZWVkV2CUAAEDJVMrTl++8846GDx+ud999VwkJCZettdvtstvtFdQZAABA2VS6I2Vvv/22hg0bprffflu9e/f2djsAAAAe4dUjZcePH9eePXtcj/fv36+MjAzVrl1bDRo00Lhx43TgwAG98cYbks6fskxKStLzzz+vuLg45eTkSJICAwMVEhLilecAAADgCV49UrZ161a1b99e7du3lySlpKSoffv2rttbZGdnKzMz01X/yiuv6Ny5cxo5cqTq1avnmpKTk73SPwAAgKdY5j5lFYX7lAEAgIpU0uxR6a4pAwAA+D0ilAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAK+Gsk8//VR9+vRR/fr1ZbPZtGzZst9cZu3atbruuutkt9vVpEkTzZ8/v9z7BAAAKG9eDWUnTpxQ27ZtNXPmzBLV79+/X71791b37t2VkZGh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sshl6tWrp2rVqrl9mKBFixbKycnRmTNn3I7iXWC3210hEgAAwKpKFcrmzZvnsQ37+/urQ4cOSk9PV9++fSWdPxKWnp6uBx98sMhlOnfurIULF8rpdMrH5/yZ1127dqlevXpFBjIAAIDKokw3j/WUlJQUzZkzR6+//rp27Nih+++/XydOnHB9GjMxMVHjxo1z1d9///36+eeflZycrF27dmnlypWaMmWKRo4c6a2nAAAA4BFl+polTxk4cKAOHz6sCRMmKCcnR+3atdPq1atdF/9nZma6johJUnR0tD788EONHj1abdq0UVRUlJKTkzVmzBhvPQUAAACPsBljjLebqEgOh0MhISHKy8tTcHCwt9sBAAC/cyXNHl49fQkAAIDzCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALMASoWzmzJmKiYlRQECA4uLitHnz5hIt984778hms6lv377l2yAAAEA583ooW7RokVJSUjRx4kRt375dbdu2Vc+ePXXo0KHLLvf999/rkUceUZcuXSqoUwAAgPLj9VD27LPP6t5779WwYcPUsmVLpaWlqXr16po7d26xyxQUFOjOO+/U5MmT1bhx4wrsFgAAoHx4NZSdOXNG27ZtU0JCgmvMx8dHCQkJ2rRpU7HLPf744woPD9c999zzm9vIz8+Xw+FwmwAAAKzGq6HsyJEjKigoUEREhNt4RESEcnJyilxmw4YNeu211zRnzpwSbSM1NVUhISGuKTo6+or7BgAA8DSvn74sjWPHjmnIkCGaM2eOwsLCSrTMuHHjlJeX55qysrLKuUsAAIDS8/PmxsPCwuTr66vc3Fy38dzcXEVGRhaq37t3r77//nv16dPHNeZ0OiVJfn5+2rlzp66++mq3Zex2u+x2ezl0DwAA4DlePVLm7++vDh06KD093TXmdDqVnp6u+Pj4QvXNmzfXf//7X2VkZLimW2+9Vd27d1dGRganJgEAQKXl1SNlkpSSkqKkpCTFxsaqY8eOmjFjhk6cOKFhw4ZJkhITExUVFaXU1FQFBASoVatWbsuHhoZKUqFxAACAysTroWzgwIE6fPiwJkyYoJycHLVr106rV692XfyfmZkpH59KdekbAABAqdmMMcbbTVQkh8OhkJAQ5eXlKTg42NvtAACA37mSZg8OQQEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABRDKAAAALIBQBgAAYAGEMgAAAAsglAEAAFgAoQwAAMACCGUAAAAWQCgDAACwAEIZAACABVgilM2cOVMxMTEKCAhQXFycNm/eXGztnDlz1KVLF9WqVUu1atVSQkLCZesBAAAqA6+HskWLFiklJUUTJ07U9u3b1bZtW/Xs2VOHDh0qsn7t2rUaNGiQPvnkE23atEnR0dG66aabdODAgQruHAAAwHNsxhjjzQbi4uL0hz/8QS+99JIkyel0Kjo6Wn/96181duzY31y+oKBAtWrV0ksvvaTExMRC8/Pz85Wfn+967HA4FB0drby8PAUHB3vuiQAAABTB4XAoJCTkN7OHV4+UnTlzRtu2bVNCQoJrzMfHRwkJCdq0aVOJ1nHy5EmdPXtWtWvXLnJ+amqqQkJCXFN0dLRHegcAAPAkr4ayI0eOqKCgQBEREW7jERERysnJKdE6xowZo/r167sFu0uNGzdOeXl5rikrK+uK+wYAAPA0P283cCWefvppvfPOO1q7dq0CAgKKrLHb7bLb7RXcGQAAQOl4NZSFhYXJ19dXubm5buO5ubmKjIy87LL//Oc/9fTTT+s///mP2rRpU55tAgAAlDuvnr709/dXhw4dlJ6e7hpzOp1KT09XfHx8sctNmzZNTzzxhFavXq3Y2NiKaBUAAKBcef30ZUpKipKSkhQbG6uOHTtqxowZOnHihIYNGyZJSkxMVFRUlFJTUyVJU6dO1YQJE7Rw4ULFxMS4rj0LCgpSUFCQ154HAADAlfB6KBs4cKAOHz6sCRMmKCcnR+3atdPq1atdF/9nZmbKx+fiAb3Zs2frzJkz6t+/v9t6Jk6cqEmTJlVk6wAAAB7j9fuUVbSS3isEAADAEyrFfcoAAABwHqEMAADAAghlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlAAAAFkAoAwAAsABLhLKZM2cqJiZGAQEBiouL0+bNmy9b/+6776p58+YKCAhQ69attWrVqgrqFAAAoHx4PZQtWrRIKSkpmjhxorZv3662bduqZ8+eOnToUJH1Gzdu1KBBg3TPPffoyy+/VN++fdW3b1998803Fdw5AACA59iMMcabDcTFxekPf/iDXnrpJUmS0+lUdHS0/vrXv2rs2LGF6gcOHKgTJ05oxYoVrrH/9//+n9q1a6e0tLTf3J7D4VBISIjyDh5UcHBw4QJfXykg4OLjEyeKX5mPjxQYWLbakyel4n71NptUvXrZak+dkpzO4vuoUaNstadPSwUFnqmtXv1835KUny+dO+eZ2sDA879nSTpzRjp71jO1AQHn/y5KW3v27Pn64tjtkp9f6WvPnTv/uyiOv79UrVrpawsKzu+74lSrdr6+tLVO5/m/NU/U+vmd/11I518TJ096prY0r3veI4qu5T2i9LW8R5z/uQq8RzgcDoXUr6+8vLyis8cFxovy8/ONr6+vef/9993GExMTza233lrkMtHR0ea5555zG5swYYJp06ZNkfWnT582eXl5rikrK8tIMnnnd0Hh6ZZb3FdQvXrRdZIxXbu614aFFV8bG+te27Bh8bUtW7rXtmxZfG3Dhu61sbHF14aFudd27Vp8bfXq7rW33FJ87a//jPr3v3zt8eMXa5OSLl976NDF2gceuHzt/v0Xax955PK133xzsXbixMvXbt58sXbatMvXfvLJxdqXXrp87YoVF2vnzbt87eLFF2sXL7587bx5F2tXrLh87UsvXaz95JPL106bdrF28+bL106ceLH2m28uX/vIIxdr9++/fO0DD1ysPXTo8rVJSRdrjx+/fG3//sbN5Wp5jzg/8R5xceI94vzEe8T5qYj3iDzJSDJ5eXnmcrx6+vLIkSMqKChQRESE23hERIRycnKKXCYnJ6dU9ampqQoJCXFN0dHRnmkeAADAg7x6+vLgwYOKiorSxo0bFR8f7xp/7LHHtG7dOn3xxReFlvH399frr7+uQYMGucZmzZqlyZMnKzc3t1B9fn6+8i85NOtwOBQdHc3py9LWcmqi9LWcmjj/cxU4NVEs3iPKVst7xHm8R5S+1qLvESU9felX/FrLX1hYmHx9fQuFqdzcXEVGRha5TGRkZKnq7Xa77Bd+6ZeqUcP9TaI4JakpS+2lb5KerL30Td2TtZf+gXmy1m6/+KLwZK2//8UXsbdqq1W7+GbmyVo/v4tvvp6s9fUt+d9waWp9fMqn1mYrn1rJGrW8R5zHe0Tpa3mPOM9K7xGX+0/IJbx6+tLf318dOnRQenq6a8zpdCo9Pd3tyNml4uPj3eolac2aNcXWAwAAVAZePVImSSkpKUpKSlJsbKw6duyoGTNm6MSJExo2bJgkKTExUVFRUUpNTZUkJScnq2vXrpo+fbp69+6td955R1u3btUrr7zizacBAABwRbweygYOHKjDhw9rwoQJysnJUbt27bR69WrXxfyZmZny8bl4QK9Tp05auHCh/vGPf+hvf/ubmjZtqmXLlqlVq1beegoAAABXzOv3KatorvuU/da9QgAAADygpNnD63f0BwAAAKEMAADAEghlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAArz+3ZcV7cK3SjkcDi93AgAAqoILmeO3vtmyyoWyY8eOSZKio6O93AkAAKhKjh07ppCQkGLnV7kvJHc6nTp48KBq1qwpm832m/UOh0PR0dHKysriC8wrCfZZ5cL+qnzYZ5UP+8y7jDE6duyY6tevLx+f4q8cq3JHynx8fHTVVVeVerng4GD+kCsZ9lnlwv6qfNhnlQ/7zHsud4TsAi70BwAAsABCGQAAgAUQyn6D3W7XxIkTZbfbvd0KSoh9Vrmwvyof9lnlwz6rHKrchf4AAABWxJEyAAAACyCUAQAAWAChDAAAwAIIZQAAABZAKCvC008/LZvNpoceesg1dvr0aY0cOVJ16tRRUFCQ/vSnPyk3N9d7TVZxkyZNks1mc5uaN2/ums/+sqYDBw7orrvuUp06dRQYGKjWrVtr69atrvnGGE2YMEH16tVTYGCgEhIStHv3bi92XLXFxMQUep3ZbDaNHDlSEq8zqykoKND48ePVqFEjBQYG6uqrr9YTTzzh9n2LvMasjVD2K1u2bNHLL7+sNm3auI2PHj1aH3zwgd59912tW7dOBw8eVL9+/bzUJSTp2muvVXZ2tmvasGGDax77y3p++eUXde7cWdWqVdO///1v/e9//9P06dNVq1YtV820adP0wgsvKC0tTV988YVq1Kihnj176vTp017svOrasmWL22tszZo1kqQ77rhDEq8zq5k6dapmz56tl156STt27NDUqVM1bdo0vfjii64aXmMWZ+By7Ngx07RpU7NmzRrTtWtXk5ycbIwx5ujRo6ZatWrm3XffddXu2LHDSDKbNm3yUrdV28SJE03btm2LnMf+sqYxY8aY66+/vtj5TqfTREZGmmeeecY1dvToUWO3283bb79dES3iNyQnJ5urr77aOJ1OXmcW1Lt3b3P33Xe7jfXr18/ceeedxhheY5UBR8ouMXLkSPXu3VsJCQlu49u2bdPZs2fdxps3b64GDRpo06ZNFd0m/n+7d+9W/fr11bhxY915553KzMyUxP6yquXLlys2NlZ33HGHwsPD1b59e82ZM8c1f//+/crJyXHbbyEhIYqLi2O/WcCZM2e0YMEC3X333bLZbLzOLKhTp05KT0/Xrl27JElfffWVNmzYoF69ekniNVYZVLkvJC/OO++8o+3bt2vLli2F5uXk5Mjf31+hoaFu4xEREcrJyamgDnGpuLg4zZ8/X9dcc42ys7M1efJkdenSRd988w37y6L27dun2bNnKyUlRX/729+0ZcsWjRo1Sv7+/kpKSnLtm4iICLfl2G/WsGzZMh09elRDhw6VxPuiFY0dO1YOh0PNmzeXr6+vCgoK9NRTT+nOO++UJF5jlQChTFJWVpaSk5O1Zs0aBQQEeLsdlMCF//lJUps2bRQXF6eGDRtq8eLFCgwM9GJnKI7T6VRsbKymTJkiSWrfvr2++eYbpaWlKSkpycvd4be89tpr6tWrl+rXr+/tVlCMxYsX66233tLChQt17bXXKiMjQw899JDq16/Pa6yS4PSlzp/uOnTokK677jr5+fnJz89P69at0wsvvCA/Pz9FRETozJkzOnr0qNtyubm5ioyM9E7TcBMaGqpmzZppz549ioyMZH9ZUL169dSyZUu3sRYtWrhOO1/YN7/+9B77zft++OEH/ec//9Hw4cNdY7zOrOfRRx/V2LFj9ec//1mtW7fWkCFDNHr0aKWmpkriNVYZEMok3Xjjjfrvf/+rjIwM1xQbG6s777zT9XO1atWUnp7uWmbnzp3KzMxUfHy8FzvHBcePH9fevXtVr149dejQgf1lQZ07d9bOnTvdxnbt2qWGDRtKkho1aqTIyEi3/eZwOPTFF1+w37xs3rx5Cg8PV+/evV1jvM6s5+TJk/Lxcf9n3dfXV06nUxKvsUrB2580sKpLP31pjDEjRowwDRo0MB9//LHZunWriY+PN/Hx8d5rsIp7+OGHzdq1a83+/fvNZ599ZhISEkxYWJg5dOiQMYb9ZUWbN282fn5+5qmnnjK7d+82b731lqlevbpZsGCBq+bpp582oaGh5l//+pf5+uuvzW233WYaNWpkTp065cXOq7aCggLToEEDM2bMmELzeJ1ZS1JSkomKijIrVqww+/fvN0uXLjVhYWHmsccec9XwGrM2Qlkxfh3KTp06ZR544AFTq1YtU716dXP77beb7Oxs7zVYxQ0cONDUq1fP+Pv7m6ioKDNw4ECzZ88e13z2lzV98MEHplWrVsZut5vmzZubV155xW2+0+k048ePNxEREcZut5sbb7zR7Ny500vdwhhjPvzwQyOpyP3A68xaHA6HSU5ONg0aNDABAQGmcePG5u9//7vJz8931fAaszabMZfc6hcAAABewTVlAAAAFkAoAwAAsABCGQAAgAUQygAAACyAUAYAAGABhDIAAAALIJQBAABYAKEMAADAAghlACqloUOHqm/fvq7H3bp100MPPVThfaxdu1Y2m63QF3N7ms1m07Jly8p1GwC8i1AGwGOGDh0qm80mm80mf39/NWnSRI8//rjOnTtX7tteunSpnnjiiRLVVlSQOnPmjMLCwvT0008XOf+JJ55QRESEzp49W659AKgcCGUAPOrmm29Wdna2du/erYcffliTJk3SM888U2TtmTNnPLbd2rVrq2bNmh5bnyf4+/vrrrvu0rx58wrNM8Zo/vz5SkxMVLVq1bzQHQCrIZQB8Ci73a7IyEg1bNhQ999/vxISErR8+XJJF085PvXUU6pfv76uueYaSVJWVpYGDBig0NBQ1a5dW7fddpu+//571zoLCgqUkpKi0NBQ1alTR4899ph+/bW9vz59mZ+frzFjxig6Olp2u11NmjTRa6+9pu+//17du3eXJNWqVUs2m01Dhw6VJDmdTqWmpqpRo0YKDAxU27ZttWTJErftrFq1Ss2aNVNgYKC6d+/u1mdR7rnnHu3atUsbNmxwG1+3bp327dune+65R1u2bFGPHj0UFhamkJAQde3aVdu3by92nUUd6cvIyJDNZnPrZ8OGDerSpYsCAwMVHR2tUaNG6cSJE675s2bNUtOmTRUQEKCIiAj179//ss8FQPkilAEoV4GBgW5HxNLT07Vz506tWbNGK1as0NmzZ9WzZ0/VrFlT69ev12effaagoCDdfPPNruWmT5+u+fPna+7cudqwYYN+/vlnvf/++5fdbmJiot5++2298MIL2rFjh15++WUFBQUpOjpa7733niRp586dys7O1vPPPy9JSk1N1RtvvKG0tDR9++23Gj16tO666y6tW7dO0vnw2K9fP/Xp00cZGRkaPny4xo4de9k+WrdurT/84Q+aO3eu2/i8efPUqVMnNW/eXMeOHVNSUpI2bNigzz//XE2bNtUtt9yiY8eOle6XfYm9e/fq5ptv1p/+9Cd9/fXXWrRokTZs2KAHH3xQkrR161aNGjVKjz/+uHbu3KnVq1frhhtuKPP2AHiAAQAPSUpKMrfddpsxxhin02nWrFlj7Ha7eeSRR1zzIyIiTH5+vmuZN99801xzzTXG6XS6xvLz801gYKD58MMPjTHG1KtXz0ybNs01/+zZs+aqq65ybcsYY7p27WqSk5ONMcbs3LnTSDJr1qwpss9PPvnESDK//PKLa+z06dOmevXqZuPGjW6199xzjxk0aJAxxphx48aZli1bus0fM2ZMoXX9WlpamgkKCjLHjh0zxhjjcDhM9erVzauvvlpkfUFBgalZs6b54IMPXGOSzPvvv19s/19++aWRZPbv3+/q+7777nNb7/r1642Pj485deqUee+990xwcLBxOBzF9g2gYnGkDIBHrVixQkFBQQoICFCvXr00cOBATZo0yTW/devW8vf3dz3+6quvtGfPHtWsWVNBQUEKCgpS7dq1dfr0ae3du1d5eXnKzs5WXFycaxk/Pz/FxsYW20NGRoZ8fX3VtWvXEve9Z88enTx5Uj169HD1ERQUpDfeeEN79+6VJO3YscOtD0mKj4//zXUPGjRIBQUFWrx4sSRp0aJF8vHx0cCBAyVJubm5uvfee9W0aVOFhIQoODhYx48fV2ZmZon7/7WvvvpK8+fPd3suPXv2lNPp1P79+9WjRw81bNhQjRs31pAhQ/TWW2/p5MmTZd4egCvn5+0GAPy+dO/eXbNnz5a/v7/q168vPz/3t5kaNWq4PT5+/Lg6dOigt956q9C66tatW6YeAgMDS73M8ePHJUkrV65UVFSU2zy73V6mPi4IDg5W//79NW/ePN19992aN2+eBgwYoKCgIElSUlKSfvrpJz3//PNq2LCh7Ha74uPji/0ghI/P+f9Pm0uuq/v1JziPHz+uv/zlLxo1alSh5Rs0aCB/f39t375da9eu1UcffaQJEyZo0qRJ2rJli0JDQ6/o+QIoG0IZAI+qUaOGmjRpUuL66667TosWLVJ4eLiCg4OLrKlXr56++OIL1zVP586d07Zt23TdddcVWd+6dWs5nU6tW7dOCQkJheZfOFJXUFDgGmvZsqXsdrsyMzOLPcLWokUL14cWLvj8889/+0nq/AX/3bp104oVK7Rx40a3T6R+9tlnmjVrlm655RZJ569dO3LkSLHruhBWs7OzVatWLUnnjw5e6rrrrtP//ve/y+4LPz8/JSQkKCEhQRMnTlRoaKg+/vhj9evXr0TPCYBncfoSgFfdeeedCgsL02233ab169dr//79Wrt2rUaNGqUff/xRkpScnKynn35ay5Yt03fffacHHnjgsvcYi4mJUVJSku6++24tW7bMtc4Lpw8bNmwom82mFStW6PDhwzp+/Lhq1qypRx55RKNHj9brr7+uvXv3avv27XrxxRf1+uuvS5JGjBih3bt369FHH9XOnTu1cOFCzZ8/v0TP84YbblCTJk2UmJio5s2bq1OnTq55TZs21ZtvvqkdO3boiy++0J133nnZo31NmjRRdHS0Jk2apN27d2vlypWaPn26W82YMWO0ceNGPfjgg8rIyNDu3bv1r3/9y3Wh/4oVK/TCCy8oIyNDP/zwg9544w05nU7XJ2IBVDxCGQCvql69uj799FM1aNBA/fr1U4sWLXTPPffo9OnTriNnDz/8sIYMGaKkpCTFx8erZs2auv322y+73tmzZ6t///564IEH1Lx5c917772u20FERUVp8uTJGjt2rCIiIlxB5YknntD48eOVmpqqFi1a6Oabb9bKlSvVqFEjSedP+7333ntatmyZ2rZtq7S0NE2ZMqVEz9Nms+nuu+/WL7/8orvvvttt3muvvaZffvlF1113nYYMGaJRo0YpPDy82HVVq1ZNb7/9tr777ju1adNGU6dO1ZNPPulW06ZNG61bt067du1Sly5d1L59e02YMEH169eXJIWGhmrp0qX64x//qBYtWigtLU1vv/22rr322hI9HwCeZzPmVzf7AQAAQIXjSBkAAIAFEMoAAAAsgFAGAABgAYQyAAAACyCUAQAAWAChDAAAwAIIZQAAABZAKAMAALAAQhkAAIAFEMoAAAAsgFAGAABgAf8f4DQb3ow2OQkAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**B]Simple Linear Regression by using Numpy**"
      ],
      "metadata": {
        "id": "6Xdc1Bu4Iwn4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#independent Variables\n",
        "x = df[\"study_Hours\"].values\n",
        "\n",
        "#Dependent Variable (Target)\n",
        "y = df[\"Marks\"].values"
      ],
      "metadata": {
        "id": "Yg1GIyL9I4sy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Calculate mean\n",
        "x_mean = np.mean(x)\n",
        "y_mean = np.mean(y)"
      ],
      "metadata": {
        "id": "puxZw6AQJiKH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Calculate slope\n",
        "m = np.sum((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2)\n",
        "\n",
        "#Calculate intercept\n",
        "b = y_mean -m*x_mean\n",
        "\n",
        "print(\"Slope = \", m)\n",
        "print(\"Intercept = \", b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GbiIIEq1JtjW",
        "outputId": "876f323e-a1b5-4661-f3c4-2005d11f5b58"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Slope =  6.503030303030303\n",
            "Intercept =  28.33333333333333\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Prediction\n",
        "y_pred_numpy =m*x + b\n",
        "y_pred_numpy"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ve3MX-IWKREr",
        "outputId": "d62e0042-3f9f-4e5a-d745-9d6b4ad8289f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([34.83636364, 41.33939394, 47.84242424, 54.34545455, 60.84848485,\n",
              "       67.35151515, 73.85454545, 80.35757576, 86.86060606, 93.36363636])"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Multiple Linear Regression**"
      ],
      "metadata": {
        "id": "8dvWyS5AKj3E"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Feature Selection\n",
        "x = df[['study_Hours', 'Attendance']]  #Independent Variables\n",
        "y = df['Marks']  # Dependent variables\n",
        "\n",
        "# Split Dataset\n",
        "x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)"
      ],
      "metadata": {
        "id": "zIzfDZucKrGM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Model Building**"
      ],
      "metadata": {
        "id": "QTbYAfslMB4y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model=LinearRegression()\n",
        "model.fit(x_train, y_train)"
      ],
      "metadata": {
        "id": "BhAmNB_ZMAi1",
        "outputId": "45ecd6d7-8ba9-47e4-c141-bcd170bc2aff",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {\n",
              "  /* Definition of color scheme common for light and dark mode */\n",
              "  --sklearn-color-text: #000;\n",
              "  --sklearn-color-text-muted: #666;\n",
              "  --sklearn-color-line: gray;\n",
              "  /* Definition of color scheme for unfitted estimators */\n",
              "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
              "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
              "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
              "  --sklearn-color-unfitted-level-3: chocolate;\n",
              "  /* Definition of color scheme for fitted estimators */\n",
              "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
              "  --sklearn-color-fitted-level-1: #d4ebff;\n",
              "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
              "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
              "\n",
              "  /* Specific color for light theme */\n",
              "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
              "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-icon: #696969;\n",
              "\n",
              "  @media (prefers-color-scheme: dark) {\n",
              "    /* Redefinition of color scheme for dark theme */\n",
              "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
              "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-icon: #878787;\n",
              "  }\n",
              "}\n",
              "\n",
              "#sk-container-id-2 {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 pre {\n",
              "  padding: 0;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 input.sk-hidden--visually {\n",
              "  border: 0;\n",
              "  clip: rect(1px 1px 1px 1px);\n",
              "  clip: rect(1px, 1px, 1px, 1px);\n",
              "  height: 1px;\n",
              "  margin: -1px;\n",
              "  overflow: hidden;\n",
              "  padding: 0;\n",
              "  position: absolute;\n",
              "  width: 1px;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-dashed-wrapped {\n",
              "  border: 1px dashed var(--sklearn-color-line);\n",
              "  margin: 0 0.4em 0.5em 0.4em;\n",
              "  box-sizing: border-box;\n",
              "  padding-bottom: 0.4em;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-container {\n",
              "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
              "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
              "     so we also need the `!important` here to be able to override the\n",
              "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
              "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
              "  display: inline-block !important;\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-text-repr-fallback {\n",
              "  display: none;\n",
              "}\n",
              "\n",
              "div.sk-parallel-item,\n",
              "div.sk-serial,\n",
              "div.sk-item {\n",
              "  /* draw centered vertical line to link estimators */\n",
              "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
              "  background-size: 2px 100%;\n",
              "  background-repeat: no-repeat;\n",
              "  background-position: center center;\n",
              "}\n",
              "\n",
              "/* Parallel-specific style estimator block */\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel-item::after {\n",
              "  content: \"\";\n",
              "  width: 100%;\n",
              "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
              "  flex-grow: 1;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel {\n",
              "  display: flex;\n",
              "  align-items: stretch;\n",
              "  justify-content: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel-item {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel-item:first-child::after {\n",
              "  align-self: flex-end;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel-item:last-child::after {\n",
              "  align-self: flex-start;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-parallel-item:only-child::after {\n",
              "  width: 0;\n",
              "}\n",
              "\n",
              "/* Serial-specific style estimator block */\n",
              "\n",
              "#sk-container-id-2 div.sk-serial {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "  align-items: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  padding-right: 1em;\n",
              "  padding-left: 1em;\n",
              "}\n",
              "\n",
              "\n",
              "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
              "clickable and can be expanded/collapsed.\n",
              "- Pipeline and ColumnTransformer use this feature and define the default style\n",
              "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
              "*/\n",
              "\n",
              "/* Pipeline and ColumnTransformer style (default) */\n",
              "\n",
              "#sk-container-id-2 div.sk-toggleable {\n",
              "  /* Default theme specific background. It is overwritten whether we have a\n",
              "  specific estimator or a Pipeline/ColumnTransformer */\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "/* Toggleable label */\n",
              "#sk-container-id-2 label.sk-toggleable__label {\n",
              "  cursor: pointer;\n",
              "  display: flex;\n",
              "  width: 100%;\n",
              "  margin-bottom: 0;\n",
              "  padding: 0.5em;\n",
              "  box-sizing: border-box;\n",
              "  text-align: center;\n",
              "  align-items: start;\n",
              "  justify-content: space-between;\n",
              "  gap: 0.5em;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 label.sk-toggleable__label .caption {\n",
              "  font-size: 0.6rem;\n",
              "  font-weight: lighter;\n",
              "  color: var(--sklearn-color-text-muted);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 label.sk-toggleable__label-arrow:before {\n",
              "  /* Arrow on the left of the label */\n",
              "  content: \"▸\";\n",
              "  float: left;\n",
              "  margin-right: 0.25em;\n",
              "  color: var(--sklearn-color-icon);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "/* Toggleable content - dropdown */\n",
              "\n",
              "#sk-container-id-2 div.sk-toggleable__content {\n",
              "  max-height: 0;\n",
              "  max-width: 0;\n",
              "  overflow: hidden;\n",
              "  text-align: left;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-toggleable__content.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-toggleable__content pre {\n",
              "  margin: 0.2em;\n",
              "  border-radius: 0.25em;\n",
              "  color: var(--sklearn-color-text);\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-toggleable__content.fitted pre {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
              "  /* Expand drop-down */\n",
              "  max-height: 200px;\n",
              "  max-width: 100%;\n",
              "  overflow: auto;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
              "  content: \"▾\";\n",
              "}\n",
              "\n",
              "/* Pipeline/ColumnTransformer-specific style */\n",
              "\n",
              "#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator-specific style */\n",
              "\n",
              "/* Colorize estimator box */\n",
              "#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-label label.sk-toggleable__label,\n",
              "#sk-container-id-2 div.sk-label label {\n",
              "  /* The background is the default theme color */\n",
              "  color: var(--sklearn-color-text-on-default-background);\n",
              "}\n",
              "\n",
              "/* On hover, darken the color of the background */\n",
              "#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "/* Label box, darken color on hover, fitted */\n",
              "#sk-container-id-2 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator label */\n",
              "\n",
              "#sk-container-id-2 div.sk-label label {\n",
              "  font-family: monospace;\n",
              "  font-weight: bold;\n",
              "  display: inline-block;\n",
              "  line-height: 1.2em;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-label-container {\n",
              "  text-align: center;\n",
              "}\n",
              "\n",
              "/* Estimator-specific */\n",
              "#sk-container-id-2 div.sk-estimator {\n",
              "  font-family: monospace;\n",
              "  border: 1px dotted var(--sklearn-color-border-box);\n",
              "  border-radius: 0.25em;\n",
              "  box-sizing: border-box;\n",
              "  margin-bottom: 0.5em;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-estimator.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "/* on hover */\n",
              "#sk-container-id-2 div.sk-estimator:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-2 div.sk-estimator.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
              "\n",
              "/* Common style for \"i\" and \"?\" */\n",
              "\n",
              ".sk-estimator-doc-link,\n",
              "a:link.sk-estimator-doc-link,\n",
              "a:visited.sk-estimator-doc-link {\n",
              "  float: right;\n",
              "  font-size: smaller;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1em;\n",
              "  height: 1em;\n",
              "  width: 1em;\n",
              "  text-decoration: none !important;\n",
              "  margin-left: 0.5em;\n",
              "  text-align: center;\n",
              "  /* unfitted */\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted,\n",
              "a:link.sk-estimator-doc-link.fitted,\n",
              "a:visited.sk-estimator-doc-link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "/* Span, style for the box shown on hovering the info icon */\n",
              ".sk-estimator-doc-link span {\n",
              "  display: none;\n",
              "  z-index: 9999;\n",
              "  position: relative;\n",
              "  font-weight: normal;\n",
              "  right: .2ex;\n",
              "  padding: .5ex;\n",
              "  margin: .5ex;\n",
              "  width: min-content;\n",
              "  min-width: 20ex;\n",
              "  max-width: 50ex;\n",
              "  color: var(--sklearn-color-text);\n",
              "  box-shadow: 2pt 2pt 4pt #999;\n",
              "  /* unfitted */\n",
              "  background: var(--sklearn-color-unfitted-level-0);\n",
              "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted span {\n",
              "  /* fitted */\n",
              "  background: var(--sklearn-color-fitted-level-0);\n",
              "  border: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link:hover span {\n",
              "  display: block;\n",
              "}\n",
              "\n",
              "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
              "\n",
              "#sk-container-id-2 a.estimator_doc_link {\n",
              "  float: right;\n",
              "  font-size: 1rem;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1rem;\n",
              "  height: 1rem;\n",
              "  width: 1rem;\n",
              "  text-decoration: none;\n",
              "  /* unfitted */\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 a.estimator_doc_link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "#sk-container-id-2 a.estimator_doc_link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "#sk-container-id-2 a.estimator_doc_link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>LinearRegression</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LinearRegression.html\">?<span>Documentation for LinearRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>LinearRegression()</pre></div> </div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Preidction\n",
        "y_pred = model.predict(x_test)\n",
        "y_pred"
      ],
      "metadata": {
        "id": "D7rC5jcNMTgD",
        "outputId": "e9094678-965b-4aa4-a47d-e543d088f92a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([88.08653885, 43.59718321, 67.84336712])"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Model Parameters\n",
        "print('Intercept:' , model.intercept_)\n",
        "print (\"Coefficient\",)\n",
        "coeff=pd.DataFrame({'Feature': x.columns, 'Coefficient': model.coef_})\n",
        "print(coeff)"
      ],
      "metadata": {
        "id": "9sPRbxN5Mf33",
        "outputId": "52def7a3-176b-4cc6-c266-8c98d1eb87b4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intercept: 16.14458419831481\n",
            "Coefficient\n",
            "       Feature  Coefficient\n",
            "0  study_Hours     6.280539\n",
            "1   Attendance     0.175194\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "MLR Equation\n",
        "\n",
        "\n",
        "*   Marks=(6.29 Study_Hours)+(0.18 Attendence) + 16.15\n",
        "\n",
        "```\n",
        "`# This is formatted as code`\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "U_btgyxTNPO2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Model Evaluation**"
      ],
      "metadata": {
        "id": "_1Ify_ClNmrD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Evaluation Metrics\n",
        "print('Metrics value of MLR:')\n",
        "rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n",
        "r2 = r2_score(y_test, y_pred)\n",
        "print('RMSE:', round(rmse,3))\n",
        "print('R2 Score:',round(r2,2))"
      ],
      "metadata": {
        "id": "2TEu7t0INif0",
        "outputId": "280ee5bb-2cd8-437e-929b-908873466cdf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Metrics value of MLR:\n",
            "RMSE: 1.044\n",
            "R2 Score: 1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Actual vs Predicted Plot\n",
        "plt.figure(figsize=(7,5))\n",
        "plt.scatter(y_test, y_pred, color='purple')\n",
        "\n",
        "#Perfect Prediction Line\n",
        "plt.plot([y.min(), y.max()], [y_pred.min(), y_pred.max()], color='red')\n",
        "plt.xlabel('Actual')\n",
        "plt.ylabel('Predicted Marks')\n",
        "plt.title('Actual vs Predicted')\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "CPtdbdomOJEj",
        "outputId": "c765da94-a65f-4b7e-b0f2-8662dcaafacb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 700x500 with 1 Axes>"
            ],
            "image/png": "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59NPP6VHjx7UqVOHAwcO8Pbbb3PfffcxatQoatWqxYQJE7j//vvp2rUrd955JwcOHGD+/PllWm/10ksvkZCQQLt27bjvvvto1qwZn376KWvWrHE9Zuq6664D4IknnqB3797UqlWL2267rdJqFJHv2HRXpohUkttuu80KDAy0Tp06dclzBgwYYNWqVcv66quvLMuyrK+//toaOnSo1ahRI8vf39+68sorrf79+7vetyzLWrVqlRUXF2f5+fldsE3C1KlTrUaNGlkBAQHWDTfcYG3btu2CLSpKSkqsZ5991oqOjrYCAgKstm3bWu+8847Vv39/Kzo6ulR9lGGLivOcTqcVFBRkAdaSJUsueH/ChAlWhw4drLp161pBQUFWq1atrLS0NKuwsPAnP/f8FhXLly//yfPOb1Fx9OjRi76/YsUKKyEhwQoODraCg4OtVq1aWQ8++KCVm5tb6ryZM2dazZo1swICAqz27dtb//znPy+4hhfbosKyLGvPnj3W7bffbtWtW9cKDAy0rr76amvMmDGlznnmmWesRo0aWT4+PhdsV+HJGkXk0hyW9aOes4iIiIhUOK0JExEREbGBQpiIiIiIDRTCRERERGygECYiIiJiA4UwERERERvYGsIKCgoYMWIE0dHRBAUFcf311/PBBx+43rcsi7Fjx9KwYUOCgoJISkoq90N3RURERLyJrZu1Dh48mD179rB48WKioqJYsmQJSUlJ/Pe//6VRo0ZMnjyZl156iYULF9KsWTPGjBnDzTffzH//+18CAwPL9B0lJSUcOnSIOnXq/OSjVkREREQul2VZFBQUEBUVhY/Pz/S67Nqg7Ntvv7V8fX2td955p9Txdu3aWU888YRVUlJiRUZGWlOmTHG9d/z4cSsgIMB64403yvw9eXl5FqCXXnrppZdeeulVaa+8vLyfzSi2dcKKioooLi6+oKMVFBTEpk2bOHDgAIcPHyYpKcn1XmhoKB07diQnJ4fevXtf9HPPnj1b6hlw1nd70ebl5RESElIBP4mIiIiI4XQ6ady4MXXq1PnZc20LYXXq1KFz584888wzxMbGEhERwRtvvEFOTg4tW7bk8OHDAERERJT6exEREa73LmbixImMHz/+guMhISEKYSIiIlIpyrIEytaF+YsXL8ayLBo1akRAQAAvvfQSd91118/Pof6Exx9/nBMnTrheeXl5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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Residual Plot**\n"
      ],
      "metadata": {
        "id": "0crA345GPDe6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "residuals =y_test - y_pred  #calculate residual\n",
        "\n",
        "plt.scatter(y_pred, residuals, color='orange')\n",
        "plt.axhline(y=0, color='red', linestyle='--')\n",
        "plt.xlabel('Predicted Marks')\n",
        "plt.ylabel('Residuals')\n",
        "plt.title('Residual Plot(MLR)')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "Vk2F7r0vPHC7",
        "outputId": "8a0cf6c3-c2ed-43e4-f6b7-baf70f973b73",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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1KlTTuMXL17UmTNnCj10tnbtWh08eFBBQUFO4w8++KDuuOMOrV+/vsDlfHx85OPjU9ynAAAArkEuDUghISEKCQm5Yl10dLTS0tK0a9cutW3bVlJeAMrNzVX79u0LXCY+Pl7Dhg1zGmvRooVmzZqle++9t+zNAwCAa5ZbXMXWtGlTdevWTcOHD9e8efOUnZ2tUaNGqX///o4r2I4dO6YuXbron//8p2699VaFhYUVuHepXr16atCgQWU/BQAA4Ebc4iRtSVq8eLGioqLUpUsX9ejRQx07dtSbb77pmJ+dna2kpCRlZma6sEsAAHAtsBljjKubuJqlp6crMDBQdrtdAQEBrm4HAAAUQ1m/v91mDxIAAEBlISABAABYEJAAAAAsCEgAAAAWBCQAAAALAhIAAIAFAQkAAMCCgAQAAGBBQAIAALAgIAEAAFgQkAAAACwISAAAABYEJAAAAAsCEgAAgAUBCQAAwIKABAAAYEFAAgAAsCAgAQAAWBCQAAAALAhIAAAAFgQkAAAACwISAACABQEJAADAgoAEAABgQUACAACwICABAABYEJAAAAAsCEgAAAAWBCQAAAALAhIAAIAFAQkAAMDCbQLSmTNnFBsbq4CAAAUFBWno0KHKyMi44nJbt27V73//e1WrVk0BAQG68847de7cuUroGAAAuCu3CUixsbHas2ePVq9erZUrV+rrr7/WY489VuQyW7duVbdu3XTPPfdo+/bt2rFjh0aNGiUPD7d52gAAwAVsxhjj6iauZO/evWrWrJl27Nihdu3aSZJWrVqlHj166OjRo6pTp06By9122226++679fzzz5d62+np6QoMDJTdbldAQECp1wMAACpPWb+/3WJXytatWxUUFOQIR5IUExMjDw8Pbdu2rcBlTp06pW3btik0NFQdOnRQrVq11KlTJ23atKnIbWVlZSk9Pd1pAgAA1xe3CEgpKSkKDQ11GvP09FSNGjWUkpJS4DI//vijJGnq1KkaPny4Vq1apVtuuUVdunTR/v37C91WQkKCAgMDHVN4eHj5PREAAOAWXBqQ4uPjZbPZipz27dtXqnXn5uZKkh5//HE98sgjatOmjWbNmqUmTZronXfeKXS5iRMnym63O6bk5ORSbR8AALgvT1dufPz48YqLiyuypmHDhgoLC9OpU6ecxi9evKgzZ84oLCyswOVq164tSWrW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SrUHyWaz6U9/+pPOnDmj3bt365tvvlFqaqoCAwPVoEGD8u4RAACgUpUoIGVlZWnixIlq166dbr/9dn322Wdq1qyZ9uzZoyZNmujVV1/VuHHjKqpXAACASlGiQ2yTJ0/W3//+d8XExGjLli3q27evHnnkEX3zzTeaOXOm+vbtqypV+IFGAADg3koUkD766CP985//1H333afdu3erZcuWunjxor777jvZbLaK6hEAAKBSlegQ29GjR9W2bVtJUvPmzeXj46Nx48YRjgAAwDWlRAEpJydH3t7ejseenp7y9/cv96YAAABcqUSH2IwxiouLk4+PjyTp/PnzeuKJJ1StWjWnuk8++aT8OgQAAKhkJQpIQ4YMcXo8aNCgcm0GAADgalCigDR//vyK6gMAAOCqUaobRQIAAFzLCEgAAAAWBCQAAAALtwlI06dPV4cOHeTn56egoKBiLWOM0eTJk1W7dm35+voqJiZG+/fvr9hGAQCA23ObgHThwgX17dtXI0aMKPYyL7/8subMmaN58+Zp27Ztqlatmrp27arz589XYKcAAMDd2YwxxtVNlMSCBQs0duxYpaWlFVlnjFGdOnU0fvx4Pf3005Iku92uWrVqacGCBerfv3+xtpeenq7AwEDZ7XYFBASUtX0AAFAJyvr97TZ7kErq0KFDSklJUUxMjGMsMDBQ7du319atWwtdLisrS+np6U4TAAC4vlyzASklJUWSVKtWLafxWrVqOeYVJCEhQYGBgY4pPDy8QvsEAABXH5cGpPj4eNlstiKnffv2VWpPEydOlN1ud0zJycmVun0AAOB6JbqTdnkbP3684uLiiqxp2LBhqdYdFhYmSTp58qRq167tGD958qRat25d6HI+Pj6O35oDAADXJ5cGpJCQEIWEhFTIuhs0aKCwsDCtWbPGEYjS09O1bdu2El0JBwAArj9ucw7SkSNHlJiYqCNHjignJ0eJiYlKTExURkaGoyYqKkrLli2TJNlsNo0dO1YvvPCCVqxYof/+9796+OGHVadOHd1///0uehYAAMAduHQPUklMnjxZCxcudDxu06aNJGndunXq3LmzJCkpKUl2u91R88wzz+js2bN67LHHlJaWpo4dO2rVqlWqWrVqpfYOAADci9vdB6mycR8kAADcD/dBAgAAKGcEJAAAAAsCEgAAgAUBCQAAwIKABAAAYEFAAgAAsCAgAQAAWBCQAAAALAhIAAAAFgQkAAAACwISAACABQEJAADAgoAEAABgQUACAACwICABAABYEJAAAAAsCEgAAAAWBCQAAAALAhIAAIAFAQkAAMCCgAQAAGBBQAIAALAgIAEAAFgQkAAAACwISAAAABYEJAAAAAsCEgAAgAUBCQAAwIKABAAAYEFAAgAAsCAgAQAAWLhNQJo+fbo6dOggPz8/BQUFXbE+Oztbzz77rFq0aKFq1aqpTp06evjhh3X8+PGKbxYAALg1twlIFy5cUN++fTVixIhi1WdmZurbb7/VpEmT9O233+qTTz5RUlKS7rvvvgruFAAAuDubMca4uomSWLBggcaOHau0tLQSL7tjxw7deuut+umnn1SvXr1iLZOenq7AwEDZ7XYFBASUeJsAAKDylfX727MCerpq2e122Wy2Ig/RZWVlKSsry/E4PT29EjoDAABXE7c5xFZW58+f17PPPqsBAwYUmSQTEhIUGBjomMLDwyuxSwAAcDVwaUCKj4+XzWYrctq3b1+Zt5Odna1+/frJGKO5c+cWWTtx4kTZ7XbHlJycXObtAwAA9+LSQ2zjx49XXFxckTUNGzYs0zYuhaOffvpJa9euveJxSB8fH/n4+JRpmwAAwL25NCCFhIQoJCSkwtZ/KRzt379f69atU3BwcIVtCwAAXDvc5hykI0eOKDExUUeOHFFOTo4SExOVmJiojIwMR01UVJSWLVsmKS8c9enTRzt37tTixYuVk5OjlJQUpaSk6MKFC656GgAAwA24zVVskydP1sKFCx2P27RpI0lat26dOnfuLElKSkqS3W6XJB07dkwrVqyQJLVu3dppXb9dBgAAwMrt7oNU2bgPEgAA7qes399uc4gNAACgshCQAAAALAhIAAAAFgQkAAAACwISAACABQEJAADAgoAEAABgQUACAACwICABAABYEJAAAAAsCEgAAAAWBCQAAAALAhIAAIAFAQkAAMCCgAQAAGBBQAIAALAgIAEAAFgQkAAAACwISAAAABYEJAAAAAsCEgAAgAUBCQAAwIKABAAAYEFAAgAAsCAgAQAAWBCQAAAALAhIAAAAFgQkAAAACwISAACABQEJAADAgoAEAABg4TYBafr06erQoYP8/PwUFBRU4uWfeOIJ2Ww2zZ49u9x7AwAA1xa3CUgXLlxQ3759NWLEiBIvu2zZMn3z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\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}