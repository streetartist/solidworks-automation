# AttachSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface`

Attaches a surface to this face.
Attaches a surface to this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AttachSurface( _
   ByVal SurfIn As Surface, _
   ByVal SenseIn As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFace2
Dim SurfIn As Surface
Dim SenseIn As System.Boolean
Dim value As System.Boolean
 
value = instance.AttachSurface(SurfIn, SenseIn)
```

```

System.bool AttachSurface( 
   Surface SurfIn,
   System.bool SenseIn
)
```

```

System.bool AttachSurface( 
   Surface^ SurfIn,
   System.bool SenseIn
) 
```

#### Parameters

*SurfIn*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) to attach to face

*SenseIn*
:   True if surface normal and face normal are in the same direction, false if surface normal and face normal are in opposite direction

#### Return Value

True if surface is attached to face, false if not

Remarks

To detach surfaces from faces, use [IFace2::DetachSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface.md). Neither IFace2::AttachSurface nor IFace2::DetachSurface affect body topology.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.md)  
[IFace2::IGetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.md)  
[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.md)
