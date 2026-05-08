# GetVertexCount Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertexCount`

Gets the number of vertices in this body.
Gets the number of vertices in this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVertexCount() As System.Integer
```

```

Dim instance As IBody2
Dim value As System.Integer
 
value = instance.GetVertexCount()
```

```

System.int GetVertexCount()
```

```

System.int GetVertexCount(); 
```

#### Return Value

Number of vertices in this body

Remarks

Call this method before calling [IBody2::IGetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetVertices.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
