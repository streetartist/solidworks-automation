# IGetTessellation Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetTessellation`

Obsolete. Superseded by IBody2::IGetTessellation.
Obsolete. Superseded by [IBody2::IGetTessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessellation( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face _
) As Tessellation
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim value As Tessellation
 
value = instance.IGetTessellation(NumOfFaces, FaceList)
```

```

Tessellation IGetTessellation( 
   System.int NumOfFaces,
   ref Face FaceList
)
```

```

Tessellation^ IGetTessellation( 
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
