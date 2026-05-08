# GetID Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID`

Gets the edge ID of this edge in an imported body.
Gets the edge ID of this edge in an imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As IEdge
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

Edge ID of this edge in an imported body

Remarks

SOLIDWORKS uses this ID to track edges of imported bodies.

The ID of the edge of an imported body:

- is not saved with the document.
- must be unique.
- can be changed by any third-party application. The intent is that if you [assign an ID to an edge of an imported body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.md), you can refer to that edge within your application.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) or [tracking ID](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm).

Use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object to store data with an edge.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::RemoveId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveId.md)  
[IEdge::SetId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.md)
