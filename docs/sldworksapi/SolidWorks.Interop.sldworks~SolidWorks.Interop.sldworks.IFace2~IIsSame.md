# IIsSame Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsSame`

Gets whether the two faces are the same.
Gets whether the two faces are the same.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIsSame( _
   ByVal FaceIn As Face2 _
) As System.Boolean
```

```

Dim instance As IFace2
Dim FaceIn As Face2
Dim value As System.Boolean
 
value = instance.IIsSame(FaceIn)
```

```

System.bool IIsSame( 
   Face2 FaceIn
)
```

```

System.bool IIsSame( 
   Face2^ FaceIn
) 
```

#### Parameters

*FaceIn*
:   Pointer to the [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which to compare this face

#### Return Value

True if the two faces are the same, false if they are different

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IsSame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsSame.md)
