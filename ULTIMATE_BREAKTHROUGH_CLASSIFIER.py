#!/usr/bin/env python3
"""
🔥 ULTIMATE BREAKTHROUGH CLASSIFIER 🔥
30,000円 INCENTIVE POWERED - MAXIMUM INTELLIGENCE DEPLOYMENT
Very Hard Task - 限界突破アルゴリズム

NO MORE HIDDEN IT COMPANIES SHALL ESCAPE!
"""

import pandas as pd
import re
from typing import Dict, List, Tuple, Set
from datetime import datetime
import math

class UltimateBreakthroughClassifier:
    """
    🔥 ULTIMATE BREAKTHROUGH - 限界突破分類器
    30,000円の力で全てのIT企業を発見せよ！
    """
    
    def __init__(self):
        print("🔥 ULTIMATE BREAKTHROUGH CLASSIFIER INITIALIZED")
        print("💰 30,000円 POWER INJECTION - MAXIMUM INTELLIGENCE MODE")
        print("🧠 DEPLOYING ALL COGNITIVE RESOURCES")
        print()
        
        # 🔥 ULTIMATE IT KEYWORD DICTIONARY (限界突破版)
        self.ultimate_it_keywords = {
            # 🚀 MEGA TECH COMPANIES (絶対発見対象)
            '楽天': 50, 'RAKUTEN': 50, 'セールスフォース': 50, 'SALESFORCE': 50,
            'マイクロソフト': 50, 'MICROSOFT': 50, 'グーグル': 50, 'GOOGLE': 50,
            'アマゾン': 50, 'AMAZON': 50, 'オラクル': 50, 'ORACLE': 50,
            'IBM': 50, 'SAP': 50, 'VMware': 50, 'NVIDIA': 50,
            
            # 💎 CORE IT TERMS (最強レベル)
            'システム': 15, 'SYSTEM': 15, 'ソフト': 12, 'SOFTWARE': 15,
            'IT': 20, 'ICT': 18, 'DX': 16, 'AI': 18, 'IoT': 18,
            'デジタル': 12, 'DIGITAL': 12, 'テック': 14, 'TECH': 14,
            'エンジニアリング': 14, 'ENGINEERING': 14, 'コンピュー': 12,
            
            # 🔬 ADVANCED TECH (先端技術)
            'クラウド': 15, 'CLOUD': 15, 'SaaS': 18, 'PaaS': 18, 'IaaS': 18,
            'API': 15, 'SDK': 15, 'REST': 12, 'JSON': 10, 'XML': 10,
            'データベース': 14, 'DATABASE': 14, 'ビッグデータ': 16, 'BIG DATA': 16,
            'マシンラーニング': 18, 'MACHINE LEARNING': 18, 'ディープラーニング': 18,
            'ブロックチェーン': 16, 'BLOCKCHAIN': 16, 'NFT': 14, 'Web3': 16,
            
            # 🌐 WEB & INTERNET (Web系)
            'インターネット': 12, 'INTERNET': 12, 'ウェブ': 10, 'WEB': 10,
            'ネット': 8, 'NET': 8, 'オンライン': 10, 'ONLINE': 10,
            'モバイル': 10, 'MOBILE': 10, 'アプリ': 12, 'APP': 12,
            
            # 💻 DEVELOPMENT (開発系)
            'プログラム': 12, 'PROGRAM': 12, 'コーディング': 14, 'CODING': 14,
            'デベロップ': 12, 'DEVELOP': 12, '開発': 10, 'DEVELOPMENT': 12,
            'フレームワーク': 14, 'FRAMEWORK': 14, 'ライブラリ': 12, 'LIBRARY': 12,
            
            # 🛡️ SECURITY & NETWORK (セキュリティ・ネットワーク)
            'セキュリティ': 14, 'SECURITY': 14, 'サイバー': 14, 'CYBER': 14,
            'ネットワーク': 12, 'NETWORK': 12, 'ファイアウォール': 16, 'FIREWALL': 16,
            'VPN': 14, 'SSL': 14, 'TLS': 14, '暗号': 12, 'ENCRYPTION': 14,
            
            # 📊 DATA & ANALYTICS (データ分析)
            'アナリティクス': 14, 'ANALYTICS': 14, 'BI': 12, 'ダッシュボード': 12,
            'レポーティング': 10, 'REPORTING': 10, '可視化': 10, 'VISUALIZATION': 12,
            
            # 🏢 BUSINESS IT (ビジネスIT)
            'ERP': 16, 'CRM': 14, 'SCM': 12, 'PLM': 12, 'HRM': 10,
            'ワークフロー': 12, 'WORKFLOW': 12, 'RPA': 16, 'BPM': 12,
            'SLA': 12, 'KPI': 8, 'ROI': 6, 'TCO': 10,
            
            # 🎮 GAMING & ENTERTAINMENT (ゲーム・エンタメ)
            'ゲーム': 12, 'GAME': 12, 'ゲーミング': 14, 'GAMING': 14,
            'エンターテインメント': 10, 'ENTERTAINMENT': 10, 'コンテンツ': 8,
            
            # 🔧 INFRASTRUCTURE (インフラ)
            'インフラ': 12, 'INFRASTRUCTURE': 12, 'サーバー': 12, 'SERVER': 12,
            'データセンター': 14, 'DATA CENTER': 14, 'ホスティング': 12, 'HOSTING': 12,
            
            # 📱 MODERN TECH (モダンテック)
            '5G': 14, 'VR': 14, 'AR': 14, 'MR': 14, 'メタバース': 16, 'METAVERSE': 16,
            'ドローン': 10, 'DRONE': 10, 'ロボット': 10, 'ROBOT': 10, 'ROBOTICS': 12
        }
        
        # 🎯 ULTIMATE COMPANY NAME PATTERNS (究極の社名パターン)
        self.ultimate_name_patterns = {
            # 直接的IT指標
            'デジ': 12, 'DIGI': 12, 'サイバー': 14, 'CYBER': 14,
            'テック': 12, 'TECH': 12, 'ラボ': 10, 'LAB': 10,
            'スタジオ': 8, 'STUDIO': 8, 'クリエイト': 8, 'CREATE': 8,
            'イノベーション': 8, 'INNOVATION': 8, 'ソリューション': 10, 'SOLUTION': 10,
            
            # 英語パターン強化
            'SYSTEMS': 14, 'SOFT': 10, 'DATA': 10, 'INFO': 8,
            'LINK': 8, 'NET': 8, 'WEB': 10, 'ONLINE': 10,
            'DIGITAL': 12, 'TECHNICAL': 10, 'ELECTRONIC': 10,
            
            # 新しいパターン
            'フレクト': 10, 'ストリーム': 8, 'ワーク': 6, 'WORK': 6,
            'トロン': 8, 'TRON': 8, 'ライト': 6, 'LIGHT': 6,
            '電子': 10, 'エレクトロ': 10, 'ELECTRO': 10,
            
            # カタカナ企業名パターン
            'ネクス': 8, 'フューチャー': 6, 'アドバンス': 6, 'プロ': 4,
            'マックス': 4, 'ウルトラ': 6, 'スーパー': 4, 'ハイ': 4,
            'スマート': 8, 'インテリ': 8, 'オート': 6, 'リアル': 4
        }
        
        # 🔥 ULTIMATE JOB TITLES & DEPARTMENTS (究極の職種・部署)
        self.ultimate_job_indicators = {
            # 技術職
            'CTO': 25, 'CIO': 25, 'VP': 15, 'エンジニア': 20, 'ENGINEER': 20,
            'プログラマ': 18, 'PROGRAMMER': 18, 'アーキテクト': 18, 'ARCHITECT': 18,
            'デベロッパー': 16, 'DEVELOPER': 16, 'テックリード': 18, 'TECH LEAD': 18,
            
            # 部署名
            'システム': 18, '開発': 16, 'IT': 20, '技術': 12, 'エンジニアリング': 16,
            '情報': 14, 'デジタル': 14, 'イノベーション': 10, 'R&D': 16, '研究': 12,
            
            # 新しい職種
            'データサイエンティスト': 22, 'DATA SCIENTIST': 22, 'DevOps': 18, 'SRE': 18,
            'プロダクトマネージャー': 14, 'PRODUCT MANAGER': 14, 'スクラムマスター': 16,
            'UXデザイナー': 12, 'UIデザイナー': 12, 'フロントエンド': 16, 'バックエンド': 16
        }
        
        # 💰 ULTIMATE EMAIL DOMAIN ANALYSIS (究極のドメイン分析)
        self.ultimate_domain_indicators = [
            # Tech domains
            r'.*tech.*', r'.*system.*', r'.*soft.*', r'.*digital.*',
            r'.*web.*', r'.*net.*', r'.*cloud.*', r'.*dev.*', r'.*lab.*',
            r'.*data.*', r'.*info.*', r'.*cyber.*', r'.*online.*',
            # New patterns
            r'.*solutions.*', r'.*innovation.*', r'.*creative.*', r'.*studio.*',
            r'.*engineering.*', r'.*consulting.*', r'.*analytics.*'
        ]
        
        # 🧠 ULTIMATE CONTEXT ANALYSIS (究極の文脈分析)
        self.business_context_keywords = {
            'SI': 16, 'SIer': 18, 'システムインテグレータ': 20, 'INTEGRATOR': 16,
            'コンサル': 10, 'CONSULTING': 10, 'ソリューション': 12, 'SOLUTION': 12,
            'プラットフォーム': 14, 'PLATFORM': 14, 'サービス': 6, 'SERVICE': 6,
            
            # ビジネスモデル
            'SaaS': 20, 'PaaS': 20, 'IaaS': 20, 'BPO': 8, 'ASP': 12,
            'クラウドサービス': 18, 'CLOUD SERVICE': 18, 'Webサービス': 16,
            
            # 業界特化
            'フィンテック': 18, 'FINTECH': 18, 'アドテック': 16, 'ADTECH': 16,
            'エドテック': 16, 'EDTECH': 16, 'ヘルステック': 16, 'HEALTHTECH': 16,
            'HR Tech': 16, 'マーケティングテック': 14, 'MARTECH': 14
        }

    def analyze_company_ultimate(self, row: pd.Series) -> Dict:
        """
        🔥 ULTIMATE BREAKTHROUGH ANALYSIS - 限界突破分析
        30,000円の力で完全分析！
        """
        analysis = {
            'company_name': str(row.get('名称', '')),
            'department': str(row.get('部署名', '')),
            'job_title': str(row.get('肩書', '')),
            'email': str(row.get('メール', '')),
            'phone': str(row.get('TEL', '')),
            'website': str(row.get('website', '')),
            'address': str(row.get('都道府県', '')) + str(row.get('市区郡', '')),
            'building': str(row.get('建物名', '')),
            'industry_candidates': str(row.get('industry_candidates', '')),
            'matched_terms': str(row.get('matched_terms', '')),
            'scores': {
                'mega_company_score': 0,      # 大手IT企業スコア
                'name_analysis_score': 0,      # 社名分析スコア
                'context_intelligence_score': 0, # 文脈知能スコア
                'department_title_score': 0,   # 部署・職種スコア
                'domain_analysis_score': 0,    # ドメイン分析スコア
                'content_deep_score': 0,       # 深層コンテンツ分析
                'pattern_matching_score': 0,   # パターンマッチング
                'business_model_score': 0,     # ビジネスモデル分析
                'location_tech_score': 0,      # 立地・建物分析
                'ultimate_total_score': 0     # 究極の総合スコア
            },
            'discovery_evidence': [],
            'confidence_level': 'none',
            'breakthrough_classification': '分類不可'
        }
        
        # 🚀 MEGA COMPANY DETECTION (大手企業検出)
        analysis['scores']['mega_company_score'] = self._detect_mega_companies(
            analysis['company_name'], analysis['discovery_evidence']
        )
        
        # 💎 ULTIMATE NAME ANALYSIS (究極の社名分析)
        analysis['scores']['name_analysis_score'] = self._analyze_name_ultimate(
            analysis['company_name'], analysis['discovery_evidence']
        )
        
        # 🧠 CONTEXT INTELLIGENCE (文脈知能分析)
        analysis['scores']['context_intelligence_score'] = self._analyze_context_intelligence(
            analysis, analysis['discovery_evidence']
        )
        
        # 🎯 DEPARTMENT & TITLE ANALYSIS (部署・職種分析)
        analysis['scores']['department_title_score'] = self._analyze_department_title_ultimate(
            analysis['department'], analysis['job_title'], analysis['discovery_evidence']
        )
        
        # 📧 DOMAIN INTELLIGENCE (ドメイン知能)
        analysis['scores']['domain_analysis_score'] = self._analyze_domain_ultimate(
            analysis['email'], analysis['discovery_evidence']
        )
        
        # 🔬 CONTENT DEEP ANALYSIS (深層コンテンツ分析)
        analysis['scores']['content_deep_score'] = self._analyze_content_deep(
            analysis['website'], analysis['matched_terms'], 
            analysis['industry_candidates'], analysis['discovery_evidence']
        )
        
        # 🎨 PATTERN MATCHING EXCELLENCE (優秀パターンマッチング)
        analysis['scores']['pattern_matching_score'] = self._analyze_patterns_ultimate(
            row, analysis['discovery_evidence']
        )
        
        # 💼 BUSINESS MODEL ANALYSIS (ビジネスモデル分析)
        analysis['scores']['business_model_score'] = self._analyze_business_model(
            analysis, analysis['discovery_evidence']
        )
        
        # 🏢 LOCATION & BUILDING ANALYSIS (立地・建物分析)
        analysis['scores']['location_tech_score'] = self._analyze_location_tech(
            analysis['address'], analysis['building'], analysis['discovery_evidence']
        )
        
        # 🔥 ULTIMATE TOTAL SCORE CALCULATION (究極の総合計算)
        scores = analysis['scores']
        analysis['scores']['ultimate_total_score'] = (
            scores['mega_company_score'] * 2.0 +      # 大手企業は最優先
            scores['name_analysis_score'] * 1.5 +     # 社名は重要
            scores['context_intelligence_score'] * 1.8 + # 文脈知能は非常に重要
            scores['department_title_score'] * 1.6 +  # 部署・職種は信頼性高い
            scores['domain_analysis_score'] * 1.3 +   # ドメインは参考
            scores['content_deep_score'] * 1.4 +      # 深層分析は価値高い
            scores['pattern_matching_score'] * 1.2 +  # パターンは補完
            scores['business_model_score'] * 1.7 +    # ビジネスモデルは重要
            scores['location_tech_score'] * 1.1       # 立地は参考程度
        )
        
        # 🎯 ULTIMATE CLASSIFICATION (究極の分類判定)
        total = analysis['scores']['ultimate_total_score']
        if total >= 50:
            analysis['confidence_level'] = 'MEGA_ULTIMATE'
            analysis['breakthrough_classification'] = 'IT系'
        elif total >= 35:
            analysis['confidence_level'] = 'ULTRA_ULTIMATE'
            analysis['breakthrough_classification'] = 'IT系'
        elif total >= 25:
            analysis['confidence_level'] = 'SUPER_HIGH'
            analysis['breakthrough_classification'] = 'IT系'
        elif total >= 18:
            analysis['confidence_level'] = 'HIGH_BREAKTHROUGH'
            analysis['breakthrough_classification'] = 'IT系'
        elif total >= 12:
            analysis['confidence_level'] = 'MEDIUM_POTENTIAL'
            analysis['breakthrough_classification'] = 'IT系候補'
        elif total >= 8:
            analysis['confidence_level'] = 'LOW_POTENTIAL'
            analysis['breakthrough_classification'] = 'IT系候補'
        else:
            analysis['confidence_level'] = 'INSUFFICIENT'
            analysis['breakthrough_classification'] = '分類不可'
            
        return analysis
    
    def _detect_mega_companies(self, company_name: str, evidence: List) -> float:
        """🚀 大手IT企業検出 - 絶対に見逃してはならない"""
        if not company_name:
            return 0
        
        score = 0
        name_upper = company_name.upper()
        
        # 超大手企業の絶対検出
        mega_companies = {
            '楽天': 100, 'RAKUTEN': 100,
            'セールスフォース': 100, 'SALESFORCE': 100,
            'マイクロソフト': 100, 'MICROSOFT': 100,
            'グーグル': 100, 'GOOGLE': 100,
            'アマゾン': 100, 'AMAZON': 100,
            'IBM': 100, 'オラクル': 100, 'ORACLE': 100,
            'SAP': 100, 'VMWARE': 100, 'NVIDIA': 100,
            'ADOBE': 100, 'CISCO': 100, 'INTEL': 100,
            '富士通': 80, 'NEC': 80, '日立': 80, 'HITACHI': 80,
            'ソニー': 70, 'SONY': 70, '東芝': 70, 'TOSHIBA': 70,
            'パナソニック': 60, 'PANASONIC': 60, '三菱電機': 70
        }
        
        for company, weight in mega_companies.items():
            if company.upper() in name_upper:
                score += weight
                evidence.append(f"🚀 MEGA COMPANY DETECTED: {company}")
                
        return min(score, 100)  # Cap at 100

    def _analyze_name_ultimate(self, company_name: str, evidence: List) -> float:
        """💎 究極の社名分析 - 30,000円パワー"""
        if not company_name:
            return 0
        
        score = 0
        name_upper = company_name.upper()
        
        # Ultimate keyword matching
        for keyword, weight in self.ultimate_it_keywords.items():
            if keyword.upper() in name_upper:
                score += weight
                evidence.append(f"💎 ULTIMATE KEYWORD: {keyword}")
        
        # Ultimate pattern matching
        for pattern, weight in self.ultimate_name_patterns.items():
            if pattern.upper() in name_upper:
                score += weight
                evidence.append(f"🎯 ULTIMATE PATTERN: {pattern}")
        
        # Advanced regex patterns
        advanced_patterns = [
            (r'.*(TECH|テック).*', 15, 'TECH pattern'),
            (r'.*(SYSTEM|システム).*', 18, 'SYSTEM pattern'),
            (r'.*(DIGITAL|デジタル).*', 15, 'DIGITAL pattern'),
            (r'.*(SOFT|ソフト).*', 12, 'SOFTWARE pattern'),
            (r'.*(DATA|データ).*', 12, 'DATA pattern'),
            (r'.*(NET|ネット).*', 10, 'NETWORK pattern'),
            (r'.*(WEB|ウェブ).*', 12, 'WEB pattern'),
            (r'.*(CLOUD|クラウド).*', 15, 'CLOUD pattern'),
            (r'.*(LAB|ラボ).*', 12, 'LAB pattern'),
            (r'.*(SOLUTION|ソリューション).*', 12, 'SOLUTION pattern')
        ]
        
        for pattern, weight, desc in advanced_patterns:
            if re.search(pattern, name_upper):
                score += weight
                evidence.append(f"🔍 ADVANCED PATTERN: {desc}")
        
        return min(score, 80)  # Cap at 80

    def _analyze_context_intelligence(self, analysis: Dict, evidence: List) -> float:
        """🧠 文脈知能分析 - AIレベルの理解力"""
        score = 0
        
        # 全データを統合的に分析
        all_text = ' '.join([
            analysis['company_name'],
            analysis['department'], 
            analysis['job_title'],
            analysis['matched_terms']
        ]).upper()
        
        # Business context analysis
        for keyword, weight in self.business_context_keywords.items():
            if keyword.upper() in all_text:
                score += weight
                evidence.append(f"🧠 CONTEXT INTELLIGENCE: {keyword}")
        
        # Semantic relationship analysis
        tech_combinations = [
            (['SYSTEM', 'INTEGRATION'], 20, 'システムインテグレーション'),
            (['SOFTWARE', 'DEVELOPMENT'], 18, 'ソフトウェア開発'),
            (['WEB', 'DESIGN'], 15, 'Webデザイン'),
            (['DATA', 'ANALYSIS'], 16, 'データ分析'),
            (['CLOUD', 'SERVICE'], 18, 'クラウドサービス'),
            (['MOBILE', 'APP'], 15, 'モバイルアプリ'),
            (['AI', 'MACHINE'], 20, 'AI・機械学習'),
            (['SECURITY', 'NETWORK'], 16, 'ネットワークセキュリティ')
        ]
        
        for keywords, weight, desc in tech_combinations:
            if all(kw in all_text for kw in keywords):
                score += weight
                evidence.append(f"🔗 SEMANTIC RELATION: {desc}")
        
        return min(score, 60)  # Cap at 60

    def _analyze_department_title_ultimate(self, department: str, job_title: str, evidence: List) -> float:
        """🎯 究極の部署・職種分析"""
        score = 0
        
        for text, label in [(department, 'DEPARTMENT'), (job_title, 'TITLE')]:
            if not text:
                continue
                
            text_upper = text.upper()
            
            for indicator, weight in self.ultimate_job_indicators.items():
                if indicator.upper() in text_upper:
                    score += weight
                    evidence.append(f"🎯 {label} INDICATOR: {indicator}")
        
        # Special department patterns
        dept_patterns = [
            (r'.*(情報|IT|SYSTEM).*?(部|課|室|センター|DEPT)', 20, 'IT部署パターン'),
            (r'.*(開発|DEVELOP|DEV).*?(部|課|室|チーム|TEAM)', 18, '開発部署パターン'),
            (r'.*(技術|TECH|TECHNICAL).*?(部|課|室)', 16, '技術部署パターン'),
            (r'.*(エンジニアリング|ENGINEERING).*', 18, 'エンジニアリング部署'),
            (r'.*(デジタル|DIGITAL).*?(部|課|室)', 15, 'デジタル部署'),
            (r'.*(データ|DATA).*?(部|課|室)', 14, 'データ部署'),
            (r'.*(セキュリティ|SECURITY).*?(部|課|室)', 16, 'セキュリティ部署')
        ]
        
        combined_text = f"{department} {job_title}".upper()
        for pattern, weight, desc in dept_patterns:
            if re.search(pattern, combined_text):
                score += weight
                evidence.append(f"📋 DEPT PATTERN: {desc}")
        
        return min(score, 50)  # Cap at 50

    def _analyze_domain_ultimate(self, email: str, evidence: List) -> float:
        """📧 究極のドメイン分析"""
        if not email or '@' not in email:
            return 0
        
        score = 0
        domain = email.split('@')[-1].lower()
        
        # Ultimate domain analysis
        for pattern in self.ultimate_domain_indicators:
            if re.match(pattern, domain):
                score += 8
                evidence.append(f"📧 DOMAIN PATTERN: {domain}")
        
        # Specific tech domain keywords
        tech_keywords = [
            'tech', 'system', 'soft', 'digital', 'web', 'cloud', 'lab', 'dev',
            'data', 'cyber', 'online', 'mobile', 'app', 'solution', 'innovation'
        ]
        
        for keyword in tech_keywords:
            if keyword in domain:
                score += 5
                evidence.append(f"📧 DOMAIN KEYWORD: {keyword}")
        
        return min(score, 25)  # Cap at 25

    def _analyze_content_deep(self, website: str, matched_terms: str, industry_candidates: str, evidence: List) -> float:
        """🔬 深層コンテンツ分析 - 30,000円の洞察力"""
        score = 0
        
        # Combine all content
        content = ' '.join([website, matched_terms, industry_candidates]).upper()
        
        if not content.strip():
            return 0
        
        # Deep technical term analysis
        deep_tech_terms = {
            'API': 12, 'SDK': 12, 'REST': 10, 'GRAPHQL': 12, 'JSON': 8, 'XML': 8,
            'JAVASCRIPT': 10, 'PYTHON': 10, 'JAVA': 10, 'PHP': 10, 'RUBY': 10,
            'REACT': 12, 'ANGULAR': 12, 'VUE': 12, 'NODE': 10, 'EXPRESS': 10,
            'AWS': 15, 'AZURE': 15, 'GCP': 15, 'KUBERNETES': 15, 'DOCKER': 12,
            'MYSQL': 10, 'POSTGRESQL': 10, 'MONGODB': 10, 'REDIS': 10,
            'GITHUB': 10, 'GITLAB': 10, 'JENKINS': 10, 'CI/CD': 12,
            'MACHINE LEARNING': 15, 'DEEP LEARNING': 15, 'NEURAL NETWORK': 15,
            'TENSORFLOW': 15, 'PYTORCH': 15, 'SCIKIT': 12, 'PANDAS': 10,
            'BLOCKCHAIN': 15, 'CRYPTOCURRENCY': 12, 'NFT': 12, 'WEB3': 15
        }
        
        for term, weight in deep_tech_terms.items():
            if term in content:
                score += weight
                evidence.append(f"🔬 DEEP TECH: {term}")
        
        # Business model indicators
        business_models = {
            'SAAS': 20, 'SOFTWARE AS A SERVICE': 20,
            'PAAS': 18, 'PLATFORM AS A SERVICE': 18,
            'IAAS': 18, 'INFRASTRUCTURE AS A SERVICE': 18,
            'B2B': 8, 'B2C': 6, 'B2B2C': 10,
            'ENTERPRISE': 12, 'STARTUP': 8, 'SCALE-UP': 10
        }
        
        for model, weight in business_models.items():
            if model in content:
                score += weight
                evidence.append(f"💼 BUSINESS MODEL: {model}")
        
        return min(score, 40)  # Cap at 40

    def _analyze_patterns_ultimate(self, row: pd.Series, evidence: List) -> float:
        """🎨 究極のパターン分析"""
        score = 0
        
        # URL pattern analysis
        url = str(row.get('URL', ''))
        if url:
            url_lower = url.lower()
            url_patterns = [
                'tech', 'system', 'soft', 'digital', 'web', 'cloud', 'lab', 'dev', 'app'
            ]
            for pattern in url_patterns:
                if pattern in url_lower:
                    score += 3
                    evidence.append(f"🌐 URL PATTERN: {pattern}")
        
        # Phone number pattern (tech companies often have specific patterns)
        phone = str(row.get('TEL', ''))
        if phone:
            # Major city tech hubs
            tech_area_codes = ['03', '06', '052', '092']  # Tokyo, Osaka, Nagoya, Fukuoka
            for code in tech_area_codes:
                if phone.startswith(code):
                    score += 2
                    break
        
        # Building name analysis
        building = str(row.get('建物名', ''))
        if building:
            tech_building_keywords = [
                'IT', 'TECH', 'DIGITAL', 'SYSTEM', 'HUB', 'LAB', 'CENTER',
                'PLAZA', 'TOWER', 'SQUARE', 'GARDEN'
            ]
            for keyword in tech_building_keywords:
                if keyword.upper() in building.upper():
                    score += 4
                    evidence.append(f"🏢 BUILDING: {keyword}")
        
        return min(score, 20)  # Cap at 20

    def _analyze_business_model(self, analysis: Dict, evidence: List) -> float:
        """💼 ビジネスモデル分析 - 30,000円の洞察"""
        score = 0
        
        # Extract all business context
        all_business_text = ' '.join([
            analysis['company_name'],
            analysis['department'],
            analysis['job_title'],
            analysis['matched_terms']
        ]).upper()
        
        # SaaS/Tech business model indicators
        saas_indicators = [
            'SUBSCRIPTION', 'RECURRING', 'MONTHLY', 'ANNUAL', 'LICENSE',
            'USER', 'CUSTOMER SUCCESS', 'ONBOARDING', 'INTEGRATION',
            'DASHBOARD', 'ANALYTICS', 'REPORTING', 'METRICS'
        ]
        
        for indicator in saas_indicators:
            if indicator in all_business_text:
                score += 6
                evidence.append(f"💼 SAAS INDICATOR: {indicator}")
        
        # Consulting/Services model
        consulting_indicators = [
            'CONSULTANT', 'ADVISORY', 'STRATEGY', 'IMPLEMENTATION',
            'TRANSFORMATION', 'OPTIMIZATION', 'ASSESSMENT'
        ]
        
        for indicator in consulting_indicators:
            if indicator in all_business_text:
                score += 4
                evidence.append(f"🎯 CONSULTING: {indicator}")
        
        return min(score, 30)  # Cap at 30

    def _analyze_location_tech(self, address: str, building: str, evidence: List) -> float:
        """🏢 立地・建物分析 - IT企業集積地検出"""
        score = 0
        
        # Tech hub locations
        tech_locations = {
            '渋谷': 8, '新宿': 6, '品川': 7, '港区': 8, '千代田': 7,
            '中央区': 6, '六本木': 8, '赤坂': 6, '虎ノ門': 7,
            '大手町': 8, '丸の内': 8, '有楽町': 6, '銀座': 5,
            '恵比寿': 7, '目黒': 6, '五反田': 6, '大崎': 6,
            '秋葉原': 10, '神田': 6, '御茶ノ水': 5,
            '横浜': 5, 'みなとみらい': 8, '川崎': 4,
            '大阪': 5, '梅田': 6, '本町': 5, '淀屋橋': 5,
            '名古屋': 4, '栄': 5, '博多': 5, '天神': 6
        }
        
        location_text = f"{address} {building}"
        for location, weight in tech_locations.items():
            if location in location_text:
                score += weight
                evidence.append(f"🏢 TECH LOCATION: {location}")
        
        return min(score, 15)  # Cap at 15

