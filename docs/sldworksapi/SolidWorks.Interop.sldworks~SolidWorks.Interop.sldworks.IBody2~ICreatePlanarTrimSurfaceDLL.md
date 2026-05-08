# ICreatePlanarTrimSurfaceDLL Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL`

Creates a planar trim surface for this body.
Creates a planar trim surface for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreatePlanarTrimSurfaceDLL( _
   ByVal VertexCount As System.Integer, _
   ByRef Points As System.Double, _
   ByRef Normal As System.Double _
) 
```

```

Dim instance As IBody2
Dim VertexCount As System.Integer
Dim Points As System.Double
Dim Normal As System.Double
 
instance.ICreatePlanarTrimSurfaceDLL(VertexCount, Points, Normal)
```

```

void ICreatePlanarTrimSurfaceDLL( 
   System.int VertexCount,
   ref System.double Points,
   ref System.double Normal
)
```

```

void ICreatePlanarTrimSurfaceDLL( 
   System.int VertexCount,
   System.double% Points,
   System.double% Normal
) 
```

#### Parameters

*VertexCount*
:   Number of vertices

*Points*
:   Pointer to an array of doubles describing the points for the surface; trim curves are automatically created between each sequential vertex

*Normal*
:   Pointer to an array of normal vectors for the surface

Remarks

You can use this method instead of [IBody2:CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md), [IBody2::ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md), and [ISurface::IAddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreatePlanarTrimSurfaceDLL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.md)
