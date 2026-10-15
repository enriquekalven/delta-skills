import { GoogleGenAI, Type, Schema } from "@google/genai";

export interface Initiative {
  id: string;
  name: string;
  description: string;
  businessValue: number;
  techFeasibility: number;
  source: string;
}

export interface StrategyPhase {
  id: string;
  name: string;
  timeframe: string;
  initiatives: Initiative[];
}

export interface StrategyKpi {
  metric: string;
  target: string;
  baseline: string;
}

export interface StrategyData {
  companyName: string;
  ticker: string;
  vision: string;
  focusAreas: string[];
  phases: StrategyPhase[];
  kpis: StrategyKpi[];
  impactedTeams: string[];
  researchSources?: { title: string; url: string }[];
}

export interface AnalysisResult {
  title: string;
  rationale: string;
  evidence: string[];
  citations: string[];
}

export const strategySchema: Schema = {
  type: Type.OBJECT,
  properties: {
    companyName: { type: Type.STRING },
    ticker: { type: Type.STRING },
    vision: {
      type: Type.STRING,
      description:
        "A cohesive 2-3 sentence paragraph combining Mission, Aspiration, and Future State grounded in filings.",
    },
    focusAreas: {
      type: Type.ARRAY,
      items: { type: Type.STRING },
      description: "Between 3 and 5 strategic pillars formatted as 'Area Name: Core problem and target outcome'.",
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
                source: { type: Type.STRING, description: "Filing citation, e.g. 'FY25 10-K, Item 7, p. 42'" },
              },
              required: ["id", "name", "description", "businessValue", "techFeasibility", "source"],
            },
          },
        },
        required: ["id", "name", "timeframe", "initiatives"],
      },
      description: "Exactly 3 execution phases (Horizon 1 Stabilization, Horizon 2 Optimization, Horizon 3 Transformation).",
    },
    kpis: {
      type: Type.ARRAY,
      items: {
        type: Type.OBJECT,
        properties: {
          metric: { type: Type.STRING, description: "Objective or metric name" },
          target: { type: Type.STRING, description: "Desired target value" },
          baseline: { type: Type.STRING, description: "Verified current baseline value from filings" },
        },
        required: ["metric", "target", "baseline"],
      },
      description: "3-6 quantitative KPIs with verified baselines and targets.",
    },
    impactedTeams: {
      type: Type.ARRAY,
      items: { type: Type.STRING },
      description: "3-6 Business Units or Functions accountable (no individual person names). Format: 'Team - Role/Impact'.",
    },
  },
  required: ["companyName", "ticker", "vision", "focusAreas", "phases", "kpis", "impactedTeams"],
};

export const generateStrategy = async (ticker: string): Promise<StrategyData> => {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

  const researchPrompt = `
    Conduct a grounded strategic analysis for public company ${ticker} using its latest 10-K, 10-Q, and earnings call transcripts.
    Extract with exact filing citations:
    1. Vision & long-term financial targets.
    2. 3-5 strategic pillars and stated operational bottlenecks.
    3. Phased initiatives and capital allocation priorities.
    4. Baseline metrics and stated target KPIs.
    5. Accountable business units or functional teams (no individual names).
  `;

  const researchResponse = await ai.models.generateContent({
    model: "gemini-2.5-pro",
    contents: researchPrompt,
    config: {
      tools: [{ googleSearch: {} }],
    },
  });

  const researchSummary = researchResponse.text || "";
  if (!researchSummary.trim()) {
    throw new Error(`Grounded search returned empty research summary for ${ticker}; refusing to synthesize ungrounded strategy.`);
  }

  const sources: { title: string; url: string }[] = [];
  const chunks = researchResponse.candidates?.[0]?.groundingMetadata?.groundingChunks || [];
  const uniqueUrls = new Set<string>();
  for (const chunk of chunks as Array<{ web?: { uri?: string; title?: string } }>) {
    if (chunk.web?.uri && chunk.web?.title && !uniqueUrls.has(chunk.web.uri)) {
      uniqueUrls.add(chunk.web.uri);
      sources.push({ title: chunk.web.title, url: chunk.web.uri });
    }
  }

  const synthesisResponse = await ai.models.generateContent({
    model: "gemini-2.5-pro",
    contents: `Map the following grounded research for ${ticker} into the Strategy House JSON schema. Do not invent metrics absent from the research.\n\n${researchSummary}`,
    config: {
      responseMimeType: "application/json",
      responseSchema: strategySchema,
    },
  });

  if (!synthesisResponse.text) {
    throw new Error("No JSON response returned from model");
  }
  const data = JSON.parse(synthesisResponse.text) as StrategyData;
  data.researchSources = sources;
  return data;
};
