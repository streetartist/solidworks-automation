# SetId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId`

Sets the edge ID of this edge of an imported body.
Sets the edge ID of this edge of an imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetId( _
   ByVal IdIn As System.Integer _
) 
```

```

Dim instance As IEdge
Dim IdIn As System.Integer
 
instance.SetId(IdIn)
```

```

void SetId( 
   System.int IdIn
)
```

```

void SetId( 
   System.int IdIn
) 
```

#### Parameters

*IdIn*
:   Edge ID of this edge of an imported body

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
[IEdge::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.md)
