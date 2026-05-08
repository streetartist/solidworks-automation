# IGetLayerList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList`

Gets a list of layers in this drawing document.
Gets a list of layers in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLayerList() As System.String
```

```

Dim instance As ILayerMgr
Dim value As System.String
 
value = instance.IGetLayerList()
```

```

System.string IGetLayerList()
```

```

System.String^ IGetLayerList(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings containing the name of each [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object in this [ILayerMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md) object

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This is a 0-based array (first element is at position 0).

Call [ILayerMgr::GetCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::GetLayerList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerList.md)
