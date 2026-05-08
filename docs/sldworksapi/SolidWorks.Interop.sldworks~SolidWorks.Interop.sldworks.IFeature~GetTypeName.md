# GetTypeName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName`

Gets the type of feature.
Gets the type of feature.

**NOTE:** To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTypeName() As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
value = instance.GetTypeName()
```

```

System.string GetTypeName()
```

```

System.String^ GetTypeName(); 
```

#### Return Value

String identifying the type of feature (see **Remarks**)

Remarks

Use [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get a feature data object (i.e., an object whose interface name ends in FeatureData or FeatureData2, such as ISymmetricMateFeatureData, IExtrudeFeatureData2, ILoftFeatureData, ISimpleFilletFeatureData2, IChamferFeatureData2, etc.); otherwise, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get an object for a feature.

| Type of feature | String returned by this method | Interface |
| --- | --- | --- |
| **Assembly** | AsmExploder | None (Assembly exploded view in ConfigurationManager) |
|  | CompExplodeStep | None (Explode step in assembly exploded view) |
|  | ExplodeLineProfileFeature | [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) |
|  | InContextFeatHolder | [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) |
|  | MagneticGroundPlane | [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) |
|  | MateCamTangent | [ICamFollowerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.md) |
|  | MateCoincident | [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md) |
|  | MateConcentric | [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md) |
|  | MateDistanceDim | [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md) |
|  | MateGearDim | [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md) |
|  | MateHinge | [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md) |
|  | MateInPlace | [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md) |
|  | MateLimitDistanceDim | [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md) |
|  | MateLinearCoupler | [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md) |
|  | MateLock | [ILockMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.md) |
|  | MateParallel | [IParallelMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.md) |
|  | MatePerpendicular | [IPerpendicularMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData.md) |
|  | MatePlanarAngleDim | [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md) |
|  | MateProfileCenter | [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.md) |
|  | MateRackPinionDim | [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md) |
|  | MateScrew | [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md) |
|  | MateSlot | [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md) |
|  | MateSymmetric | [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md) |
|  | MateTangent | [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.md) |
|  | MateUniversalJoint | [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.md) |
|  | MateWidth | [IWidthMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md) |
|  | PosGroupFolder | [IMateReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md) |
|  | Reference | [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) |
|  | ReferencePattern | [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) |
|  | SmartComponentFeature | [ISmartComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md) |
| **Body** | AdvHoleWzd | [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md) |
|  | APattern | [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) |
|  | BaseBody | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | Bending | None (**Flex** feature) |
|  | Blend | [ILoftFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md) |
|  | BlendCut | [ILoftFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md) |
|  | BodyExplodeStep | None (Explode step of multi-body part exploded view) |
|  | Boss | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | BossThin | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | Chamfer | [IChamferFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md) |
|  | CirPattern | [ICircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md) |
|  | CombineBodies | [ICombineBodiesFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md) |
|  | CosmeticThread | [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) |
|  | CosmeticWeldBead | [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) |
|  | CreateAssemFeat | [ISaveBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md) |
|  | CurvePattern | [ICurveDrivenPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md) |
|  | Cut | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | CutThin | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | Deform | None (**Deform** feature) |
|  | DeleteBody | [IDeleteBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md) |
|  | DelFace | [IDeleteFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md) |
|  | DerivedCirPattern | [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md) |
|  | DerivedHolePattern | [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md) |
|  | DerivedLPattern | [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md) |
|  | DimPattern | [IDimPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md) |
|  | Dome | [IDomeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md) |
|  | Draft | [IDraftFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md) |
|  | EdgeMerge | [IHealEdgesFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.md) |
|  | Emboss | [IWrapSketchFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.md) |
|  | Extrusion | [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md) |
|  | Fillet | [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) |
|  | Helix | [IHelixFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md) |
|  | HoleSeries | [IHoleSeriesFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md) |
|  | HoleWzd | [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md) |
|  | Imported | None (**Imported** feature) |
|  | LocalChainPattern | [IChainPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md) |
|  | LocalCirPattern | [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md) |
|  | LocalCurvePattern | [ILocalCurvePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md) |
|  | LocalLPattern | [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md) |
|  | LocalSketchPattern | [ILocalSketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md) |
|  | LPattern | [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md) |
|  | MacroFeature | [IMacroFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md) |
|  | MirrorCompFeat | [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) |
|  | MirrorPattern | [IMirrorPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md) |
|  | MirrorSolid | [IMirrorSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.md) |
|  | MirrorStock | [IMirrorPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md) |
|  | MoveCopyBody | [IMoveCopyBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md) |
|  | NetBlend | [IBoundaryBossFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md) |
|  | PrtExploder | None (Multi-body part exploded view) |
|  | Punch | [IIndentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md) |
|  | ReplaceFace | [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md) |
|  | RevCut | [IRevolveFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md) |
|  | Revolution | [IRevolveFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md) |
|  | RevolutionThin | [IRevolveFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md) |
|  | Rib | [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) |
|  | Rip | [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md) |
|  | Round fillet corner | [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) |
|  | Sculpt | [IIntersectFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md) |
|  | Shape | Obsolete |
|  | Shell | [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md) |
|  | SketchHole | [ISimpleHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md) |
|  | SketchPattern | [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md) |
|  | Split | [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md) for a feature that was created by splitting a part into multiple parts using either [IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md) or the **Split** feature in the user interface |
|  | SplitBody | None; returned for a body created by splitting a part and saving the body to a part; you cannot access the data of a split body saved to a part |
|  | Stock | [IDerivedPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md) |
|  | Sweep | [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) |
|  | SweepCut | [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) |
|  | SweepThread | [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) |
|  | TablePattern | [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md) |
|  | Thicken | [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md) |
|  | ThickenCut | [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md) |
|  | VarFillet | [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md) |
| **Drawing** | BendTableAchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | BomFeat | [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) |
|  | BomTemplate | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | DetailCircle | [IDetailCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md) |
|  | DrBreakoutSectionLine | [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) or [IBrokenOutSectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md) |
|  | DrSectionLine | [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) |
|  | GeneralTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | HoleTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | LiveSection | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) |
|  | PunchTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | RevisionTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | WeldmentTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
|  | WeldTableAnchor | [ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md) |
| **Folder** | BlockFolder | Obsolete |
|  | CommentsFolder | [ICommentFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md) |
|  | CosmeticWeldSubFolder | [ICosmeticWeldBeadFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.md) |
|  | CutListFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | FeatSolidBodyFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | FeatSurfaceBodyFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | FtrFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | InsertedFeatureFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | MateReferenceGroupFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | ProfileFtrFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | RefAxisFtrFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | RefPlaneFtrFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | SketchSliceFolder | [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) |
|  | SolidBodyFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | SubAtomFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) if a body |
|  | SubWeldFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | SurfaceBodyFolder | [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) |
|  | TemplateFlatPattern | [IFlatPatternFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder.md) |
| **Imported File** | MBimport | [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) |
| **Miscellaneous** | Attribute | [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) |
|  | BlockDef | Obsolete |
|  | CurveInFile | [IFreePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.md) |
|  | GridFeature | None (**Grid** feature) |
|  | LibraryFeature | [ILibraryFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md) |
|  | Scale | [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) |
|  | Sensor | [ISensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md) |
|  | ViewBodyFeature | Obsolete |
| **Mold** | Cavity | [ICavityFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md) |
|  | MoldCoreCavitySolids | [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) |
|  | MoldPartingGeom | [IPartingSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md) |
|  | MoldPartLine | [IPartingLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md) |
|  | MoldShutOffSrf | [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md) |
|  | SideCore | [ICoreFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md) |
|  | XformStock | [DerivedPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md) |
| **Motion and Simulation** | AEM3DContact | [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) |
|  | AEMGravity | [ISimulationGravityFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.md) |
|  | AEMLinearDamper | [ISimulationDamperFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md) |
|  | AEMLinearMotor | [ISimulationMotorFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md) |
|  | AEMLinearSpring | [ISimulationLinearSpringFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.md) |
|  | AEMRotationalMotor | [ISimulationMotorFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md) |
|  | AEMTorque | [ISimulationForceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md) |
|  | AEMTorsionalDamper | [ISimulationDamperFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md) |
|  | AEMTorsionalSpring | None (**TorsionalSpring** feature) |
|  | SimPlotFeature | [IMotionPlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.md) |
|  | SimPlotXAxisFeature | [IMotionPlotAxisFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.md) |
|  | SimPlotYAxisFeature | [IMotionPlotAxisFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.md) |
|  | SimResultFolder | [IMotionStudyResults](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.md) |
| **Reference Geometry** | BoundingBox | [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md) |
|  | CenterOfMass | [ICenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass.md) |
|  | CoordSys | [ICoordinateSystemFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.md) |
|  | GroundPlane | [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md) |
|  | RefAxis | [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) or [IRefAxisFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) |
|  | RefPlane | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or [IRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) |
| **Scenes, Lights, and Cameras** | AmbientLight | [ILight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md) |
|  | CameraFeature | [ICamera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md) |
|  | DirectionLight | [ILight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md) |
|  | PointLight | [ILight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md) |
|  | SpotLight | [ILight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md) |
| **Sheet Metal** | SMBaseFlange | [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) |
|  | BreakCorner | [IBreakCornerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md) |
|  | CornerTrim | [IBreakCornerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md) |
|  | CrossBreak | [ICrossBreakFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.md) |
|  | EdgeFlange | [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md) |
|  | FlatPattern | [IFlatPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md) |
|  | FlattenBends | [IBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md) |
|  | Fold | [IFoldsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.md) |
|  | FormToolInstance | None (**FormTool** feature) |
|  | Hem | [IHemFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md) |
|  | Jog | [IJogFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md) |
|  | LoftedBend | [ILoftedBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md) |
|  | Normal Cut | [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) |
|  | OneBend | [IOneBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md) |
|  | ProcessBends | [IBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md) |
|  | SheetMetal | [ISheetMetalFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md) |
|  | SketchBend | [IOneBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md) |
|  | SM3dBend | [ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md) |
|  | SMGusset | [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) |
|  | SMMiteredFlange | [IMiterFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md) |
|  | SolidToSheetMetal | [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) |
|  | TemplateSheetMetal | [ISheetMetalFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder.md) |
|  | ToroidalBend | [IOneBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md) |
|  | UnFold | [IFoldsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.md) |
| **Sketch** | 3DProfileFeature | [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) |
|  | 3DSplineCurve | [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md) or [IReferencePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.md) |
|  | CompositeCurve | [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md) or [ICompositeCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md) |
|  | ImportedCurve | [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md) or [IImportedCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.md) |
|  | PLine | [ISplitLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md) |
|  | ProfileFeature | [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) |
|  | RefCurve | [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md) or [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md) |
|  | RefPoint | [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md) or [IRefPointFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md) |
|  | SketchBlockDef | [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) |
|  | SketchBlockInst | [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) |
|  | SketchBitmap | [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) |
| **Surface** | BlendRefSurface | None (**Surface-Loft** feature) |
|  | ExtendRefSurface | [ISurfaceExtendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md) |
|  | ExtruRefSurface | [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) |
|  | FillRefSurface | [IFillSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md) |
|  | FlattenSurface | [ISurfaceFlattenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md) |
|  | MidRefSurface | [IMidSurface3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md) |
|  | OffsetRefSuface | [ISurfaceOffsetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.md) |
|  | PlanarSurface | [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md) |
|  | RadiateRefSurface | [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md) |
|  | RefSurface | None (**Surface-Imported** feature) |
|  | RevolvRefSurf | [ISurfRevolveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.md) |
|  | RuledSrfFromEdge | [IRuledSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md) |
|  | SewRefSurface | [ISurfaceKnitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md) |
|  | SurfCut | [ISurfaceCutFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md) |
|  | SweepRefSurface | [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) |
|  | TrimRefSurface | [ISurfaceTrimFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md) |
|  | UnTrimRefSurf | None (**Surface-Untrim** feature) |
| **Weldment and Structure System** | EndCap | [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) |
|  | StrctSysBtwPtsMbrFeat | [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) |
|  | StrctSysCnrFeat | [ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md) |
|  | StrctSysCnrGrpFeat | [ICornerTreatmentGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder.md) |
|  | StrctSysCnrMgmtFeat | [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) |
|  | StrctSysFeat | [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md) |
|  | StrctSysGrpFeat | [IProfileGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.md) |
|  | StrctSysPathSegMbrFeat | [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) |
|  | StrctSysPtToMem | [ISecondaryMemberUpToMembersFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md) |
|  | StrctSysRefPlnMbrFeat | [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) |
|  | StrctSysSkPtLenMbrFeat | [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) |
|  | StrctSysSupPlnMbrFeat | [ISecondaryMemberSupportPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.md) |
|  | StrctSysSurfPlnMbrFeat | [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) |
|  | AdvStructMember | [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md) |
|  | Gusset | [IGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md) |
|  | WeldBeadFeat | [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) |
|  | WeldCornerFeat | [IWeldmentTrimExtendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md) |
|  | WeldMemberFeat | [IStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md) |
|  | WeldmentFeature | [IStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md) |
|  | WeldmentTableFeat | [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md) |

**NOTE:** This method returns strings for some features shown in the FeatureManager design (e.g., **MateGroup**, **Weldment**, etc.) that set up the design functionality environment and, thus, do not have interfaces.

Example

[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)  
[Select Origin of Assembly Component (VBA)](Select_Origin_of_Assembly_Component_Example_VB.htm)  
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)  
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)  
[Traverse Assembly at Component and Feature Level (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)  
[Get Info on Plane-Axis (C++)](Get_Info_on_Plane_Axis_Example_CPlusPlus_COM.htm)  
[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)  
[Get Selected Feature (C++)](Get_Selected_Feature_Example_CPlusPlus_COM.htm)  
[Get Type of Instant3D Feature (C#)](Get_Type_of_Instant3D_Feature_Example_CSharp.htm)  
[Get Type of Instant3D Feature (VB.NET)](Get_Type_of_Instant3D_Feature_Example_VBNET.htm)  
[Get Type of Instant3D Feature (VBA)](Get_Type_of_Instant3D_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md)  
[IFeature::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md)
