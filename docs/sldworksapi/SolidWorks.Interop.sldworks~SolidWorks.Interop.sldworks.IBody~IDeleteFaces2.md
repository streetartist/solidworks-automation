# IDeleteFaces2 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteFaces2`

Obsolete. Superseded by IBody2::IDeleteFaces3.
Obsolete. Superseded by [IBody2::IDeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal Option As System.Integer _
) As System.Integer
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim Option As System.Integer
Dim value As System.Integer
 
value = instance.IDeleteFaces2(NumOfFaces, FaceList, Option)
```

```

System.int IDeleteFaces2( 
   System.int NumOfFaces,
   ref Face FaceList,
   System.int Option
)
```

```

System.int IDeleteFaces2( 
   System.int NumOfFaces,
   Face^% FaceList,
   System.int Option
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

*Option*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
