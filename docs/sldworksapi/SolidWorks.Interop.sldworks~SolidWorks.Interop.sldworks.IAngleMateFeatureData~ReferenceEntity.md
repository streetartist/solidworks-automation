# ReferenceEntity Property (IAngleMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~ReferenceEntity`

Gets or sets the direction reference entity for this angle mate.
Gets or sets the direction reference entity for this angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferenceEntity As System.Object
```

```

Dim instance As IAngleMateFeatureData
Dim value As System.Object
 
instance.ReferenceEntity = value
 
value = instance.ReferenceEntity
```

```

System.object ReferenceEntity {get; set;}
```

```

property System.Object^ ReferenceEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or reference [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md)  
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.md)
