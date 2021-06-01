import axiosInstance from '../axios';
import axios from 'axios';


const BASE_URL = 'http://localhost:8000/api/v1/animes';

 class AnimeService {

    


    getTop() {
        return axiosInstance.get(BASE_URL + "/top");
    }

    getAnimes() {
        return axiosInstance.get(BASE_URL);
    }

    getOngoings() {
        return axiosInstance.get(BASE_URL + "/?status=Онгоинг")
    }

    getAnonses() {
        return axiosInstance.get(BASE_URL + "/?status=Анонс")
    }

} 
export default new AnimeService();