# SelectMidpoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectMidpoint`

Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected.
Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectMidpoint() 
```

```

Dim instance As IModelDoc2
 
instance.SelectMidpoint()
```

```

void SelectMidpoint()
```

```

void SelectMidpoint(); 
```

Remarks

If the edge whose midpoint is desired is already on the selection list and you use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select it again, then IModelDoc2::SelectMidpoint leaves both the edge and the point on the selection list.

This method does not support 3D sketches.

Example

[Select the Midpoint of an Edge (VBA)](Put_a_Midpoint_on_an_Edge_Example_VB.htm)  
[Select the Midpoint of an Edge (VB.NET)](Put_a_Midpoint_on_an_Edge_Example_VBNET.htm)  
[Select the Midpoint of an Edge (C#)](Put_a_Midpoint_on_an_Edge_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
