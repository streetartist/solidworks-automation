# CutDirection Property (ISMNormalCutFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CutDirection`

Gets or sets the edge, linear curve, or planar face that defines the direction of the Normal Cut.
Gets or sets the edge, linear curve, or planar face that defines the direction of the Normal Cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CutDirection As System.Object
```

```

Dim instance As ISMNormalCutFeatureData2
Dim value As System.Object
 
instance.CutDirection = value
 
value = instance.CutDirection
```

```

System.object CutDirection {get; set;}
```

```

property System.Object^ CutDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md), or [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that defines the direction of the Normal Cut

Example

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
