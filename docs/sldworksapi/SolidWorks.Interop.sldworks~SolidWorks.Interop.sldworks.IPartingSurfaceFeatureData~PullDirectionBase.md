# PullDirectionBase Property (IPartingSurfaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionBase`

Gets or sets the entity that defines the direction of pull for this parting surface feature.
Gets or sets the entity that defines the direction of pull for this parting surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PullDirectionBase As System.Object
```

```

Dim instance As IPartingSurfaceFeatureData
Dim value As System.Object
 
instance.PullDirectionBase = value
 
value = instance.PullDirectionBase
```

```

System.object PullDirectionBase {get; set;}
```

```

property System.Object^ PullDirectionBase {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.md)  
[IPartingSurfaceFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionType.md)
