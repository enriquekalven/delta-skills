import { GoogleGenAI, Type, Schema } from "@google/genai";
// Note: Ensure @google/genai and types/AnalysisResult/StrategyData are correctly defined in your project
import { StrategyData, AnalysisResult } from "../types";

// Define the schema for structured output to ensure consistency
export const strategySchema: Schema = {
  type: Type.OBJECT,
  properties: {
    companyName: { type: Type.STRING },
    ticker: { type: Type.STRING },
    vision: { type: Type.STRING, description: "A single, cohesive, inspiring paragraph (2-3 sentences) combining Mission, Aspiration, and Future State. Do NOT use labels like 'Mission:'." },
    focusAreas: { 
      type: Type.ARRAY, 
      items: { type: Type.STRING },
      description: "Between 3 to 5 strategic pillars. Format: 'Area Name: The core problem/outcome'."
    },
    phases: {
      type: Type.ARRAY,
      items: {
        type: Type.OBJECT,
        properties: {
          id: { type: Type.STRING },
          name: { type: Type.STRING },
          timeframe: { type: Type.STRING },
          initiatives: {
            type: Type.ARRAY,
            items: {
              type: Type.OBJECT,
              properties: {
                id: { type: Type.STRING },
                name: { type: Type.STRING },
                description: { type: Type.STRING },
                businessValue: { type: Type.NUMBER, description: "Score 1-10 based on ROI/Impact" },
                techFeasibility: { type: Type.NUMBER, description: "Score 1-10 based on Ease/Dependencies" },
                source: { type: Type.STRING, description: "Citation, e.g. 'FY23 10-K'" }
              },
              required: ["id", "name", "description", "businessValue", "techFeasibility", "source"]
            }
          }
        },
        required: ["id", "name", "timeframe", "initiatives"]
      },
      description: "STRICTLY exactly 3 execution phases (e.g. Stabilization, Optimization, Transformation)."
    },
    kpis: {
      type: Type.ARRAY,
      items: {
        type: Type.OBJECT,
        properties: {
          metric: { type: Type.STRING, description: "The Objective or Metric Name" },
          target: { type: Type.STRING, description: "The desired future value" },
          baseline: { type: Type.STRING, description: "The current or starting value" }
        },
        required: ["metric", "target", "baseline"]
      },
      description: "Provide at least 3-6 KPIs to ensure coverage across phases."
    },
    impactedTeams: {
      type: Type.ARRAY,
      items: { type: Type.STRING },
      description: "List of Business Units, Departments, or Roles accountable. STRICTLY DO NOT use specific individual names. Provide at least 3-6 teams to ensure coverage across phases. Format: 'Team Name/Business Unit - Role/Impact'"
    }
  },
  required: ["companyName", "ticker", "vision", "focusAreas", "phases", "kpis", "impactedTeams"]
};

