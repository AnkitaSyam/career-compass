/**
 * CareerCompass - Data Service
 * This file handles all data retrieval operations from the FastAPI backend.
 * The frontend remains decoupled from the specific data source.
 */

/**
 * Loads and verifies the connection to the career database backend.
 * @returns {Promise<Object>} Status object.
 */
async function loadDatabase() {
  try {
    const response = await fetch('http://127.0.0.1:8000/');
    if (!response.ok) {
      throw new Error(`Failed to contact backend: ${response.statusText}`);
    }
    return { success: true };
  } catch (error) {
    console.error("Error contacting CareerCompass backend:", error);
    return { success: false };
  }
}

/**
 * Retrieves careers, filtered by path and matching interests using FastAPI.
 * @param {string} [path] - The path to filter by (e.g. 'Science', 'Commerce', 'Law')
 * @param {string[]} [selectedInterests] - Array of interest tags to match
 * @returns {Promise<Array>} List of matching career objects
 */
async function getCareers(path = null, selectedInterests = []) {
  try {
    let url = 'http://127.0.0.1:8000/careers';
    if (path) {
      url = `http://127.0.0.1:8000/careers/by-path/${encodeURIComponent(path)}`;
    }

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch careers: ${response.statusText}`);
    }

    let results = await response.json();

    // Filter by interests client-side to preserve the dynamic matching logic
    if (selectedInterests && selectedInterests.length > 0) {
      const lowerSelected = selectedInterests.map(i => i.toLowerCase());
      results = results.filter(career => 
        career.interests.some(interest => lowerSelected.includes(interest.toLowerCase()))
      );
    }

    return results;
  } catch (error) {
    console.error("Error in getCareers:", error);
    throw error;
  }
}

/**
 * Retrieves the full list of paths from FastAPI.
 * @returns {Promise<Array>} List of path objects
 */
async function getPaths() {
  try {
    const response = await fetch('http://127.0.0.1:8000/paths');
    if (!response.ok) {
      throw new Error(`Failed to fetch paths: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error in getPaths:", error);
    throw error;
  }
}

/**
 * Retrieves a single career details by its unique string ID from FastAPI.
 * @param {string} id - The career ID (e.g., 'data-scientist')
 * @returns {Promise<Object|null>} The career object or null if not found
 */
async function getCareerById(id) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/career/${encodeURIComponent(id)}`);
    if (!response.ok) {
      if (response.status === 404) return null;
      throw new Error(`Failed to fetch career details: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error in getCareerById for ${id}:`, error);
    throw error;
  }
}

/**
 * Retrieves the full list of entrance exams from FastAPI.
 * @returns {Promise<Array>} List of exam objects
 */
async function getExams() {
  try {
    const response = await fetch('http://127.0.0.1:8000/exams');
    if (!response.ok) {
      throw new Error(`Failed to fetch exams: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error in getExams:", error);
    throw error;
  }
}

/**
 * Helper to fetch a specific exam by ID from FastAPI.
 * @param {string} id - The exam ID
 * @returns {Promise<Object|null>} The exam object or null
 */
async function getExamById(id) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/exam/${encodeURIComponent(id)}`);
    if (!response.ok) {
      if (response.status === 404) return null;
      throw new Error(`Failed to fetch exam details: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error in getExamById for ${id}:`, error);
    throw error;
  }
}

/**
 * Retrieves colleges/universities from FastAPI, with option to filter by path or location.
 * @param {string} [pathFilter] - Optional path to filter by
 * @param {string} [locationFilter] - Optional location filter ('india' or 'abroad')
 * @returns {Promise<Array>} Unique sorted array of college objects: { name, location, paths[], careers[] }
 */
async function getColleges(pathFilter = null, locationFilter = null) {
  try {
    const response = await fetch('http://127.0.0.1:8000/colleges');
    if (!response.ok) {
      throw new Error(`Failed to fetch colleges: ${response.statusText}`);
    }
    
    let collegesList = await response.json();

    // Apply location filter
    if (locationFilter) {
      const locLower = locationFilter.toLowerCase();
      collegesList = collegesList.filter(c => c.location.toLowerCase() === locLower);
    }

    // Apply path filter
    if (pathFilter) {
      const pathLower = pathFilter.toLowerCase();
      collegesList = collegesList.filter(c => 
        c.paths.some(p => p.toLowerCase() === pathLower)
      );
    }

    // Sort alphabetically
    return collegesList.sort((a, b) => a.name.localeCompare(b.name));
  } catch (error) {
    console.error("Error in getColleges:", error);
    throw error;
  }
}

// Expose these methods globally so main.js can use them
window.CareerCompassData = {
  loadDatabase,
  getPaths,
  getCareers,
  getCareerById,
  getExams,
  getExamById,
  getColleges
};
