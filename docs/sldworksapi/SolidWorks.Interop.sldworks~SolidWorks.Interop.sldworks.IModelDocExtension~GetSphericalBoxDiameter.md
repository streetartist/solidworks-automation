# GetSphericalBoxDiameter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSphericalBoxDiameter`

Gets the diameter of the spherical bounding box of this model.
Gets the diameter of the spherical bounding box of this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSphericalBoxDiameter() As System.Double
```

```

Dim instance As IModelDocExtension
Dim value As System.Double
 
value = instance.GetSphericalBoxDiameter()
```

```

System.double GetSphericalBoxDiameter()
```

```

System.double GetSphericalBoxDiameter(); 
```

#### Return Value

Diameter of the sphere that encloses this model's bounding box

Example

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