export const generateStrategy = async (ticker: string): Promise<StrategyData> => {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

  const researchPrompt = `
    Conduct a deep strategic analysis for public company ${ticker}.
    
    CRITICAL: You must analyze a minimum of the last 8 quarters of financial documents and reports.
    Include:
    - Latest 10-K and 10-Q filings.
    - Transcripts from the last 8 Earnings Calls.
    - Recent Analyst Reports and Investor Presentations.

    Gather specific evidence to answer these questions:
    1. Vision & Purpose: 
       - Find the official published mission statement.
       - Identify the long-term aspiration, the core problem being solved, and the desired future state.
    2. Strategic Pillars: What are the 3-5 top themes or "must-win" battles? What are the specific challenges in these areas?
    3. Execution Plan: What are the major "jobs to be done"? Are there clear phases or sequencing (e.g., "stabilize first, then scale")?
    4. Metrics: Find specific numbers. What are the Baseline metrics (current state) and Target metrics (future goals)? Look for revenue targets, margin goals, customer counts, or operational efficiency stats.
    5. Teams: Which specific business units or departments are accountable for these changes? Avoid listing individual executive names.
    
    Provide a detailed summary containing citations.
  `;

  let researchSummary = "";
  let sources: { title: string; url: string }[] = [];

  try {
    const researchResponse = await ai.models.generateContent({
      model: "gemini-3-pro-preview",
      contents: researchPrompt,
      config: {
        tools: [{ googleSearch: {} }],
      },
    });

    researchSummary = researchResponse.text || "";
    
    if (researchResponse.candidates?.[0]?.groundingMetadata?.groundingChunks) {
      const chunks = researchResponse.candidates[0].groundingMetadata.groundingChunks;
      const uniqueUrls = new Set<string>();
      
      chunks.forEach((chunk: any) => {
        if (chunk.web?.uri && chunk.web?.title) {
          if (!uniqueUrls.has(chunk.web.uri)) {
            uniqueUrls.add(chunk.web.uri);
            sources.push({ title: chunk.web.title, url: chunk.web.uri });
          }
        }
      });
    }
  } catch (e) {
    console.warn("Search step failed, proceeding with internal knowledge", e);
    researchSummary = `Generate strategy for ${ticker} based on internal knowledge.`;
  }

  const synthesisPrompt = `
    Act as a senior MBB strategy consultant. Use the Research Data below to build a "Strategy House" for ${ticker}.
    
    Research Data:
    ${researchSummary}
    
    You must follow this specific 5-Section Framework for your thinking process before generating the JSON:

    --- FRAMEWORK START ---
    Section 1: Vision (The Roof) 
    Section 2: Strategy & Business Focus Areas (The Pillars)
    Section 3: Prioritization (The Phases)
    Section 4: Measure Success (OKRs/KPIs)
    Section 5: Impacted Teams
    --- FRAMEWORK END ---

    Task:
    Map your analysis from the framework above into the following JSON schema.
  `;

  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-pro-preview",
      contents: synthesisPrompt,
      config: {
        responseMimeType: "application/json",
        responseSchema: strategySchema,
        thinkingConfig: { thinkingBudget: 32768 },
      },
    });

    if (response.text) {
      const data = JSON.parse(response.text) as StrategyData;
      data.researchSources = sources;
      return data;
    }
    throw new Error("No text response from model");
  } catch (error) {
    console.error("Gemini Generation Error:", error);
    throw error;
  }
};

export const refineStrategy = async (
  currentStrategy: StrategyData, 
  userInstruction: string
): Promise<{ updatedStrategy: StrategyData; explanation: string }> => {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

  const prompt = `
    You are the delta AI Strategist. 
    Current Data (JSON): ${JSON.stringify(currentStrategy)}
    User Instruction: "${userInstruction}"
    Task: Update the JSON data based on the user's instruction.
  `;

  const refineSchema: Schema = {
    type: Type.OBJECT,
    properties: {
      updatedStrategy: strategySchema,
      explanation: { type: Type.STRING }
    },
    required: ["updatedStrategy", "explanation"]
  };

  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview", 
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseSchema: refineSchema
      },
    });

    if (response.text) {
      return JSON.parse(response.text) as { updatedStrategy: StrategyData; explanation: string };
    }
    throw new Error("No text response from model during refinement");
  } catch (error) {
    console.error("Gemini Refinement Error:", error);
    throw error;
  }
};

export const generateDeepDive = async (
  ticker: string,
  itemTitle: string,
  itemDescription: string
): Promise<AnalysisResult> => {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

  const prompt = `
    Analyze the following strategic element for ${ticker} in depth.
    Item: "${itemTitle}"
    Context/Description: "${itemDescription}"
  `;

  const analysisSchema: Schema = {
    type: Type.OBJECT,
    properties: {
      title: { type: Type.STRING },
      rationale: { type: Type.STRING },
      evidence: { type: Type.ARRAY, items: { type: Type.STRING } },
      citations: { type: Type.ARRAY, items: { type: Type.STRING } }
    },
    required: ["title", "rationale", "evidence", "citations"]
  };

  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-pro-preview",
      contents: prompt,
      config: {
        tools: [{ googleSearch: {} }],
        responseMimeType: "application/json",
        responseSchema: analysisSchema
      },
    });

    if (response.text) {
      return JSON.parse(response.text) as AnalysisResult;
    }
    throw new Error("No analysis generated");
  } catch (error) {
    console.error("Deep Dive Error:", error);
    throw error;
  }
};
