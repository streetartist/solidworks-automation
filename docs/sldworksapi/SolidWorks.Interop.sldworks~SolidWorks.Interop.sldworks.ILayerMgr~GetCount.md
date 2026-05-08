# GetCount Method (ILayerMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCount`

Gets the number of layers in this drawing document.
Gets the number of layers in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCount() As System.Integer
```

```

Dim instance As ILayerMgr
Dim value As System.Integer
 
value = instance.GetCount()
```

```

System.int GetCount()
```

```

System.int GetCount(); 
```

#### Return Value

Number of layers

Remarks

Call this method before calling [ILayerMgr::IGetLayerList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)
