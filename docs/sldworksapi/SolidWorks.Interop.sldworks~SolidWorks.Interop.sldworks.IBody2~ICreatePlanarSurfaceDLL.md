# ICreatePlanarSurfaceDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurfaceDLL`

Creates a planar surface.
Creates a planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlanarSurfaceDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Normal As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim RootPoint As System.Double
Dim Normal As System.Double
Dim value As Surface
 
value = instance.ICreatePlanarSurfaceDLL(RootPoint, Normal)
```

```

Surface ICreatePlanarSurfaceDLL( 
   ref System.double RootPoint,
   ref System.double Normal
)
```

```

Surface^ ICreatePlanarSurfaceDLL( 
   System.double% RootPoint,
   System.double% Normal
) 
```

#### Parameters

*RootPoint*
:   Pointer to an array of 3 doubles (x,y,z)

*Normal*
:   Pointer to an array of 3 doubles (x,y,z)

#### Return Value

Pointer to the new planar surface

Remarks

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
