/**
 * CareerCompass - Main Application Controller
 * Handles routing, view rendering, user interaction, state management,
 * and animations for the CareerCompass Single Page Application.
 */

// Global State
const appState = {
  currentView: 'home',
  wizard: {
    step: 1, // 1: Path, 2: Interests, 3: Results
    selectedPath: null,
    selectedInterests: []
  },
  lastScrollPosition: 0,
  compareList: [] // list of career IDs selected for comparison
};

// Interest Pool mapping based on Path selection
const interestPools = {
  'computer science & technology': [
    { name: 'Software & App Development', label: 'Software & App Development', icon: 'cpu' },
    { name: 'Data & AI', label: 'Data & AI', icon: 'brain' },
    { name: 'Cybersecurity & Infrastructure', label: 'Cybersecurity & Infrastructure', icon: 'shield' },
    { name: 'Hardware & Engineering', label: 'Hardware & Engineering', icon: 'settings' },
    { name: 'Telecom & Networks', label: 'Telecom & Networks', icon: 'wifi' },
    { name: 'Product, Design & Quality', label: 'Product, Design & Quality', icon: 'trello' },
    { name: 'Emerging Tech', label: 'Emerging Tech', icon: 'zap' }
  ],
  'medicine & healthcare': [
    { name: 'Clinical Medicine', label: 'Clinical Medicine', icon: 'activity' },
    { name: 'Dental Care', label: 'Dental Care', icon: 'smile' },
    { name: 'Nursing & Allied Care', label: 'Nursing & Allied Care', icon: 'heart' },
    { name: 'Vision Care', label: 'Vision Care', icon: 'eye' },
    { name: 'Diagnostics & Lab', label: 'Diagnostics & Lab', icon: 'search' },
    { name: 'Pharma & Alternative Medicine', label: 'Pharma & Alternative Medicine', icon: 'pill' },
    { name: 'Nutrition & Wellness', label: 'Nutrition & Wellness', icon: 'apple' },
    { name: 'Health Systems & Tech', label: 'Health Systems & Tech', icon: 'settings' },
    { name: 'Medical Research', label: 'Medical Research', icon: 'flask-conical' }
  ],
  'pure sciences & research': [
    { name: 'Physical Sciences', label: 'Physical Sciences', icon: 'sun' },
    { name: 'Chemical Sciences', label: 'Chemical Sciences', icon: 'flask-conical' },
    { name: 'Biological Sciences', label: 'Biological Sciences', icon: 'dna' },
    { name: 'Earth Sciences', label: 'Earth Sciences', icon: 'globe' },
    { name: 'Environmental Science', label: 'Environmental Science', icon: 'wind' },
    { name: 'Space Science', label: 'Space Science', icon: 'rocket' },
    { name: 'Mathematics & Statistics', label: 'Mathematics & Statistics', icon: 'percent' },
    { name: 'Applied & Forensic Science', label: 'Applied & Forensic Science', icon: 'search' },
    { name: 'Science Communication', label: 'Science Communication', icon: 'message-square' }
  ],
  'business, finance & economics': [
    { name: 'Accounting & Auditing', label: 'Accounting & Auditing', icon: 'calculator' },
    { name: 'Finance & Investment', label: 'Finance & Investment', icon: 'dollar-sign' },
    { name: 'Strategy & Consulting', label: 'Strategy & Consulting', icon: 'target' },
    { name: 'Marketing & Growth', label: 'Marketing & Growth', icon: 'trending-up' },
    { name: 'Operations & People', label: 'Operations & People', icon: 'users' },
    { name: 'Entrepreneurship & Trade', label: 'Entrepreneurship & Trade', icon: 'briefcase' }
  ],
  'social sciences & humanities': [
    { name: 'Mind & Behavior', label: 'Mind & Behavior', icon: 'smile' },
    { name: 'Society & Culture', label: 'Society & Culture', icon: 'users' },
    { name: 'Media & Communication', label: 'Media & Communication', icon: 'message-square' },
    { name: 'Governance & Policy', label: 'Governance & Policy', icon: 'landmark' },
    { name: 'Education & Knowledge', label: 'Education & Knowledge', icon: 'book-open' },
    { name: 'Social Impact', label: 'Social Impact', icon: 'heart' },
    { name: 'Philosophy & Ethics', label: 'Philosophy & Ethics', icon: 'award' }
  ],
  'vocational / skilled trades': [
    { name: 'Electrical & Electronics', label: 'Electrical & Electronics', icon: 'zap' },
    { name: 'Mechanical & Automotive', label: 'Mechanical & Automotive', icon: 'settings' },
    { name: 'Construction & Building', label: 'Construction & Building', icon: 'wrench' },
    { name: 'Personal Care & Craft', label: 'Personal Care & Craft', icon: 'scissors' },
    { name: 'Food Production', label: 'Food Production', icon: 'coffee' },
    { name: 'Printing & Manufacturing', label: 'Printing & Manufacturing', icon: 'printer' }
  ],
  'defense & civil services': [
    { name: 'Armed Forces', label: 'Armed Forces', icon: 'shield' },
    { name: 'Coast & Border Security', label: 'Coast & Border Security', icon: 'anchor' },
    { name: 'Defense Technology & Intelligence', label: 'Defense Technology & Intelligence', icon: 'cpu' },
    { name: 'Defense Support Services', label: 'Defense Support Services', icon: 'truck' }
  ],
  'government (upsc/ssc track)': [
    { name: 'All-India Civil Services', label: 'All-India Civil Services', icon: 'landmark' },
    { name: 'Revenue & Customs', label: 'Revenue & Customs', icon: 'percent' },
    { name: 'Public Sector & Local Bodies', label: 'Public Sector & Local Bodies', icon: 'building' },
    { name: 'Statistical & Audit Services', label: 'Statistical & Audit Services', icon: 'calculator' }
  ],
  'sports & fitness': [
    { name: 'Competitive Sport', label: 'Competitive Sport', icon: 'trophy' },
    { name: 'Coaching & Training', label: 'Coaching & Training', icon: 'users' },
    { name: 'Sports Science & Health', label: 'Sports Science & Health', icon: 'heart' },
    { name: 'Sports Business & Media', label: 'Sports Business & Media', icon: 'trending-up' },
    { name: 'Officiating & Design', label: 'Officiating & Design', icon: 'award' }
  ],
  'performing arts': [
    { name: 'Music', label: 'Music', icon: 'music' },
    { name: 'Acting & Theatre', label: 'Acting & Theatre', icon: 'film' },
    { name: 'Dance', label: 'Dance', icon: 'activity' },
    { name: 'Film Production', label: 'Film Production', icon: 'video' }
  ],
  'agriculture & allied sciences': [
    { name: 'Crop & Soil Science', label: 'Crop & Soil Science', icon: 'leaf' },
    { name: 'Animal & Fisheries Science', label: 'Animal & Fisheries Science', icon: 'fish' },
    { name: 'AgriTech & Engineering', label: 'AgriTech & Engineering', icon: 'settings' },
    { name: 'Food & Forestry', label: 'Food & Forestry', icon: 'tree-pine' }
  ],
  'hospitality': [
    { name: 'Hotel Operations', label: 'Hotel Operations', icon: 'building' },
    { name: 'Culinary Arts', label: 'Culinary Arts', icon: 'coffee' },
    { name: 'Travel & Tourism', label: 'Travel & Tourism', icon: 'globe' },
    { name: 'Events & Dining', label: 'Events & Dining', icon: 'calendar' }
  ],
  'law': [
    { name: 'Litigation & Advocacy', label: 'Litigation & Advocacy', icon: 'scale' },
    { name: 'Judiciary', label: 'Judiciary', icon: 'award' },
    { name: 'Specialized Legal Practice', label: 'Specialized Legal Practice', icon: 'briefcase' },
    { name: 'Legal Research & Compliance', label: 'Legal Research & Compliance', icon: 'search' }
  ]
};

