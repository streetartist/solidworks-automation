# GetBodiesCount Method (IMoveCopyBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~GetBodiesCount`

Gets the number of bodies to move or rotate and copy.
Gets the number of bodies to move or rotate and copy.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesCount() As System.Integer
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Integer
 
value = instance.GetBodiesCount()
```

```

System.int GetBodiesCount()
```

```

System.int GetBodiesCount(); 
```

#### Return Value

Number of bodies to move or rotate and copy

Remarks

Call this method before calling [IMoveCopyBodyFeatureData::IGetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.md).

Example

[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)  
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)  
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies.md)  
[IMoveCopyBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~ISetBodies.md)
