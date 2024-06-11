from flask import Flask, render_template, jsonify, request, make_response
from random import *
from flask_cors import CORS
import requests,json
import pymysql
from datetime import datetime
import pandas as pd
import mysql.connector
import base64