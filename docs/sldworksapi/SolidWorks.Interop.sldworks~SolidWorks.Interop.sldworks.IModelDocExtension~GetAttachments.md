# GetAttachments Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments`

Gets the attachments for this document.
Gets the attachments for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachments( _
   ByRef LinkedVar As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim LinkedVar As System.Object
Dim value As System.Object
 
value = instance.GetAttachments(LinkedVar)
```

```

System.object GetAttachments( 
   out System.object LinkedVar
)
```

```

System.Object^ GetAttachments( 
   [Out] System.Object^ LinkedVar
) 
```

#### Parameters

*LinkedVar*
:   Array of VARIANT\_BOOL values indicating if a document is linked or not

#### Return Value

Array of strings of the names of the attachments for this document

Remarks

This method is supported by SOLIDWORKS 2005 and later.

There is a one-to-one correspondence between the output arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.md)  
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.md)  
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.md)  
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.md)
