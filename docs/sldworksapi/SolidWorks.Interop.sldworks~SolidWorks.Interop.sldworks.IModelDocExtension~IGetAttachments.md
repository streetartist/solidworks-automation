# IGetAttachments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments`

Gets the attachments for this document.
Gets the attachments for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAttachments( _
   ByVal NumAttachments As System.Integer, _
   ByRef LinkedArr As System.Boolean _
) As System.String
```

```

Dim instance As IModelDocExtension
Dim NumAttachments As System.Integer
Dim LinkedArr As System.Boolean
Dim value As System.String
 
value = instance.IGetAttachments(NumAttachments, LinkedArr)
```

```

System.string IGetAttachments( 
   System.int NumAttachments,
   out System.bool LinkedArr
)
```

```

System.String^ IGetAttachments( 
   System.int NumAttachments,
   [Out] System.bool LinkedArr
) 
```

#### Parameters

*NumAttachments*
:   Number of attachments for this document

*LinkedArr*
:   - in-process, unmanaged C++: Pointer to an array of VARIANT\_BOOL values indicating if a document is linked or not

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the attachments for this document

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method is supported by SOLIDWORKS 2005 and later.

Call [IModelDocExtension::GetAttachmentCoun](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.md)t before calling this method to determine the size of the array.

There is a one-to-one correspondence between the output arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.md)  
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.md)  
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.md)
