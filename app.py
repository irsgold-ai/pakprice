from flask import Flask,render_template,request,jsonify,send_from_directory
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import config
from core.search_engine import search
from core.cache import setup_database,clear_expired_cache
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
app=Flask(__name__,template_folder=os.path.join(BASE_DIR,'ui/templates'),static_folder=os.path.join(BASE_DIR,'ui/static'))
app.secret_key=os.environ.get('SECRET_KEY','pakprice-secret-2024')
@app.route('/')
def home():
    return render_template('index.html',categories=config.CATEGORIES,sites=config.SITE_INFO,version=config.APP_VERSION,app_name=config.APP_NAME)
    @app.route('/search')
    def search_page():
        query=request.args.get('q','').strip()
            category=request.args.get('cat','all').strip()
                if not query:
                        return render_template('index.html',categories=config.CATEGORIES,sites=config.SITE_INFO,version=config.APP_VERSION,error="Please enter a product name")
                            data=search(query,category)
                                try:
                                        clear_expired_cache()
                                            except:
                                                    pass
                                                        return render_template('results.html',query=query,category=category,category_info=data.get('category_info',{}),results=data.get('results',[]),alternatives=data.get('alternatives',[]),stats=data.get('stats',{}),from_cache=data.get('from_cache',False),total_results=data.get('total_results',0),error=data.get('error'),price_buffer=config.PRICE_RANGE_BUFFER_PERCENT,app_name=config.APP_NAME)
                                                        @app.route('/api/search')
                                                        def api_search():
                                                            query=request.args.get('q','').strip()
                                                                if not query:
                                                                        return jsonify({'error':'Please provide a search query','results':[]}),400
                                                                            return jsonify(search(query,request.args.get('cat','all').strip()))
                                                                            @app.route('/health')
                                                                            def health():
                                                                                return jsonify({'status':'healthy','app':config.APP_NAME,'version':config.APP_VERSION})
                                                                                @app.route('/manifest.json')
                                                                                def manifest():
                                                                                    return send_from_directory('ui/static','manifest.json')
                                                                                    @app.route('/sw.js')
                                                                                    def service_worker():
                                                                                        return send_from_directory('ui/static','sw.js',mimetype='application/javascript')
                                                                                        @app.errorhandler(404)
                                                                                        def not_found(e):
                                                                                            return render_template('index.html',categories=config.CATEGORIES,sites=config.SITE_INFO,version=config.APP_VERSION,error="Page not found."),404
                                                                                            @app.errorhandler(500)
                                                                                            def server_error(e):
                                                                                                return render_template('index.html',categories=config.CATEGORIES,sites=config.SITE_INFO,version=config.APP_VERSION,error="Something went wrong."),500
                                                                                                if __name__=='__main__':
                                                                                                    setup_database()
                                                                                                        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',5000)))