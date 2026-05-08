# ThinWallType Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ThinWallType`

Gets or sets the thin wall type for a thin base extrude feature.
Gets or sets the thin wall type for a thin base extrude feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThinWallType As System.Integer
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Integer
 
instance.ThinWallType = value
 
value = instance.ThinWallType
```

```

System.int ThinWallType {get; set;}
```

```

property System.int ThinWallType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thin feature type:

- 0 = One Direction
- 1 = One Direction Reverse
- 2 = Mid Plane
- 3 = Two Direction

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.md)  
[IExtrudeFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.md)  
[IExtrudeFeatureData2::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetWallThickness.md)  
[IExtrudeFeatureData2::CapEnds Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.md)  
[IExtrudeFeatureData2::CapThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.md)
