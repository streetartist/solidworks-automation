# GetEdgeCount Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdgeCount`

Gets the number of edges for this body.
Gets the number of edges for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgeCount() As System.Integer
```

```

Dim instance As IBody2
Dim value As System.Integer
 
value = instance.GetEdgeCount()
```

```

System.int GetEdgeCount()
```

```

System.int GetEdgeCount(); 
```

#### Return Value

Number of edges

Remarks

Call this method before calling [IBody2::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.md).

Example

[Get Original Body from Pattern Body (VBA)](Get_Original_Body_from_Pattern_Body_Example_VB.htm)  
[Get Original Body from Pattern Body (VB.NET)](Get_Original_Body_from_Pattern_Body_Example_VBNET.htm)  
[Get Original Body from Pattern Body (C#)](Get_Original_Body_from_Pattern_Body_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
