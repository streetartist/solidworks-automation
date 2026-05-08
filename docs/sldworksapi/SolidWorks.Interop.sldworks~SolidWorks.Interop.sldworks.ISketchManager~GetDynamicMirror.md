# GetDynamicMirror Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetDynamicMirror`

Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled.
Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDynamicMirror() As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
value = instance.GetDynamicMirror()
```

```

System.bool GetDynamicMirror()
```

```

System.bool GetDynamicMirror(); 
```

#### Return Value

True if dynamic sketch mirroring is enabled, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::SetDynamicMirror Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetDynamicMirror.md)
