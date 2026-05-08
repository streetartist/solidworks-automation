# CreatePlanarTrimSurfaceDLL Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL`

Creates a planar trim surface for this body.
Creates a planar trim surface for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePlanarTrimSurfaceDLL( _
   ByVal Points As System.Object, _
   ByVal Normal As System.Object _
) As System.Boolean
```

```

Dim instance As IBody2
Dim Points As System.Object
Dim Normal As System.Object
Dim value As System.Boolean
 
value = instance.CreatePlanarTrimSurfaceDLL(Points, Normal)
```

```

System.bool CreatePlanarTrimSurfaceDLL( 
   System.object Points,
   System.object Normal
)
```

```

System.bool CreatePlanarTrimSurfaceDLL( 
   System.Object^ Points,
   System.Object^ Normal
) 
```

#### Parameters

*Points*
:   Array of the points for the surface; trim curves are automatically created between each sequential vertex

*Normal*
:   Array of normal vector for the surface

#### Return Value

True if planar trim surface is created, false if not

Remarks

You can use this method instead of [IBody2:CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md), [IBody2::ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md), and [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md).

Example

[Create Imported Solid Body (C#)](Create_Imported_Solid_Body_Example_CSharp.htm)  
[Create Imported Solid Body (VB.NET)](Create_Imported_Solid_Body_Example_VBNET.htm)  
[Create Imported Solid Body (VBA)](Create_Imported_Solid_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreatePlanarTrimSurfaceDLL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.md)
