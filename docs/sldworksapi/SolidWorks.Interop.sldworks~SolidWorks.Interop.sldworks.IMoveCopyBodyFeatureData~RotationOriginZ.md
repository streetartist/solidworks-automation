# RotationOriginZ Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginZ`

Gets or sets the z coordinate for the origin about which to rotate the selected bodies.
Gets or sets the z coordinate for the origin about which to rotate the selected bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationOriginZ As System.Double
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double
 
instance.RotationOriginZ = value
 
value = instance.RotationOriginZ
```

```

System.double RotationOriginZ {get; set;}
```

```

property System.double RotationOriginZ {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

z coordinate

Remarks

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.md) must be NULL.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::RotationOriginX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginX.md)  
[IMoveCopyBodyFeatureData::RotationOriginY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginY.md)
