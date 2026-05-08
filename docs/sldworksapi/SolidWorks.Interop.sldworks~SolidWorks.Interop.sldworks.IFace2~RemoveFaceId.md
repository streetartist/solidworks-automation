# RemoveFaceId Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId`

Removes the face ID on an imported body.
Removes the face ID on an imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveFaceId( _
   ByVal IdIn As System.Integer _
) 
```

```

Dim instance As IFace2
Dim IdIn As System.Integer
 
instance.RemoveFaceId(IdIn)
```

```

void RemoveFaceId( 
   System.int IdIn
)
```

```

void RemoveFaceId( 
   System.int IdIn
) 
```

#### Parameters

*IdIn*
:   Face ID

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::SetFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetFaceId.md)  
[IFace2::GetFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.md)
