# OffsetPlaneReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OffsetPlaneReference`

Gets or sets the offset plane reference for the Normal Cut.
Gets or sets the offset plane reference for the Normal Cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetPlaneReference As System.Object
```

```

Dim instance As ISMNormalCutFeatureData2
Dim value As System.Object
 
instance.OffsetPlaneReference = value
 
value = instance.OffsetPlaneReference
```

```

System.object OffsetPlaneReference {get; set;}
```

```

property System.Object^ OffsetPlaneReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or top or bottom [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of the sheet metal body

Remarks

This property is valid only if [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.md) is set to [swNormalCutParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
