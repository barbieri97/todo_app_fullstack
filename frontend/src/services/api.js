import axios from 'axios';

axios.defaults.headers.post['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;

const api = axios.create({
    baseURL: 'http://localhost:8000',
});


export default api