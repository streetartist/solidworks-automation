# SetFaceId Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetFaceId`

Sets the face ID on an imported body.
Sets the face ID on an imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFaceId( _
   ByVal IdIn As System.Integer _
) 
```

```

Dim instance As IFace2
Dim IdIn As System.Integer
 
instance.SetFaceId(IdIn)
```

```

void SetFaceId( 
   System.int IdIn
)
```

```

void SetFaceId( 
   System.int IdIn
) 
```

#### Parameters

*IdIn*
:   Face ID

Remarks

SOLIDWORKS uses face IDs to track specific faces of imported bodies (for example, IGES imports).

Prior to setting a face ID, you should examine all faces in the model to [get their face IDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.md), if any, to ensure that the face ID you are setting is unique to the model.

Face IDs are saved with the document, but face IDs are removed whenever the document is rebuilt. Typically you assign face IDs to a read-only copy of the finalized model.

Any third-party application can change a face ID. The intent is that you assign face IDs so that you can refer to those faces within your application.

To store data with a face, use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::RemoveFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId.md)
