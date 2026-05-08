# IDeleteBlends2 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteBlends2`

Obsolete. Superseded by IBody2::IDeleteBlends2.
Obsolete. Superseded by [IBody2::IDeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean
 
value = instance.IDeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

```

System.bool IDeleteBlends2( 
   System.int NumOfFaces,
   ref Face FaceList,
   System.bool DoLocalCheck
)
```

```

System.bool IDeleteBlends2( 
   System.int NumOfFaces,
   Face^% FaceList,
   System.bool DoLocalCheck
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

*DoLocalCheck*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
