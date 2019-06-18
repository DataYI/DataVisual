import pandas as pd
from flask import Flask, render_template


def get_df():
    df = pd.read_excel('data.xlsx')

    def get_animal(year):
        animals = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
        ix = (year - 1900) % 12
        return animals[ix]

    df['生肖'] = df['年份'].map(get_animal)
    df['年份'] = df['年份'].astype(str)
    return df


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# 修改jinja变量定界符
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

df = get_df()


@app.route('/chart/')
def chart():
    records1 = df[['年份', '出生人口数']].to_json(orient='records', force_ascii=False)
    records2 = df[['生肖', '出生人口数']].to_json(orient='records', force_ascii=False)
    return render_template('web.html', records1=eval(records1), records2=eval(records2))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
