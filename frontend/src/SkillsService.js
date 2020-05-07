import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class SkillsService {
    constructor() {}

    getSkills() {
        const url = `${API_URL}/api/skills/`;
        return axios.get(url).then(response => response.data);
    }

    getSkillByURL(link) {
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }

    getSkill(slug) {
        const url = `${API_URL}/api/skill/${slug}`;
        return axios.get(url).then(response => response.data);
    }

    deleteSkill(skill){
        const url = `${API_URL}/api/skill/${skill.slug}`;
        return axios.delete(url);
    }

    createSkill(skill){
        const url = `${API_URL}/api/skills/`;
        return axios.post(url,skill);
    }

    updateSkill(skill){
        const url = `${API_URL}/api/skill/${skill.slug}`;
        return axios.put(url,skill);
    }
}