# DeleteAttachment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment`

Deletes the specified file in the Attachments folder in the FeatureManager design tree.
Deletes the specified file in the Attachments folder in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteAttachment( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.DeleteAttachment(FileName)
```

```

System.bool DeleteAttachment( 
   System.string FileName
)
```

```

System.bool DeleteAttachment( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the file to delete from the Attachments folder in the FeatureManager design tree

#### Return Value

True if the file is deleted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.md)  
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.md)  
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.md)  
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.md)
