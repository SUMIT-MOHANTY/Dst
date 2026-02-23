from flask import jsonify, request
from app import db
from app.models import Profile, Skill, Project

def register_routes(app):
    @app.route('/api/profile', methods=['GET'])
    def get_profile():
        profile = Profile.query.first()
        if not profile:
            return jsonify({'error': 'Profile not found'}), 404
        return jsonify({'id': profile.id, 'name': profile.name, 'title': profile.title, 'bio': profile.bio, 'email': profile.email})

    @app.route('/api/profile', methods=['POST'])
    def create_profile():
        data = request.get_json()
        profile = Profile(name=data.get('name'), title=data.get('title'), bio=data.get('bio'), email=data.get('email'))
        db.session.add(profile)
        db.session.commit()
        return jsonify({'message': 'Profile created', 'id': profile.id}), 201

    @app.route('/api/skills', methods=['GET'])
    def get_skills():
        skills = Skill.query.all()
        return jsonify([{'id': s.id, 'name': s.name, 'level': s.level} for s in skills])

    @app.route('/api/skills', methods=['POST'])
    def create_skill():
        data = request.get_json()
        skill = Skill(name=data.get('name'), level=data.get('level'), profile_id=data.get('profile_id'))
        db.session.add(skill)
        db.session.commit()
        return jsonify({'message': 'Skill created'}), 201

    @app.route('/api/projects', methods=['GET'])
    def get_projects():
        projects = Project.query.all()
        return jsonify([{'id': p.id, 'title': p.title, 'description': p.description, 'technologies': p.technologies, 'link': p.link} for p in projects])

    @app.route('/api/projects', methods=['POST'])
    def create_project():
        data = request.get_json()
        project = Project(title=data.get('title'), description=data.get('description'), technologies=data.get('technologies'), link=data.get('link'), profile_id=data.get('profile_id'))
        db.session.add(project)
        db.session.commit()
        return jsonify({'message': 'Project created'}), 201

    @app.route('/api/ai/generate', methods=['POST'])
    def ai_generate():
        data = request.get_json()
        prompt = data.get('prompt')
        return jsonify({'suggestion': f'AI generated content for: {prompt}'})
