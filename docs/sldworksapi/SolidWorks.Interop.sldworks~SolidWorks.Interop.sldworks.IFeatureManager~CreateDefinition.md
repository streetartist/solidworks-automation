# CreateDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition`

Creates a feature data object of the specified type.
Creates a feature data object of the specified type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDefinition( _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.CreateDefinition(Type)
```

```

System.object CreateDefinition( 
   System.int Type
)
```

```

System.Object^ CreateDefinition( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Feature name ID as defined in [swFeatureNameID\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html):

    - swFmBaseFlange (sheet metal base flange)
    - swFmBeltAndChain (belt/chain)
    - swFmBoundingBox (bounding box)
    - swFmCirPattern (circular pattern)
    - swFmCornerRelief (sheet metal corner relief)
    - swFmCurvePattern (curve-driven pattern)
    - swFmDerivedLPattern (derived-driven pattern)
    - swFmDimPattern (variable/dimension pattern)
    - swFmEdgeFlange (sheet metal edge flange)
    - swFmFillet (constant radius, face, full round fillet/chamfer)
    - swFmFillPattern (fill pattern)
    - swFmFormToolInstance (library form tool)
    - swFmGroundPlane (ground plane)
    - swFmLibraryFeature (library)
    - swFmLocalChainPattern (chain component pattern)
    - swFmLocalCirPattern (circular component pattern)
    - swFmLocalCurvePattern (curve-driven component pattern)
    - swFmLocalLPattern (linear component pattern)
    - swFmLocalSketchPattern (sketch-driven component pattern)
    - swFmLPattern (linear pattern)
    - swFmMateController (mate controller)
    - swFmMirrorComponent (mirror components)
    - swFmNormalCut (sheet metal normal cut)
    - swFmRefCurve (projection curve)
    - swFmRefSurface (surface sweep)
    - swFmSketchBend (sheet metal sketched bend)
    - swFmSketchPattern (sketch-driven pattern)
    - swFmSMGusset (sheet metal gusset)
    - swFmSolidToSheetMetal (convert solid to sheet metal)
    - swFmSweep (boss sweep)
    - swFmSweepCut (cut sweep)
    - swFmSweepThread (sweep thread)
    - swFmSweptFlange (sheet metal swept flange)
    - swFmTabAndSlot (tab and slot)
    - swFmTablePattern (table pattern)

#### Return Value

[thread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md), [sweep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md), [library](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md), [library form tool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md), [tab and slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.md), [bounding box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md), [ground plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md), [mirror components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md), [projection curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md), [sheet metal normal cut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md), [sheet metal swept flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md), [sheet metal gusset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md), [sheet metal edge flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md), [convert solid to sheet metal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md), [simple fillet/chamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md), [belt/chain](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md), [sheet metal base flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md), [sheet metal corner relief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md), [sheet metal sketched bend](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md), [mate controller](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md), or pattern-specific feature data object (see **Remarks**); Nothing or null otherwise

Remarks

This method initializes the feature data objects with default data for pattern, sweep, bounding box, ground plane, mirror components, projection curve, sheet metal normal cut, sheet metal swept flange, sheet metal gusset, sheet metal edge flange, tab/slot, library form tool, and belt/chain features.

For sheet metal base flange, sheet metal corner relief, convert solid to sheet metal, library, simple fillet, and thread features, you must initialize feature data objects using specific initialize methods.

For mate controller features, you can either pre-select mates before calling this method or initialize the feature data object returned by this method with default values.

See the **See Also** section.

For additional information, see:

- [Library Features and LibraryFeatureData Objects](sldworksAPIProgGuide.chm::/OVERVIEW/Library_Features_and_LibraryFeatureData_Objects.htm)
- [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm)
- [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm)
- [Thread Features and ThreadFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Thread_Features_and_ThreadFeatureData_Objects.htm)

Example

See examples for:

[IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)

[IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)

[ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)

[IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)

[IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)

[IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)

[IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)

[ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)

[ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)

[ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)

[ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)

[ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.md)

Example

[Create a Thread Feature (VBA)](Create_a_Thread_Feature_Example_VB.htm)  
[Create a Thread Feature (VB.NET)](Create_a_Thread_Feature_Example_VBNET.htm)  
[Create a Thread Feature (C#)](Create_a_Thread_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md)  
[IFeature::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md)  
[IFeatureManager::CreateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md)  
[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.md)  
[IThreadFeatureData::InitializeThreadData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~InitializeThreadData.md)  
[ISimpleFilletFeatureData2::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.md)  
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.md)  
[ICornerReliefFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize.md)  
[IMateControllerFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.md)  
[IConvertSolidFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize.md)
