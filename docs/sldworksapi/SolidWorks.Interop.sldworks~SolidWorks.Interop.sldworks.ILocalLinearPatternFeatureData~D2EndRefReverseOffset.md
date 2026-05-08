# D2EndRefReverseOffset Property (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndRefReverseOffset`

Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear component pattern feature.
Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2EndRefReverseOffset As System.Boolean
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean
 
instance.D2EndRefReverseOffset = value
 
value = instance.D2EndRefReverseOffset
```

```

System.bool D2EndRefReverseOffset {get; set;}
```

```

property System.bool D2EndRefReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse [ILocalLinearPatternFeatureData::D2EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndRefOffset.md) from [ILocalLinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndReference.md), false to not

Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndCondition.md) is set to [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_UpToReference.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
