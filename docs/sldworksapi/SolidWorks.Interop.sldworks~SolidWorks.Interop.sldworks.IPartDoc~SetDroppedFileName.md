# SetDroppedFileName Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetDroppedFileName`

Sets the filename for a recently dropped file.
Sets the filename for a recently dropped file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDroppedFileName( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SetDroppedFileName(FileName)
```

```

System.bool SetDroppedFileName( 
   System.string FileName
)
```

```

System.bool SetDroppedFileName( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the file to use for the rest of the drop process

#### Return Value

True if name is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md)  
[DPartDocEvents\_FileDropPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileDropPreNotifyEventHandler.md)
