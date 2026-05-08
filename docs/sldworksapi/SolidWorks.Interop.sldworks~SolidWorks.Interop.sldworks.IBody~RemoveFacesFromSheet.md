# RemoveFacesFromSheet Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~RemoveFacesFromSheet`

Obsolete. Superseded by IBody2::RemoveFacesFromSheet.
Obsolete. Superseded by [IBody2::RemoveFacesFromSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FacesToRemove As System.Object _
) 
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FacesToRemove As System.Object
 
instance.RemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

```

void RemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.object FacesToRemove
)
```

```

void RemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.Object^ FacesToRemove
) 
```

#### Parameters

*NumOfFaces*

*FacesToRemove*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
