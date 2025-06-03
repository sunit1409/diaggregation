import numpy as np

def disaggregate_ac(mains_power, threshold=1000):
    """Return an estimate of AC power usage from aggregate mains power.

    This simple method assumes that when power consumption rises more than
    `threshold` watts above the baseline, the difference can be attributed
    to the air conditioner (AC). The function subtracts a baseline (median)
    from the mains power and keeps positive differences above the threshold
    as the AC power signal.

    Parameters
    ----------
    mains_power : sequence of float
        Array-like aggregated power readings (e.g., from a smart meter).
    threshold : float, optional
        Power difference in watts to qualify as AC usage. Defaults to 1000.

    Returns
    -------
    numpy.ndarray
        Estimated AC power consumption for each input sample.
    """
    mains_power = np.asarray(mains_power, dtype=float)
    baseline = np.median(mains_power)
    diff = mains_power - baseline
    ac_power = np.where(diff >= threshold, diff, 0.0)
    return ac_power
