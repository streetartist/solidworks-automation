# CreateBodyFromFaces Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromFaces`

Creates a temporary body from the faces.
Creates a temporary body from the faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Object
 
value = instance.CreateBodyFromFaces(NumOfFaces, FaceList)
```

```

System.object CreateBodyFromFaces( 
   System.int NumOfFaces,
   System.object FaceList
)
```

```

System.Object^ CreateBodyFromFaces( 
   System.int NumOfFaces,
   System.Object^ FaceList
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces to use to create the body

*FaceList*
:   Array containing the faces to use to create the body

#### Return Value

Object for the body

Example

[Create Body from Selected Faces (C#)](Create_Body_From_Selected_Faces_Example_CSharp.htm)  
[Create Body from Selected Faces (VB.NET)](Create_Body_From_Selected_Faces_Example_VBNET.htm)  
[Create Body from Selected Faces (VBA)](Create_Body_From_Selected_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreateBodyFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBodyFromFaces.md)
