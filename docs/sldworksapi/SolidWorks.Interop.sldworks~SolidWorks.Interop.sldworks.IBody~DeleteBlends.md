# DeleteBlends Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DeleteBlends`

Obsolete. Superseded by IBody2::DeleteBlends2.
Obsolete. Superseded by [IBody2::DeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteBlends( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Boolean
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Boolean
 
value = instance.DeleteBlends(NumOfFaces, FaceList)
```

```

System.bool DeleteBlends( 
   System.int NumOfFaces,
   System.object FaceList
)
```

```

System.bool DeleteBlends( 
   System.int NumOfFaces,
   System.Object^ FaceList
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
