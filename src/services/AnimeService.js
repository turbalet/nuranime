import axiosInstance from '../axios';
import axios from 'axios';


const BASE_URL = 'http://localhost:8000/api/v1/animes';

 class AnimeService {


    getAnimes() {
        return axiosInstance.get(BASE_URL);
    }


} 
export default new AnimeService;