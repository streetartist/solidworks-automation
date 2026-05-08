# NormalToFlangePlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~NormalToFlangePlane`

Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange.
Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NormalToFlangePlane As System.Boolean
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean
 
instance.NormalToFlangePlane = value
 
value = instance.NormalToFlangePlane
```

```

System.bool NormalToFlangePlane {get; set;}
```

```

property System.bool NormalToFlangePlane {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the Up To Vertex is on a plane that is normal to the end face of the edge flange (default), false if the Up To Vertex passes through a plane that is parallel to the face of the base flange

Remarks

This property is valid only if [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.md) is set to [swFlangeOffsetTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetUpToVertex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)