// Initialize Application
document.addEventListener('DOMContentLoaded', async () => {
  // Load data cache initially
  await window.CareerCompassData.loadDatabase();
  
  // Setup Router
  window.addEventListener('hashchange', handleRouting);
  
  // Setup Mobile Nav Toggle
  setupMobileNav();
  
  // Run router for initial load
  handleRouting();

  // Setup Modal Closing on overlay click and Event Delegation for Accordions
  const modalOverlay = document.getElementById('career-modal');
  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        closeCareerModal();
        return;
      }
      
      // Accordion Tier toggle
      const tierHeader = e.target.closest('.college-tier-header');
      if (tierHeader) {
        const group = tierHeader.closest('.college-tier-group');
        if (group) {
          group.classList.toggle('active');
        }
        return;
      }
      
      // College Row toggle
      const rowTrigger = e.target.closest('.college-row-trigger');
      if (rowTrigger) {
        const row = rowTrigger.closest('.college-row-item');
        if (row) {
          row.classList.toggle('open');
          const isExpanded = row.classList.contains('open');
          rowTrigger.setAttribute('aria-expanded', isExpanded);
        }
        return;
      }
    });
  }
});

// Setup Mobile Navigation Menu
function setupMobileNav() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const navMenu = document.getElementById('nav-menu');
  
  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', () => {
      navMenu.classList.toggle('mobile-active');
      const icon = toggleBtn.querySelector('i');
      if (icon) {
        if (navMenu.classList.contains('mobile-active')) {
          icon.setAttribute('data-lucide', 'x');
        } else {
          icon.setAttribute('data-lucide', 'menu');
        }
        lucide.createIcons();
      }
    });

    // Close mobile menu on nav link clicks
    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('mobile-active');
        const icon = toggleBtn.querySelector('i');
        if (icon) {
          icon.setAttribute('data-lucide', 'menu');
          lucide.createIcons();
        }
      });
    });
  }
}

// Router
async function handleRouting() {
  const hash = window.location.hash || '#home';
  const container = document.getElementById('view-container');
  
  // Update Active Link styling in navbar
  updateActiveNavLink(hash);
  
  // Close any open modals
  const modalOverlay = document.getElementById('career-modal');
  if (modalOverlay && modalOverlay.classList.contains('active')) {
    modalOverlay.classList.remove('active');
  }

  // Parse Path and Queries (e.g. #career?id=data-scientist or #exams?highlight=CLAT)
  const pathParts = hash.split('?');
  const path = pathParts[0];
  const queryStr = pathParts[1] || '';
  const queryParams = new URLSearchParams(queryStr);

  // Update floating compare badge visibility
  updateCompareFloatingBadge();

  switch (path) {
    case '#home':
      appState.currentView = 'home';
      renderHome(container);
      break;
    case '#explore':
      appState.currentView = 'explore';
      await renderExplore(container, queryParams);
      break;
    case '#exams':
      appState.currentView = 'exams';
      await renderExams(container, queryParams);
      break;
    case '#colleges':
      appState.currentView = 'colleges';
      await renderColleges(container);
      break;
    case '#compare':
      appState.currentView = 'compare';
      await renderCompare(container);
      break;
    case '#about':
      appState.currentView = 'about';
      renderAbout(container);
      break;
    default:
      // Fallback to home
      window.location.hash = '#home';
  }
  
  // Initialize icons for the newly rendered view
  lucide.createIcons();
  
  // Scroll to top on route change, unless it's a sub-action
  window.scrollTo({ top: 0, behavior: 'instant' });
}

