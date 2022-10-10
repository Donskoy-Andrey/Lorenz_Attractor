from scipy.integrate import ode
import matplotlib.pyplot as plt


COLORS = ['r', 'g']


class LorenzAttractor:
    def __init__(self,
                 initial_params: list[float],
                 params: list[float],
                 step: float):
        self.initial_params = initial_params
        self.params = params
        self.step = step

    def __iter__(self):
        return LorenzAttractorIterator(
            self.initial_params,
            self.params,
            self.step
        )


class LorenzAttractorIterator:
    def __init__(self,
                 initial_params: list[float],
                 params: list[float],
                 step: float):
        self.x0, self.y0, self.z0 = initial_params
        self.sigma, self.beta, self.rho = params
        self.step = step

        def func(t, coordinates: list) -> list:
            x_t, y_t, z_t = coordinates
            x_dot = self.sigma * (y_t - x_t)
            y_dot = x_t * (self.rho - z_t) - y_t
            z_dot = x_t * y_t - self.beta * z_t
            return [x_dot, y_dot, z_dot]

        r = ode(func).set_integrator('zvode', method='bdf')
        r.set_initial_value([self.x0, self.y0, self.z0], step)

        self.r = r

    def __next__(self):
        return self.r.integrate(self.r.t + self.step)


def draw(xs: list, ys: list, zs: list, num: int) -> None:
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot(xs, ys, zs, lw=1, c=COLORS[num])
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.savefig(f'images/Lorenz-Attractor-{num}')


def main():
    attractor1 = LorenzAttractor([1, 2, 3],
                                 [10, 8/3, 28],
                                 0.1)
    attractor2 = LorenzAttractor([2, 8, 1],
                                 [10, 8/3, 28],
                                 0.1)

    for num, att in enumerate([attractor1, attractor2]):
        xs, ys, zs = [], [], []
        for i, state in enumerate(att):
            x, y, z = state.real
            xs.append(x)
            ys.append(y)
            zs.append(z)
            if len(xs) > 1000:
                draw(xs, ys, zs, num=num)
                break


if __name__ == '__main__':
    main()



