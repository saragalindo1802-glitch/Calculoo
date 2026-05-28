import numpy as np
import plotly.graph_objects as go

def calcular_volumen(figura, radio, n):

    limite = radio

    dx = (2 * limite) / n

    volumen_elemento = dx**3

    volumen = np.sum(figura) * volumen_elemento

    return volumen


def graficar_figura(X, Y, Z, figura, titulo):

    fig = go.Figure(data=go.Isosurface(

        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),

        value=figura.flatten(),

        isomin=0.5,
        isomax=1.0,

        surface_count=1,

        colorscale='Viridis',

        showscale=False,

        caps=dict(
            x_show=False,
            y_show=False,
            z_show=False
        )
    ))

    fig.update_layout(

        title=titulo,

        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='cube'
        )
    )

    fig.show()
