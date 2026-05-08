# GetSense Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetSense`

Gets the sense of the coedge.
Gets the sense of the coedge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSense() As System.Boolean
```

```

Dim instance As ICoEdge
Dim value As System.Boolean
 
value = instance.GetSense()
```

```

System.bool GetSense()
```

```

System.bool GetSense(); 
```

#### Return Value

True if the coedge has the same direction as the underlying edge, false if not

Example

[Select Tangent Edges via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)  
[Get Sense for Each Coedge in a Loop (VBA)](Get_Sense_for_Each_Coedge_in_a_Loop_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)
