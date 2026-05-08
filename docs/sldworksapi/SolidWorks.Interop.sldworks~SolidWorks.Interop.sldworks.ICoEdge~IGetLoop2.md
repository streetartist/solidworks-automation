# IGetLoop2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetLoop2`

Gets the loop containing this coedge.
Gets the loop containing this coedge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLoop2() As Loop2
```

```

Dim instance As ICoEdge
Dim value As Loop2
 
value = instance.IGetLoop2()
```

```

Loop2 IGetLoop2()
```

```

Loop2^ IGetLoop2(); 
```

#### Return Value

Pointer to the [loop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::GetLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetLoop.md)  
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.md)  
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.md)
