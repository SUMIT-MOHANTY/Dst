class Store {
    constructor() {
        this.state = { data: [], isLoading: false, error: null };
        this.listeners = [];
    }

    subscribe(listener) {
        this.listeners.push(listener);
    }

    notify() {
        this.listeners.forEach(l => l(this.state));
    }

    setLoading(bool) {
        this.state.isLoading = bool;
        this.notify();
    }

    setData(data) {
        this.state.data = data;
        this.state.error = null;
        this.notify();
    }

    setError(msg) {
        this.state.error = msg;
        this.notify();
    }
}

export const appStore = new Store();
