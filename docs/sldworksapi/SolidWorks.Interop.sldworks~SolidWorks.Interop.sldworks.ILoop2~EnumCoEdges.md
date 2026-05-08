# EnumCoEdges Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumCoEdges`

Enumerates the coedges in a loop.
Enumerates the coedges in a loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumCoEdges() As EnumCoEdges
```

```

Dim instance As ILoop2
Dim value As EnumCoEdges
 
value = instance.EnumCoEdges()
```

```

EnumCoEdges EnumCoEdges()
```

```

EnumCoEdges^ EnumCoEdges(); 
```

#### Return Value

[Coedges enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)

Remarks

The [ICoEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter.md).

The coedge direction always aligns with the direction of the ILoop2.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.md)  
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.md)
