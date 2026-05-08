# GetAttachmentCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount`

Gets the number of attachments for this document.
Gets the number of attachments for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachmentCount() As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
value = instance.GetAttachmentCount()
```

```

System.int GetAttachmentCount()
```

```

System.int GetAttachmentCount(); 
```

#### Return Value

Number of Attachments for this document

Remarks

This method is supported by SOLIDWORKS 2005 and later.

Call this method before calling [IModelDocExtension::IGetAttachments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.md)  
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.md)  
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.md)
