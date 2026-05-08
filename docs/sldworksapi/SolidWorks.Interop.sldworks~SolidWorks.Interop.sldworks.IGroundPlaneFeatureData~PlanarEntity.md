# PlanarEntity Property (IGroundPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~PlanarEntity`

Gets or sets the planar entity for this ground plane feature.
Gets or sets the planar entity for this ground plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PlanarEntity As System.Object
```

```

Dim instance As IGroundPlaneFeatureData
Dim value As System.Object
 
instance.PlanarEntity = value
 
value = instance.PlanarEntity
```

```

System.object PlanarEntity {get; set;}
```

```

property System.Object^ PlanarEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Example

See the [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md)  
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.md)