// Highlights the current active navigation item in the header
function updateActiveNavLink(hash) {
  const links = document.querySelectorAll('nav a');
  const baseHash = hash.split('?')[0];
  
  links.forEach(link => {
    if (link.getAttribute('href') === baseHash) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// -------------------------------------------------------------
// VIEW RENDERERS
// -------------------------------------------------------------

// Render Home View
function renderHome(container) {
  container.innerHTML = `
    <section class="hero">
      <div class="hero-badge">Discover Your Potential</div>
      <h1 class="hero-title">Beyond Engineering & Medicine:<br>Find Your <mark>True Direction</mark>.</h1>
      <p class="hero-subtitle">
        Just finished Class 12? Unsure what's next? CareerCompass helps Indian students break free from standard career options and explore exciting paths customized to their actual interests.
      </p>
      
      <div class="hero-stats-bar" style="margin-top: 0.5rem; margin-bottom: 2.5rem; font-size: 1.1rem; color: var(--text-secondary); display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; align-items: center;">
        <span class="stat-stat-item"><span class="skeleton" style="display:inline-block; width: 40px; height: 1.2rem;"></span> careers</span> &middot; 
        <span class="stat-stat-item"><span class="skeleton" style="display:inline-block; width: 40px; height: 1.2rem;"></span> exams</span> &middot; 
        <span class="stat-stat-item"><span class="skeleton" style="display:inline-block; width: 40px; height: 1.2rem;"></span> colleges</span>
      </div>

      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="#explore" class="btn btn-primary">
          Find My Career Path
          <i data-lucide="compass"></i>
        </a>
        <a href="#about" class="btn btn-secondary">Learn Why We Exist</a>
      </div>
    </section>

    <div class="section-header" style="margin-top: 2rem; margin-bottom: 2rem;">
      <h2>How it works</h2>
      <p>Three simple steps to discover your career matches</p>
    </div>

    <section class="quick-stats">
      <div class="stat-card">
        <div class="stat-icon"><i data-lucide="layers"></i></div>
        <h3>1. Select Your Path</h3>
        <p>Choose from 11 specialized pathways, covering traditional streams and modern vocational/applied fields.</p>
      </div>
      <div class="stat-card">
        <div class="stat-icon"><i data-lucide="check-square"></i></div>
        <h3>2. Highlight Interests</h3>
        <p>Pick 2-3 topics you actually enjoy—from tech and design to counseling or finance.</p>
      </div>
      <div class="stat-card">
        <div class="stat-icon"><i data-lucide="award"></i></div>
        <h3>3. Explore Matches</h3>
        <p>Get a customized map of modern careers, educational paths, entrance exams, and colleges.</p>
      </div>
    </section>
  `;
  loadHomeStats();
}

async function loadHomeStats() {
  const statsBar = document.querySelector('.hero-stats-bar');
  if (!statsBar) return;
  try {
    const [careers, exams, colleges] = await Promise.all([
      window.CareerCompassData.getCareers(),
      window.CareerCompassData.getExams(),
      window.CareerCompassData.getColleges()
    ]);
    statsBar.innerHTML = `
      <span class="stat-stat-item" style="font-weight: 700; color: var(--primary);">${careers.length}</span> careers &middot; 
      <span class="stat-stat-item" style="font-weight: 700; color: var(--accent);">${exams.length}</span> exams &middot; 
      <span class="stat-stat-item" style="font-weight: 700; color: var(--emerald);">${colleges.length}</span> colleges
    `;
  } catch (error) {
    console.error("Failed to load home stats:", error);
    statsBar.innerHTML = `<span style="font-size: 0.95rem; color: var(--text-secondary);">Empowering Indian high school graduates since 2026.</span>`;
  }
}

// Render Explore & Selectors View
async function renderExplore(container, queryParams) {
  // If career ID is specified in query parameters, we can render the explorer background
  // and trigger the detail modal on top.
  const careerId = queryParams.get('id');

  container.innerHTML = `
    <div class="section-header">
      <h2>Career Discovery Wizard</h2>
      <p>Filter by your background and fields of interest to find custom career trajectories.</p>
    </div>
    
    <div class="wizard-container" id="wizard-container">
      <!-- Wizard Progress Indicators -->
      <div class="wizard-progress">
        <div class="progress-step ${appState.wizard.step >= 1 ? 'active' : ''} ${appState.wizard.step > 1 ? 'completed' : ''}" id="step-indicator-1">
          1
          <div class="progress-step-label">Select Path</div>
        </div>
        <div class="progress-step ${appState.wizard.step >= 2 ? 'active' : ''} ${appState.wizard.step > 2 ? 'completed' : ''}" id="step-indicator-2">
          2
          <div class="progress-step-label">Select Interests</div>
        </div>
        <div class="progress-step ${appState.wizard.step >= 3 ? 'active' : ''}" id="step-indicator-3">
          3
          <div class="progress-step-label">Matching Careers</div>
        </div>
      </div>

      <!-- STEP 1: Path Selection -->
      <div class="wizard-step ${appState.wizard.step === 1 ? 'active' : ''}" id="wizard-step-1">
        <h3 style="font-family: var(--font-title); font-size: 1.5rem; text-align: center; margin-bottom: 1.5rem;">
          What's your path?
        </h3>
        
        <!-- Search filter input above the grid -->
        <div class="search-input-wrap" style="max-width: 400px; margin: 0 auto 2rem auto;">
          <i data-lucide="search"></i>
          <input type="text" class="search-input" id="path-search-box" placeholder="Search path by name...">
        </div>
        
        <div class="path-grid" id="paths-list-container">
          <!-- Dynamically populated from JS -->
        </div>
      </div>

      <!-- STEP 2: Interests Picker -->
      <div class="wizard-step ${appState.wizard.step === 2 ? 'active' : ''}" id="wizard-step-2">
        <div class="interests-intro">
          <h3 id="interests-title-text">What excites you?</h3>
          <p style="color: var(--text-secondary);">Select 2 to 3 tags that capture your curiosity (Minimum 1 required).</p>
        </div>
        <div class="interests-grid" id="interests-container">
          <!-- Dynamically populated from JS -->
        </div>
        
        <div class="wizard-nav">
          <button class="btn btn-secondary" id="btn-back-to-step-1">
            <i data-lucide="arrow-left"></i> Back
          </button>
          <button class="btn btn-primary" id="btn-to-step-3" disabled>
            Find Career Matches <i data-lucide="arrow-right"></i>
          </button>
        </div>
      </div>

      <!-- STEP 3: Results Grid -->
      <div class="wizard-step ${appState.wizard.step === 3 ? 'active' : ''}" id="wizard-step-3">
        <div class="results-header">
          <div class="results-meta">
            Showing matches for <strong>${appState.wizard.selectedPath || ''}</strong> 
            with interests: <strong>${appState.wizard.selectedInterests.join(', ') || ''}</strong>
          </div>
          <button class="btn btn-secondary btn-outline" id="btn-reset-wizard" style="padding: 0.5rem 1rem; font-size: 0.9rem;">
            <i data-lucide="refresh-cw"></i> Restart Search
          </button>
        </div>
        
        <div class="careers-grid" id="careers-results-container">
          <!-- Dynamically populated careers cards -->
        </div>
      </div>
    </div>
  `;

  // Fetch paths and initialize Step 1 / 2 / 3
  try {
    const paths = await window.CareerCompassData.getPaths();
    
    // Function to populate path cards
    function populatePaths(list) {
      const pathsContainer = document.getElementById('paths-list-container');
      if (!pathsContainer) return;
      
      const iconMap = {
        "Computer Science & Technology": "cpu",
        "Medicine & Healthcare": "heart",
        "Pure Sciences & Research": "atom",
        "Business, Finance & Economics": "trending-up",
        "Social Sciences & Humanities": "book-open",
        "Vocational / Skilled Trades": "wrench",
        "Defense & Civil Services": "shield",
        "Government (UPSC/SSC track)": "landmark",
        "Sports & Fitness": "trophy",
        "Performing Arts": "music",
        "Agriculture & Allied Sciences": "leaf",
        "Hospitality": "coffee",
        "Law": "scale"
      };

      const descMap = {
        "Computer Science & Technology": "Coding, software, systems engineering, cybersecurity, and artificial intelligence.",
        "Medicine & Healthcare": "Clinical practice, surgery, nursing, pharmaceuticals, and allied health sciences.",
        "Pure Sciences & Research": "Fundamental research in physics, chemistry, biology, mathematics, and climate sciences.",
        "Business, Finance & Economics": "Corporate finance, actuarial systems, management, entrepreneurship, and economics.",
        "Social Sciences & Humanities": "Psychology, sociology, history, journalism, languages, and education studies.",
        "Vocational / Skilled Trades": "Hands-on careers, craftsmanship, technical trades, and specialized skills.",
        "Defense & Civil Services": "Army, Navy, Air Force, police forces, and national security roles.",
        "Government (UPSC/SSC track)": "Public administration, civil services, and government sector careers.",
        "Sports & Fitness": "Professional sports, coaching, fitness instruction, and sports science.",
        "Performing Arts": "Music, dance, acting, theatre, film production, and creative arts.",
        "Agriculture & Allied Sciences": "Modern farming, horticulture, animal husbandry, and agribusiness.",
        "Hospitality": "Hotel management, culinary arts, travel, tourism, and event planning.",
        "Law": "Legal practice, corporate law, litigation, judiciary, and public policy."
      };

      pathsContainer.innerHTML = list.map(path => {
        const icon = iconMap[path.name] || "compass";
        const desc = descMap[path.name] || "Explore career options and choices.";
        const isSelected = appState.wizard.selectedPath === path.name;
        
        return `
          <div class="path-card ${isSelected ? 'selected' : ''}" data-path="${path.name}">
            <div class="path-card-icon"><i data-lucide="${icon}"></i></div>
            <h3>${path.name}</h3>
            <p>${desc}</p>
          </div>
        `;
      }).join('');
      
      // Bind click events on path cards
      pathsContainer.querySelectorAll('.path-card').forEach(card => {
        card.addEventListener('click', () => {
          pathsContainer.querySelectorAll('.path-card').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          
          const chosenPath = card.getAttribute('data-path');
          if (appState.wizard.selectedPath !== chosenPath) {
            appState.wizard.selectedPath = chosenPath;
            appState.wizard.selectedInterests = [];
          }
          
          appState.wizard.step = 2;
          updateStepUI();
          populateInterests();
          lucide.createIcons();
        });
      });
      
      lucide.createIcons();
    }

    // Initial populate
    if (appState.wizard.step === 1) {
      populatePaths(paths);
      
      // Bind Search Box
      const searchBox = document.getElementById('path-search-box');
      if (searchBox) {
        searchBox.addEventListener('input', (e) => {
          const q = e.target.value.toLowerCase().trim();
          const filtered = paths.filter(p => p.name.toLowerCase().includes(q));
          populatePaths(filtered);
        });
      }
    }

    // Bind Event Listeners for wizard navigation buttons
    bindWizardEvents(paths, populatePaths);

    // If we are currently at Step 2 or 3, load content appropriately
    if (appState.wizard.step === 2 && appState.wizard.selectedPath) {
      populateInterests();
    } else if (appState.wizard.step === 3 && appState.wizard.selectedPath) {
      await displayCareerMatches();
    }

  } catch (error) {
    console.error("Error initializing explore view paths:", error);
    const containerStep1 = document.getElementById('paths-list-container');
    if (containerStep1) {
      renderErrorState(containerStep1, () => renderExplore(container, queryParams));
    }
  }

  // Trigger modal if direct career id specified
  if (careerId) {
    const career = await window.CareerCompassData.getCareerById(careerId);
    if (career) {
      showCareerModal(career);
    }
  }
}

// Binds event listeners for path selection, tags selection, and step movement buttons
function bindWizardEvents(paths, populatePathsCallback) {
  // Step 2 Back Button
  const back1 = document.getElementById('btn-back-to-step-1');
  if (back1) {
    back1.addEventListener('click', () => {
      appState.wizard.step = 1;
      updateStepUI();
      // Re-populate paths and search box binding on back
      setTimeout(() => {
        populatePathsCallback(paths);
        const searchBox = document.getElementById('path-search-box');
        if (searchBox) {
          searchBox.addEventListener('input', (e) => {
            const q = e.target.value.toLowerCase().trim();
            const filtered = paths.filter(p => p.name.toLowerCase().includes(q));
            populatePathsCallback(filtered);
          });
        }
      }, 50);
      lucide.createIcons();
    });
  }

  // Step 2 Forward Button (Match Career results)
  const toStep3 = document.getElementById('btn-to-step-3');
  if (toStep3) {
    toStep3.addEventListener('click', async () => {
      appState.wizard.step = 3;
      updateStepUI();
      await displayCareerMatches();
      lucide.createIcons();
    });
  }

  // Step 3 Reset Button
  const resetBtn = document.getElementById('btn-reset-wizard');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      appState.wizard.step = 1;
      appState.wizard.selectedPath = null;
      appState.wizard.selectedInterests = [];
      updateStepUI();
      
      // Re-populate paths and search box
      setTimeout(() => {
        populatePathsCallback(paths);
        const searchBox = document.getElementById('path-search-box');
        if (searchBox) {
          searchBox.value = '';
          searchBox.addEventListener('input', (e) => {
            const q = e.target.value.toLowerCase().trim();
            const filtered = paths.filter(p => p.name.toLowerCase().includes(q));
            populatePathsCallback(filtered);
          });
        }
      }, 50);
      lucide.createIcons();
    });
  }
}

