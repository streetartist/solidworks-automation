# IDeleteBlends Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteBlends`

Obsolete. Superseded by IBody2::IDeleteBlends2.
Obsolete. Superseded by [IBody2::IDeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteBlends( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face _
) As System.Boolean
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim value As System.Boolean
 
value = instance.IDeleteBlends(NumOfFaces, FaceList)
```

```

System.bool IDeleteBlends( 
   System.int NumOfFaces,
   ref Face FaceList
)
```

```

System.bool IDeleteBlends( 
   System.int NumOfFaces,
   Face^% FaceList
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
