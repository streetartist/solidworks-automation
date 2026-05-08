# CreateOffsetSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface`

Creates a new surface offset from an existing surface.
Creates a new surface offset from an existing surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateOffsetSurface( _
   ByVal SurfaceIn As System.Object, _
   ByVal Distance As System.Double _
) As System.Object
```

```

Dim instance As IBody2
Dim SurfaceIn As System.Object
Dim Distance As System.Double
Dim value As System.Object
 
value = instance.CreateOffsetSurface(SurfaceIn, Distance)
```

```

System.object CreateOffsetSurface( 
   System.object SurfaceIn,
   System.double Distance
)
```

```

System.Object^ CreateOffsetSurface( 
   System.Object^ SurfaceIn,
   System.double Distance
) 
```

#### Parameters

*SurfaceIn*
:   Surface from which to offset the new surface

*Distance*
:   Offset distance

#### Return Value

Newly created offset surface

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.md)
