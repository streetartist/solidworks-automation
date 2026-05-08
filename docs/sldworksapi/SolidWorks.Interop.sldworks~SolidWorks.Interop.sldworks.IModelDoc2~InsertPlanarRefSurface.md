# InsertPlanarRefSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertPlanarRefSurface`

Inserts a planar reference surface.
Inserts a planar reference surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPlanarRefSurface() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.InsertPlanarRefSurface()
```

```

System.bool InsertPlanarRefSurface()
```

```

System.bool InsertPlanarRefSurface(); 
```

#### Return Value

True if the reference surface is created, false if not

Remarks

Before calling this method, select the surface's boundary entities using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Marks of 1. See the SOLIDWORKS Help for more information about what entities are valid for selection.

Example

[Create Planar Surface Feature (VBA)](Create_Planar_Surface_Feature_Example_VB.htm)  
[Create Planar Surface Feature (VB.NET)](Create_Planar_Surface_Feature_Example_VBNET.htm)  
[Create Planar Surface Feature (C#)](Create_Planar_Surface_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md)
