# GetDroppedAtEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity`

Gets a pointer to the entity where a file is dropped into this assembly.
Gets a pointer to the entity where a file is dropped into this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDroppedAtEntity() As System.Object
```

```

Dim instance As IAssemblyDoc
Dim value As System.Object
 
value = instance.GetDroppedAtEntity()
```

```

System.object GetDroppedAtEntity()
```

```

System.Object^ GetDroppedAtEntity(); 
```

#### Return Value

Object for the entity

Remarks

Use this method in the handler for the [FileDropNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.md) event.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::SetDroppedFileConfigName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.md)  
[SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md)
