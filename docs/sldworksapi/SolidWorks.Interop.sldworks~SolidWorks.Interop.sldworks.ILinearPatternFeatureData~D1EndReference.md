# D1EndReference Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference`

Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature.
Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1EndReference As System.Object
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Object
 
instance.D1EndReference = value
 
value = instance.D1EndReference
```

```

System.object D1EndReference {get; set;}
```

```

property System.Object^ D1EndReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pattern's up-to reference geometry ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)) in Direction 1

Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.md) is set to [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_UpToReference.

To control the pattern in Direction 1, also set:

- ILinearPatternFeatureData::D1Axis
- ILinearPatternFeatureData::D1EndRefOffset
- ILinearPatternFeatureData::D1EndRefReverseOffset
- ILinearPatternFeatureData::D1EndUseSeedReference
  - ILinearPatternFeatureData::D1EndSeedReference (if D1EndUseSeedReference is true)
- ILinearPatternFeatureData::D1EndUseSpacing
  - ILinearPatternFeatureData::D1Spacing (if D1EndUseSpacing is true)
  - ILinearPatternFeatureData::D1TotalInstances (if D1EndUseSpacing is false)

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)