// Updates step active classes, visibility of panels, and indicator states
function updateStepUI() {
  const s1 = document.getElementById('wizard-step-1');
  const s2 = document.getElementById('wizard-step-2');
  const s3 = document.getElementById('wizard-step-3');
  const i1 = document.getElementById('step-indicator-1');
  const i2 = document.getElementById('step-indicator-2');
  const i3 = document.getElementById('step-indicator-3');

  // Set classes
  if (s1) s1.classList.remove('active');
  if (s2) s2.classList.remove('active');
  if (s3) s3.classList.remove('active');

  if (i1) i1.className = 'progress-step';
  if (i2) i2.className = 'progress-step';
  if (i3) i3.className = 'progress-step';

  if (appState.wizard.step === 1) {
    if (s1) s1.classList.add('active');
    if (i1) i1.classList.add('active');
  } else if (appState.wizard.step === 2) {
    if (s2) s2.classList.add('active');
    if (i1) {
      i1.classList.add('completed');
      const label = i1.querySelector('.progress-step-label');
      if (label) label.textContent = "Select Path";
    }
    if (i2) i2.classList.add('active');
  } else if (appState.wizard.step === 3) {
    if (s3) s3.classList.add('active');
    if (i1) {
      i1.classList.add('completed');
      const label = i1.querySelector('.progress-step-label');
      if (label) label.textContent = "Select Path";
    }
    if (i2) i2.classList.add('completed');
    if (i3) i3.classList.add('active');
  }

  // Update floating compare badge visibility
  updateCompareFloatingBadge();
}

// Fills step 2 interest checklist with appropriate path tags
function populateInterests() {
  const container = document.getElementById('interests-container');
  const titleText = document.getElementById('interests-title-text');
  if (!container) return;

  const pathKey = appState.wizard.selectedPath.toLowerCase();
  const pathInterests = interestPools[pathKey] || [];

  const combined = pathInterests;

  if (titleText) {
    titleText.textContent = `Interests for ${appState.wizard.selectedPath}`;
  }

  container.innerHTML = combined.map(item => {
    const isChecked = appState.wizard.selectedInterests.includes(item.name);
    return `
      <label class="interest-tag">
        <input type="checkbox" value="${item.name}" ${isChecked ? 'checked' : ''}>
        <span class="interest-label">
          <i data-lucide="${item.icon}"></i>
          ${item.label}
        </span>
      </label>
    `;
  }).join('');

  // Bind change listeners to checkboxes
  const checkboxes = container.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(box => {
    box.addEventListener('change', () => {
      const value = box.value;
      if (box.checked) {
        // Enforce 3-interest maximum limit for focused results
        if (appState.wizard.selectedInterests.length >= 3) {
          box.checked = false; // block check
          alert("You can select a maximum of 3 interests for best matching recommendations.");
          return;
        }
        appState.wizard.selectedInterests.push(value);
      } else {
        appState.wizard.selectedInterests = appState.wizard.selectedInterests.filter(i => i !== value);
      }
      
      // Update forward button disabled status (needs at least 1 interest selected)
      const nextBtn = document.getElementById('btn-to-step-3');
      if (nextBtn) {
        nextBtn.disabled = appState.wizard.selectedInterests.length === 0;
      }
    });
  });

  // Initial trigger for forward button state
  const nextBtn = document.getElementById('btn-to-step-3');
  if (nextBtn) {
    nextBtn.disabled = appState.wizard.selectedInterests.length === 0;
  }
}

