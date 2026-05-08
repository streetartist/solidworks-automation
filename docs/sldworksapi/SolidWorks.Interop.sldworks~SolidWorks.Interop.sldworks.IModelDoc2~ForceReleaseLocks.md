# ForceReleaseLocks Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceReleaseLocks`

Releases the locks that a file system places on a file when it is opened and detaches that file from the file system.
Releases the locks that a file system places on a file when it is opened and detaches that file from the file system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ForceReleaseLocks() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.ForceReleaseLocks()
```

```

System.int ForceReleaseLocks()
```

```

System.int ForceReleaseLocks(); 
```

#### Return Value

1 if locks are released, 0 if not

Remarks

This method only supports part and assembly documents; it does not support drawing documents. See [ISldWorks::CloseAndReopen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md) for details about closing and reopening a drawing document without unloading its references from memory.

You must call [IModelDoc2::ReloadOrReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.md) after calling IModelDoc2::ForceReleaseLocks to re-attach the detached file to the file system. If you do not call IModelDoc2::ReloadOrReplace after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables).

IModelDoc2::ReloadOrReplace re-attaches the detached file to the file system; however, any changes made to the detached file are not preserved unless you save the file to disk before calling IModelDoc2::ReloadOrReplace.

CAUTION: This method is intended to be used by PDM systems. Using this method incorrectly could corrupt your data.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
