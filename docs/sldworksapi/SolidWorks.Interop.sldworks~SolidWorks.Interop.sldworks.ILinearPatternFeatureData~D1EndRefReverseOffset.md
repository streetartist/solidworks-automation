# D1EndRefReverseOffset Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefReverseOffset`

Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature.
Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1EndRefReverseOffset As System.Boolean
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean
 
instance.D1EndRefReverseOffset = value
 
value = instance.D1EndRefReverseOffset
```

```

System.bool D1EndRefReverseOffset {get; set;}
```

```

property System.bool D1EndRefReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse [ILinearPatternFeatureData::D1EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefOffset.md) from [ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.md), false to not

Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.md) is set to [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_UpToReference.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)