// Queries matches from db and populates results card grid
async function displayCareerMatches() {
  const container = document.getElementById('careers-results-container');
  if (!container) return;

  // Show skeleton loader
  container.innerHTML = `
    <div class="skeleton-card">
      <div class="skeleton skeleton-badge"></div>
      <div class="skeleton skeleton-title"></div>
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text short"></div>
    </div>
    <div class="skeleton-card">
      <div class="skeleton skeleton-badge"></div>
      <div class="skeleton skeleton-title"></div>
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text short"></div>
    </div>
    <div class="skeleton-card">
      <div class="skeleton skeleton-badge"></div>
      <div class="skeleton skeleton-title"></div>
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text short"></div>
    </div>
  `;

  try {
    const results = await window.CareerCompassData.getCareers(
      appState.wizard.selectedPath,
      appState.wizard.selectedInterests
    );

    if (results.length === 0) {
      container.innerHTML = `
        <div class="empty-state" style="grid-column: 1/-1;">
          <i data-lucide="help-circle"></i>
          <h3>No Direct Match Found</h3>
          <p>No careers match this exact combo of interests. Try broadening your interest tags or selecting a different path!</p>
          <button class="btn btn-primary btn-outline" id="btn-empty-reset">
            Adjust Interests
          </button>
        </div>
      `;
      lucide.createIcons();
      const btnEmptyReset = document.getElementById('btn-empty-reset');
      if (btnEmptyReset) {
        btnEmptyReset.addEventListener('click', () => {
          appState.wizard.step = 2;
          updateStepUI();
          populateInterests();
          lucide.createIcons();
        });
      }
      return;
    }

    container.innerHTML = results.map(career => {
      // Create safe CSS classes for badges by removing special chars
      const pathClass = career.path.toLowerCase().replace(/[^a-z0-9]/g, '-');
      const dotsMarkup = career.interests
        .map(tag => `<span class="career-interest-dot">${tag}</span>`)
        .join('');

      return `
        <div class="career-card" data-id="${career.id}">
          <label class="card-compare-checkbox" onclick="event.stopPropagation();">
            <input type="checkbox" data-id="${career.id}" ${appState.compareList.includes(career.id) ? 'checked' : ''}>
            Compare
          </label>
          <div class="career-card-top">
            <span class="career-badge ${pathClass}">${career.path}</span>
            <h3>${career.title}</h3>
            <p>${career.description}</p>
          </div>
          <div class="career-card-footer">
            <div class="career-interests-wrap">
              ${dotsMarkup}
            </div>
            <a href="#explore?id=${career.id}" class="career-link">
              Details <i data-lucide="chevron-right"></i>
            </a>
          </div>
        </div>
      `;
    }).join('');

    // Bind click events on cards to open modal
    container.querySelectorAll('.career-card').forEach(card => {
      card.addEventListener('click', async (e) => {
        if (e.target.closest('a') || e.target.closest('.card-compare-checkbox')) return;
        const id = card.getAttribute('data-id');
        window.location.hash = `#explore?id=${id}`;
      });
    });

    // Bind checkbox change events for compare
    container.querySelectorAll('.card-compare-checkbox input').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        const id = checkbox.getAttribute('data-id');
        if (checkbox.checked) {
          if (appState.compareList.length >= 3) {
            checkbox.checked = false;
            alert("You can compare a maximum of 3 careers side-by-side.");
            return;
          }
          if (!appState.compareList.includes(id)) {
            appState.compareList.push(id);
          }
        } else {
          appState.compareList = appState.compareList.filter(item => item !== id);
        }
        updateCompareFloatingBadge();
      });
    });

    lucide.createIcons();
  } catch (error) {
    console.error("Error displaying matches:", error);
    renderErrorState(container, () => displayCareerMatches());
  }
}

