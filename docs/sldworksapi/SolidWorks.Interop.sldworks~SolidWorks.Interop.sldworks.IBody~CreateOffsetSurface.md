# CreateOffsetSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateOffsetSurface`

Obsolete. Superseded by IBody2::CreateOffsetSurface.
Obsolete. Superseded by [IBody2::CreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.md).

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

Dim instance As IBody
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

*Distance*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
