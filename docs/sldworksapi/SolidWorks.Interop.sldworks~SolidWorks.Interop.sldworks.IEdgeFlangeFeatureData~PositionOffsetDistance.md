# PositionOffsetDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance`

Gets or sets the flange position offset for this edge flange.
Gets or sets the flange position offset for this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PositionOffsetDistance As System.Double
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double
 
instance.PositionOffsetDistance = value
 
value = instance.PositionOffsetDistance
```

```

System.double PositionOffsetDistance {get; set;}
```

```

property System.double PositionOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Flange position offset value; default value is 0.01 m

Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.md) is set to true,

    - and -

- [IEdgeflangeFeatureData::PostionOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.md) is set to either [swFlangeOffsetTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetFromSurface or swFlangeOffsetTypes\_e.swFlangeOffsetBlind.

Example

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::PositionOffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference.md)  
[IEdgeFlangeFeatureData::ReversePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.md)