// Render Entrance Exams View
// Render Entrance Exams View
async function renderExams(container, queryParams) {
  const queryHighlight = queryParams.get('highlight');
  
  container.innerHTML = `
    <div class="section-header">
      <h2>National & International Entrance Exams</h2>
      <p>Key information regarding crucial entrance examinations for high school graduates in India.</p>
    </div>

    <!-- Search / Filtering bar -->
    <div class="filters-bar" style="margin-bottom: 3rem;">
      <div class="search-input-wrap">
        <i data-lucide="search"></i>
        <input type="text" class="search-input" id="exams-search-box" placeholder="Search exams by name, eligibility or purpose...">
      </div>
    </div>

    <div class="exams-grid" id="exams-list-container">
      <div class="skeleton-card">
        <div class="skeleton skeleton-title"></div>
        <div class="skeleton skeleton-text"></div>
        <div class="skeleton skeleton-text short"></div>
      </div>
      <div class="skeleton-card">
        <div class="skeleton skeleton-title"></div>
        <div class="skeleton skeleton-text"></div>
        <div class="skeleton skeleton-text short"></div>
      </div>
    </div>
  `;

  const displayContainer = document.getElementById('exams-list-container');

  async function fetchAndPopulate() {
    try {
      const exams = await window.CareerCompassData.getExams();
      
      function populateExams(list) {
        if (list.length === 0) {
          displayContainer.innerHTML = `
            <div class="empty-state" style="grid-column: 1/-1;">
              <i data-lucide="info"></i>
              <h3>No Exams Found</h3>
              <p>No exams match your search criteria. Try a different search term.</p>
            </div>
          `;
          lucide.createIcons();
          return;
        }

        displayContainer.innerHTML = list.map(exam => {
          const isHighlighted = queryHighlight && exam.id.toLowerCase() === queryHighlight.toLowerCase();
          const highlightStyles = isHighlighted 
            ? 'border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-light); transform: scale(1.02);' 
            : '';

          return `
            <div class="exam-card" id="exam-card-${exam.id}" style="${highlightStyles}">
              <div class="exam-header">
                <div>
                  <h3 class="exam-title">${exam.title}</h3>
                </div>
                <div class="exam-timeline-badge">
                  <i data-lucide="calendar"></i>
                  <span>${exam.timeline}</span>
                </div>
              </div>
              <div class="exam-details">
                <div class="exam-detail-row">
                  <div class="exam-detail-label">Purpose / Admission For</div>
                  <div class="exam-detail-val">${exam.purpose}</div>
                </div>
                <div class="exam-detail-row">
                  <div class="exam-detail-label">Eligibility</div>
                  <div class="exam-detail-val">${exam.eligibility}</div>
                </div>
              </div>
            </div>
          `;
        }).join('');

        // Re-initialize icons inside cards
        lucide.createIcons();
        
        // Scroll highlighted item into view if it exists
        if (queryHighlight) {
          const highlightedEl = document.getElementById(`exam-card-${queryHighlight}`);
          if (highlightedEl) {
            setTimeout(() => {
              highlightedEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 150);
          }
        }
      }

      // Initial draw
      populateExams(exams);

      // Bind Search bar
      const searchBox = document.getElementById('exams-search-box');
      if (searchBox) {
        searchBox.addEventListener('input', (e) => {
          const query = e.target.value.toLowerCase();
          const filtered = exams.filter(exam => 
            exam.title.toLowerCase().includes(query) || 
            exam.purpose.toLowerCase().includes(query) ||
            exam.eligibility.toLowerCase().includes(query)
          );
          populateExams(filtered);
        });
      }
    } catch (error) {
      console.error("Error loading exams:", error);
      renderErrorState(displayContainer, () => fetchAndPopulate());
    }
  }

  await fetchAndPopulate();
}

// Render Colleges View
// Render Colleges View
async function renderColleges(container) {
  // Fetch paths to populate select options dynamically
  let paths = [];
  try {
    paths = await window.CareerCompassData.getPaths();
  } catch (e) {
    console.error("Failed to load paths for college filters", e);
  }

  container.innerHTML = `
    <div class="section-header">
      <h2>Suggested Universities & Colleges</h2>
      <p>Explore top tier educational institutes in India and abroad based on fields of study.</p>
    </div>

    <!-- Multi filters -->
    <div class="filters-bar" style="margin-bottom: 2.5rem; justify-content: space-between;">
      <div class="search-input-wrap" style="max-width: 400px;">
        <i data-lucide="search"></i>
        <input type="text" class="search-input" id="college-search" placeholder="Search college by name or career path...">
      </div>
      
      <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
        <!-- Location Tabs -->
        <div class="filter-tags" id="location-filters">
          <button class="filter-tag-btn active" data-loc="all">All Locations</button>
          <button class="filter-tag-btn" data-loc="india">India Only</button>
          <button class="filter-tag-btn" data-loc="abroad">Abroad Only</button>
        </div>

        <!-- Path Select -->
        <select class="select-filter" id="stream-select-filter">
          <option value="all">All Paths</option>
          ${paths.map(p => `<option value="${p.name.toLowerCase()}">${p.name}</option>`).join('')}
        </select>
      </div>
    </div>

    <div class="colleges-list-container" id="colleges-list-container">
      <div style="display:flex; flex-direction:column; gap:1rem; width:100%;">
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
      </div>
    </div>
  `;

  // Fetch compiled colleges
  let filterLoc = 'all';
  let filterStream = 'all';
  let queryText = '';

  const displayListContainer = document.getElementById('colleges-list-container');

  async function updateCollegesDisplay() {
    displayListContainer.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:1rem; width:100%;">
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
        <div class="skeleton" style="height: 80px; width: 100%; border-radius: var(--radius-md);"></div>
      </div>
    `;

    // Query from data helper
    const resolvedStream = filterStream === 'all' ? null : filterStream;
    const resolvedLoc = filterLoc === 'all' ? null : filterLoc;
    
    try {
      let list = await window.CareerCompassData.getColleges(resolvedStream, resolvedLoc);

      // Apply Client-Side Text Search filter
      if (queryText) {
        list = list.filter(item => 
          item.name.toLowerCase().includes(queryText) || 
          item.careers.some(c => c.toLowerCase().includes(queryText))
        );
      }

      if (list.length === 0) {
        displayListContainer.innerHTML = `
          <div class="empty-state" style="width: 100%;">
            <i data-lucide="map-pin"></i>
            <h3>No Colleges Found</h3>
            <p>We couldn't find colleges matching that criteria. Try clearing the search or changing filter flags.</p>
          </div>
        `;
        lucide.createIcons();
        return;
      }

      displayListContainer.innerHTML = list.map(college => {
        const locClass = college.location.toLowerCase() === 'india' ? 'location-india' : 'location-abroad';
        const pathBadges = college.paths.map(str => `<span class="college-badge stream-tag">${str}</span>`).join(' ');

        return `
          <div class="college-list-item">
            <div class="college-main-info">
              <h3 class="college-name">${college.name}</h3>
              <div class="college-meta-details">
                <span class="college-badge ${locClass}">${college.location}</span>
                <span class="college-badge stream-tag" style="background-color: var(--primary-light); color: var(--primary); font-weight:700;">${college.tier}</span>
                ${pathBadges}
              </div>
            </div>
            <div class="college-careers-associated">
              <span style="font-weight: 500; font-size: 0.8rem; text-transform: uppercase; color: var(--text-secondary);">Offers path to:</span>
              <div style="font-weight: 600; color: var(--text-primary); margin-top: 0.2rem;">${college.careers.join(', ')}</div>
            </div>
          </div>
        `;
      }).join('');

      lucide.createIcons();
    } catch (error) {
      console.error("Error loading colleges:", error);
      renderErrorState(displayListContainer, () => updateCollegesDisplay());
    }
  }

  // Initial draw
  await updateCollegesDisplay();

  // Location filters clicks
  const locButtons = document.querySelectorAll('#location-filters button');
  locButtons.forEach(btn => {
    btn.addEventListener('click', async () => {
      locButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterLoc = btn.getAttribute('data-loc');
      await updateCollegesDisplay();
    });
  });

  // Stream select dropdown filter
  const streamSelect = document.getElementById('stream-select-filter');
  if (streamSelect) {
    streamSelect.addEventListener('change', async (e) => {
      filterStream = e.target.value;
      await updateCollegesDisplay();
    });
  }

  // Search input
  const searchInput = document.getElementById('college-search');
  if (searchInput) {
    searchInput.addEventListener('input', async (e) => {
      queryText = e.target.value.toLowerCase().trim();
      await updateCollegesDisplay();
    });
  }
}

// Render About/Problem Statement View
function renderAbout(container) {
  container.innerHTML = `
    <div class="section-header">
      <h2>Why CareerCompass?</h2>
      <p>The story and core vision driving our project.</p>
    </div>

    <article class="about-section">
      <div class="about-intro-text">
        "Most high school students in India only know 2 or 3 career options. Thousands choose engineering or medicine not by choice, but simply due to a lack of exposure to alternatives."
      </div>
      
      <div class="about-body-text">
        <h3>The Problem</h3>
        <p>
          Every year, millions of class 12th students face high anxiety. In a high-stakes academic culture, societal pressure tends to narrow their focus to competitive national exams like JEE (Engineering) or NEET (Medicine).
        </p>
        <p>
          Unfortunately, this leaves thousands of students unaware of other careers that match their capabilities, interests, and personalities. Modern industries are growing rapidly, creating highly paid and satisfying roles in areas like Astrobiology, User Experience (UX), Actuarial Science, Public Policy, and Industrial Design.
        </p>

        <h3>Our Mission</h3>
        <p>
          <strong>CareerCompass</strong> is built to broaden horizons. We want to make career discovery simple, direct, and accessible for 17-18 year olds in India. 
        </p>
        <p>
          By taking students through a quick, engaging checklist of paths and actual topics they find interesting (rather than complex psychological tests), we present immediate options they might never have heard of, complete with educational roadmaps, matching entrance exams, and leading global institutes.
        </p>
        
        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="#explore" class="btn btn-primary">Try the Career Finder</a>
        </div>
      </div>
    </article>
  `;
}

// -------------------------------------------------------------
// MODAL CONTROLS
// -------------------------------------------------------------

// Displays career details in the modal overlay
// Helper to render college tier accordion markup
function renderCollegeTierMarkup(title, colleges, tierId, defaultOpen = false) {
  if (colleges.length === 0) {
    return `
      <div class="college-tier-group">
        <button class="college-tier-header" data-tier-id="${tierId}" disabled>
          <span class="tier-title">${title}</span>
          <span class="tier-count">(0)</span>
        </button>
      </div>
    `;
  }

  const collegesHtml = colleges.map((col) => {
    const locClass = col.location.toLowerCase() === 'india' ? 'location-india' : 'location-abroad';
    const webButton = col.website_url 
      ? `<a href="${col.website_url}" target="_blank" rel="noopener" class="college-web-link btn btn-secondary">
           Visit Official Website <i data-lucide="external-link"></i>
         </a>`
      : `<p class="college-web-link-placeholder" style="font-style: italic; color: var(--text-secondary); margin-top: 0.5rem; font-size: 0.85rem;">
           Official website pending verification
         </p>`;

    return `
      <div class="college-row-item">
        <button class="college-row-trigger" aria-expanded="false">
          <span class="college-row-name">${col.name}</span>
          <span class="college-badge ${locClass}">${col.location}</span>
          <i data-lucide="chevron-down" class="college-row-chevron"></i>
        </button>
        <div class="college-row-details">
          <p>${col.short_description || 'College details pending updates.'}</p>
          ${webButton}
        </div>
      </div>
    `;
  }).join('');

  return `
    <div class="college-tier-group ${defaultOpen ? 'active' : ''}">
      <button class="college-tier-header" data-tier-id="${tierId}">
        <span class="tier-title">${title}</span>
        <span class="tier-count">(${colleges.length})</span>
        <i data-lucide="chevron-down" class="tier-chevron"></i>
      </button>
      <div class="college-tier-content">
        ${collegesHtml}
      </div>
    </div>
  `;
}

// Displays career details in the modal overlay
function showCareerModal(career) {
  const modal = document.getElementById('career-modal');
  const detailsEl = document.getElementById('modal-details-root');
  
  if (!modal || !detailsEl) return;

  // Track page scroll position to disable scrolling on background
  appState.lastScrollPosition = window.scrollY;
  document.body.style.position = 'fixed';
  document.body.style.top = `-${appState.lastScrollPosition}px`;
  document.body.style.width = '100%';

  // Render Exams Links
  const examLinksMarkup = career.exams && career.exams.length > 0
    ? `<div class="modal-exam-links">
         ${career.exams.map(examId => `
           <a href="#exams?highlight=${examId}" class="modal-exam-item" onclick="closeCareerModal();">
             <span>${examId} Info</span>
             <i data-lucide="external-link"></i>
           </a>
         `).join('')}
       </div>`
    : `<p class="modal-text" style="font-style: italic;">No specific entrance exam required. Direct admissions/merit-based.</p>`;

  // Filter Colleges by Tier
  const collegesList = career.colleges || [];
  const topColleges = collegesList.filter(c => c.tier === 'Top');
  const tier2Colleges = collegesList.filter(c => c.tier === 'Tier 2');
  const tier3Colleges = collegesList.filter(c => c.tier === 'Tier 3');

  // Split educational roadmap into steps
  const roadmapSteps = career.education_path ? career.education_path.split(' || ') : [];
  const roadmapMarkup = roadmapSteps.length > 0
    ? `<div class="roadmap-timeline">
         ${roadmapSteps.map((step, idx) => `
           <div class="roadmap-node-item">
             <div class="roadmap-node-marker">
               <span class="roadmap-node-circle">${idx + 1}</span>
               ${idx < roadmapSteps.length - 1 ? '<span class="roadmap-node-line"></span>' : ''}
             </div>
             <div class="roadmap-node-content">
               <p>${step}</p>
             </div>
           </div>
         `).join('')}
       </div>`
    : `<p class="modal-text" style="font-style: italic;">Roadmap data pending updates.</p>`;

  // Modal content layout
  const pathClass = career.path.toLowerCase().replace(/[^a-z0-9]/g, '-');
  detailsEl.innerHTML = `
    <div class="modal-header-section">
      <span class="career-badge ${pathClass}">${career.path} Path</span>
      <h2>${career.title}</h2>
      <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">${career.description}</p>
      
      <div class="modal-quick-meta" style="display: flex; gap: 2rem; flex-wrap: wrap; margin-top: 1rem; border-top: 1px solid var(--border); padding-top: 1rem;">
        <div>
          <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-secondary); display: block;">Salary Range</span>
          <strong style="color: var(--primary); font-size: 1.1rem;">${career.salary_range || '₹4–8 LPA'}</strong>
        </div>
        <div>
          <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-secondary); display: block;">Growth Outlook</span>
          <strong style="color: var(--accent); font-size: 1.1rem;">${career.growth_outlook || 'Steady growth'}</strong>
        </div>
      </div>
    </div>
    
    <div class="modal-grid">
      <!-- Left Column (Description and Path) -->
      <div class="modal-col-left">
        <div>
          <h3 class="modal-section-title">
            <i data-lucide="help-circle"></i>
            What is this career about?
          </h3>
          <p class="modal-text">${career.role_details}</p>
        </div>
        
        <div>
          <h3 class="modal-section-title">
            <i data-lucide="git-branch"></i>
            Educational Roadmap / Path
          </h3>
          ${roadmapMarkup}
        </div>
      </div>

      <!-- Right Column (Exams & Colleges) -->
      <div class="modal-col-right">
        <div>
          <h4 class="modal-section-title" style="font-size: 1.05rem;">
            <i data-lucide="award"></i> Entrance Exams
          </h4>
          ${examLinksMarkup}
        </div>

        <div>
          <h4 class="modal-section-title" style="font-size: 1.05rem; margin-top: 1rem;">
            <i data-lucide="map-pin"></i> Suggested Colleges & Tiers
          </h4>
          <div class="modal-colleges-list">
            ${renderCollegeTierMarkup("Top Colleges", topColleges, "top", true)}
            ${renderCollegeTierMarkup("Other Strong Options (Tier 2)", tier2Colleges, "tier2")}
            ${renderCollegeTierMarkup("Accessible / Flexible Options (Tier 3)", tier3Colleges, "tier3")}
          </div>
        </div>
      </div>
    </div>
  `;

  // Render icons inside the modal
  lucide.createIcons();

  // Open modal
  modal.classList.add('active');
}

// Closes detail modal overlay
function closeCareerModal() {
  const modal = document.getElementById('career-modal');
  if (!modal) return;

  // Restore scroll positions and background state
  document.body.style.position = '';
  document.body.style.top = '';
  document.body.style.width = '';
  window.scrollTo(0, appState.lastScrollPosition);

  modal.classList.remove('active');

  // Change URL Hash back to simple explore page, dropping the query parameters
  // so the route state matches the actual view (modal closed).
  if (window.location.hash.startsWith('#explore?')) {
    window.location.hash = '#explore';
  }
}

// Make modal close function globally accessible
window.closeCareerModal = closeCareerModal;

// -------------------------------------------------------------
// SKELETONS, ERROR AND COMPARE VIEWS
// -------------------------------------------------------------

// Global Helper to render error states with a retry action
function renderErrorState(container, retryCallback) {
  container.innerHTML = `
    <div class="error-state">
      <i data-lucide="alert-circle"></i>
      <h3>Unable to load information</h3>
      <p>There was a problem contacting the CareerCompass servers. Please check your network connection or try again.</p>
      <button class="btn btn-primary" id="btn-retry-action">
        <i data-lucide="refresh-cw"></i> Retry
      </button>
    </div>
  `;
  lucide.createIcons();
  const btn = container.querySelector('#btn-retry-action');
  if (btn) {
    btn.addEventListener('click', retryCallback);
  }
}

// Global Helper to update floating comparison button
function updateCompareFloatingBadge() {
  let badge = document.getElementById('compare-floating-badge');
  const hash = window.location.hash.split('?')[0];
  const isCompareView = hash === '#compare';
  const isWizardSteps = hash === '#explore' && appState.wizard.step < 3;
  
  if (appState.compareList.length > 0 && !isCompareView && !isWizardSteps) {
    if (!badge) {
      badge = document.createElement('a');
      badge.id = 'compare-floating-badge';
      badge.className = 'compare-floating-badge';
      badge.href = '#compare';
      document.body.appendChild(badge);
    }
    badge.style.display = 'flex';
    badge.innerHTML = `
      <i data-lucide="git-pull-request"></i>
      <span>Compare (${appState.compareList.length}/3)</span>
    `;
    lucide.createIcons();
  } else {
    if (badge) {
      badge.style.display = 'none';
    }
  }
}

// Render Comparison Dashboard View
async function renderCompare(container) {
  // Hide compare badge on this page
  const badge = document.getElementById('compare-floating-badge');
  if (badge) badge.style.display = 'none';

  container.innerHTML = `
    <div class="section-header">
      <h2>Compare Career Trajectories</h2>
      <p>Select up to three careers to compare salaries, growth outlooks, and roadmap details side-by-side.</p>
    </div>
    
    <div class="compare-container">
      <div class="compare-selectors-bar">
        <div class="compare-select-wrap">
          <label>Career 1</label>
          <select class="compare-select" id="compare-select-1">
            <option value="">-- Choose Career --</option>
          </select>
        </div>
        <div class="compare-select-wrap">
          <label>Career 2</label>
          <select class="compare-select" id="compare-select-2">
            <option value="">-- Choose Career --</option>
          </select>
        </div>
        <div class="compare-select-wrap">
          <label>Career 3</label>
          <select class="compare-select" id="compare-select-3">
            <option value="">-- Choose Career --</option>
          </select>
        </div>
      </div>
      
      <div class="compare-table-card" id="compare-table-root">
        <!-- Rendered dynamically -->
      </div>
    </div>
  `;

  // Fetch all careers to populate dropdown lists
  let allCareers = [];
  try {
    allCareers = await window.CareerCompassData.getCareers();
  } catch (error) {
    renderErrorState(container, () => renderCompare(container));
    return;
  }

  // Populate drop downs
  const selectors = [
    document.getElementById('compare-select-1'),
    document.getElementById('compare-select-2'),
    document.getElementById('compare-select-3')
  ];

  selectors.forEach((select, idx) => {
    if (!select) return;
    
    // Populate choices
    allCareers.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c.id;
      opt.textContent = c.title;
      select.appendChild(opt);
    });

    // Pre-select if we already have items in appState.compareList
    if (appState.compareList[idx]) {
      select.value = appState.compareList[idx];
    }

    // Bind change listener
    select.addEventListener('change', () => {
      const val = select.value;
      if (val) {
        appState.compareList[idx] = val;
      } else {
        appState.compareList[idx] = null;
      }
      // Filter out nulls/empties
      appState.compareList = appState.compareList.filter(Boolean);
      rebuildCompareTable(allCareers);
    });
  });

  // Initial draw of table
  rebuildCompareTable(allCareers);
}

function rebuildCompareTable(allCareers) {
  const root = document.getElementById('compare-table-root');
  if (!root) return;

  // Filter compare list to only active selected IDs
  const activeIds = appState.compareList.filter(Boolean);

  if (activeIds.length === 0) {
    root.innerHTML = `
      <div style="text-align: center; padding: 4rem 2rem; color: var(--text-secondary);">
        <i data-lucide="git-pull-request" style="width: 32px; height: 32px; margin-bottom: 1rem; color: var(--border-focus); display: inline-block;"></i>
        <p>Select careers using the dropdown selectors above or from the Find Careers page to compare.</p>
      </div>
    `;
    lucide.createIcons();
    return;
  }

  // Retrieve career objects
  const selectedObjects = activeIds.map(id => allCareers.find(c => c.id === id)).filter(Boolean);

  // Render comparative table
  root.innerHTML = `
    <table class="compare-table">
      <thead>
        <tr>
          <th>Metric / Field</th>
          ${selectedObjects.map(c => {
            const pathClass = c.path.toLowerCase().replace(/[^a-z0-9]/g, '-');
            return `
              <th>
                <div class="compare-cell-title">${c.title}</div>
                <span class="career-badge ${pathClass} compare-cell-stream">${c.path}</span>
              </th>
            `;
          }).join('')}
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="compare-row-header">Description</td>
          ${selectedObjects.map(c => `<td>${c.description}</td>`).join('')}
        </tr>
        <tr>
          <td class="compare-row-header">Salary Range</td>
          ${selectedObjects.map(c => `<td><strong>${c.salary_range || '₹4–8 LPA'}</strong></td>`).join('')}
        </tr>
        <tr>
          <td class="compare-row-header">Growth Outlook</td>
          ${selectedObjects.map(c => `<td><strong>${c.growth_outlook || 'Steady growth'}</strong></td>`).join('')}
        </tr>
        <tr>
          <td class="compare-row-header">Roadmap Steps</td>
          ${selectedObjects.map(c => {
            const steps = c.education_path ? c.education_path.split(' || ') : [];
            const listItems = steps.map(s => `<li>${s}</li>`).join('');
            return `<td><ol class="compare-roadmap-list">${listItems}</ol></td>`;
          }).join('')}
        </tr>
        <tr>
          <td class="compare-row-header">Entrance Exams</td>
          ${selectedObjects.map(c => {
            const examsMarkup = c.exams && c.exams.length > 0
              ? c.exams.map(e => `<span class="career-interest-dot" style="display:inline-block; margin-right:0.35rem; margin-bottom:0.35rem; font-size: 0.8rem; background-color: var(--primary-light); color: var(--primary); padding: 0.25rem 0.5rem; border-radius: var(--radius-sm); font-weight: 600;">${e}</span>`).join('')
              : 'Direct/Merit admission';
            return `<td>${examsMarkup}</td>`;
          }).join('')}
        </tr>
      </tbody>
    </table>
  `;
}