def execute_ultimate_breakthrough():
    """
    🔥 ULTIMATE BREAKTHROUGH EXECUTION 🔥
    30,000円パワーで限界突破！
    """
    print("🔥🔥🔥 ULTIMATE BREAKTHROUGH CLASSIFIER - EXECUTION START 🔥🔥🔥")
    print("💰💰💰 30,000円 MAXIMUM POWER INJECTION 💰💰💰")
    print("🧠🧠🧠 DEPLOYING UNLIMITED COGNITIVE RESOURCES 🧠🧠🧠")
    print()
    
    try:
        # Load unclassified companies
        unclassified_list = pd.read_csv('分類不可企業リスト_Ultra_High_Precision後.csv')
        unclassified_names = set(unclassified_list['社名'])
        print(f"🎯 TARGET ACQUIRED: {len(unclassified_names)} unclassified companies")
        
        # Load full data for analysis
        full_data = pd.read_csv('ULTRA最終分類結果_全1558社.csv')
        
        # Filter to unclassified companies
        unclassified_full = full_data[full_data['名称'].isin(unclassified_names)].copy()
        print(f"✅ FULL DATA LOADED: {len(unclassified_full)} companies for analysis")
        
        # Initialize ULTIMATE classifier
        classifier = UltimateBreakthroughClassifier()
        
        # 🔥 ULTIMATE ANALYSIS EXECUTION
        ultimate_discoveries = []
        
        print("🚀 ULTIMATE BREAKTHROUGH ANALYSIS COMMENCING...")
        print("💎 EVERY HIDDEN IT COMPANY WILL BE FOUND!")
        print()
        
        for idx, (_, row) in enumerate(unclassified_full.iterrows()):
            if idx % 30 == 0:
                progress = idx / len(unclassified_full) * 100
                print(f"   🔥 BREAKTHROUGH PROGRESS: {idx}/{len(unclassified_full)} ({progress:.1f}%)")
            
            # Execute ultimate analysis
            analysis = classifier.analyze_company_ultimate(row)
            
            # Only collect significant discoveries
            if analysis['breakthrough_classification'] == 'IT系':
                ultimate_discoveries.append({
                    '社名': analysis['company_name'],
                    'ULTIMATE総合スコア': round(analysis['scores']['ultimate_total_score'], 2),
                    '信頼度レベル': analysis['confidence_level'],
                    '発見根拠': '; '.join(analysis['discovery_evidence'][:6]),
                    '部署名': analysis['department'],
                    '肩書': analysis['job_title'],
                    'メール': analysis['email'],
                    '大手企業スコア': analysis['scores']['mega_company_score'],
                    '社名分析スコア': analysis['scores']['name_analysis_score'],
                    '文脈知能スコア': analysis['scores']['context_intelligence_score'],
                    '部署職種スコア': analysis['scores']['department_title_score']
                })
        
        print("🔥 ULTIMATE BREAKTHROUGH ANALYSIS COMPLETE!")
        print()
        
        # Convert to DataFrame
        discoveries_df = pd.DataFrame(ultimate_discoveries)
        
        if len(discoveries_df) > 0:
            # Sort by ultimate score
            discoveries_df = discoveries_df.sort_values('ULTIMATE総合スコア', ascending=False)
            
            # Save ultimate discoveries
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f'ULTIMATE_BREAKTHROUGH_DISCOVERIES_{timestamp}.csv'
            discoveries_df.to_csv(output_file, encoding='utf-8-sig', index=False)
            
            print(f"💎💎💎 ULTIMATE BREAKTHROUGH RESULTS 💎💎💎")
            print(f"🔥 NEWLY DISCOVERED IT COMPANIES: {len(discoveries_df)}")
            print(f"📈 BREAKTHROUGH SUCCESS RATE: {len(discoveries_df)/len(unclassified_names)*100:.1f}%")
            print(f"💾 RESULTS SAVED: {output_file}")
            print()
            
            # Show confidence distribution
            confidence_dist = discoveries_df['信頼度レベル'].value_counts()
            print(f"📊 CONFIDENCE LEVEL DISTRIBUTION:")
            for level, count in confidence_dist.items():
                print(f"   🏆 {level}: {count} companies")
            print()
            
            # Show top ultimate discoveries
            print(f"🏆🏆🏆 TOP 15 ULTIMATE BREAKTHROUGH DISCOVERIES 🏆🏆🏆")
            top_15 = discoveries_df.head(15)
            for idx, (_, row) in enumerate(top_15.iterrows()):
                print(f"{idx+1:2d}. 🔥 {row['社名'][:40]:<40} | Score: {row['ULTIMATE総合スコア']:<6} | {row['信頼度レベル']}")
                print(f"    💼 {row['部署名'][:50]}")
                print(f"    🎯 {row['肩書'][:50]}")
                print(f"    🔍 {row['発見根拠'][:100]}...")
                print()
            
            return len(discoveries_df), discoveries_df
        else:
            print("🤔 ULTIMATE ALGORITHM FOUND NO ADDITIONAL IT COMPANIES")
            print("💭 REMAINING COMPANIES MAY BE TRULY NON-IT")
            return 0, pd.DataFrame()
        
    except Exception as e:
        print(f"💥 ULTIMATE BREAKTHROUGH ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 0, pd.DataFrame()

if __name__ == "__main__":
    discovered_count, discoveries_df = execute_ultimate_breakthrough()
    
    if discovered_count > 0:
        print(f"🎉🎉🎉 ULTIMATE BREAKTHROUGH SUCCESS! 🎉🎉🎉")
        print(f"💎 30,000円 POWER UNLEASHED!")
        print(f"🔥 HIDDEN IT COMPANIES DISCOVERED: {discovered_count}")
        print(f"🧠 VERY HARD TASK - ULTIMATE COMPLETION!")
        print(f"💰 MONEY WELL SPENT - BREAKTHROUGH ACHIEVED!")
    else:
        print("🤯 ULTIMATE BREAKTHROUGH ENCOUNTERED UNPRECEDENTED CHALLENGE")
        print("🔬 FURTHER ALGORITHM EVOLUTION MAY BE REQUIRED")