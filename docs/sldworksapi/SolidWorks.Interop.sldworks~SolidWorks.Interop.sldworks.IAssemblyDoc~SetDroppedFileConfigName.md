# SetDroppedFileConfigName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName`

Sets the configuration name for the recently dropped file.
Sets the configuration name for the recently dropped file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDroppedFileConfigName( _
   ByVal ConfigName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim ConfigName As System.String
Dim value As System.Boolean
 
value = instance.SetDroppedFileConfigName(ConfigName)
```

```

System.bool SetDroppedFileConfigName( 
   System.string ConfigName
)
```

```

System.bool SetDroppedFileConfigName( 
   System.String^ ConfigName
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration to set

#### Return Value

True if the name is successfully set, false if not

Remarks

If the configuration name is set in response to the [FileDropNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.md) event, SOLIDWORKS does not display the dialog for the selected configuration names when a file is dropped in an assembly.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md)  
[IAssemblyDoc::GetDroppedAtEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.md)
