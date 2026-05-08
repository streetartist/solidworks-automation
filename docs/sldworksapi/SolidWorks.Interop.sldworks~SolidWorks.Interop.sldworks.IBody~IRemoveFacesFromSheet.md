# IRemoveFacesFromSheet Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IRemoveFacesFromSheet`

Obsolete. Superseded by IBody2::IRemoveFacesFromSheet.
Obsolete. Superseded by [IBody2::IRemoveFacesFromSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IRemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FacesToRemove As System.IntPtr _
) 
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FacesToRemove As System.IntPtr
 
instance.IRemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

```

void IRemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.IntPtr FacesToRemove
)
```

```

void IRemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.IntPtr FacesToRemove
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
