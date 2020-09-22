import axios from 'axios';
import store from '../store';

export default axios.create({
    baseURL: 'http://127.0.0.1:8000/api/music/',
    headers: {
        'Content-type': 'application/json',
        Authorization : store.state.token,
    },
})