# PositionOffsetReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference`

Gets or sets the flange position offset reference for this edge flange.
Gets or sets the flange position offset reference for this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PositionOffsetReference As System.Object
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object
 
instance.PositionOffsetReference = value
 
value = instance.PositionOffsetReference
```

```

System.object PositionOffsetReference {get; set;}
```

```

property System.Object^ PositionOffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Flange position offset reference for this edge flange

Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.md) is set to true,

  - and -

- [IEdgeFlangeFeatureData::PositionOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.md) is set to [swFlangeOffsetTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).:
  - swFlangeOffsetUpToVertex
  - swFlangeOffsetUpToSurface
  - swFlangeOffsetFromSurface

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::PositionOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance.md)  
[IEdgeFlangeFeatureData::ReversePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.md)
