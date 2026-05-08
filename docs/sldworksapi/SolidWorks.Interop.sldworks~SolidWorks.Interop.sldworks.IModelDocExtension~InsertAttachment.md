# InsertAttachment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment`

Inserts a file as an Attachment to this document.
Inserts a file as an Attachment to this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertAttachment( _
   ByVal FileName As System.String, _
   ByVal Linked As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FileName As System.String
Dim Linked As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertAttachment(FileName, Linked)
```

```

System.bool InsertAttachment( 
   System.string FileName,
   System.bool Linked
)
```

```

System.bool InsertAttachment( 
   System.String^ FileName,
   System.bool Linked
) 
```

#### Parameters

*FileName*
:   Path and filename of file to insert as an Attachment to this document

*Linked*
:   True to link the document to the file, false to not

#### Return Value

True if the file is inserted as an Attachment, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.md)  
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.md)  
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.md)  
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.md)
