# GetOpenDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument`

Gets the open document with the specified name.
Gets the open document with the specified name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOpenDocument( _
   ByVal DocName As System.String _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim DocName As System.String
Dim value As ModelDoc2
 
value = instance.GetOpenDocument(DocName)
```

```

ModelDoc2 GetOpenDocument( 
   System.string DocName
)
```

```

ModelDoc2^ GetOpenDocument( 
   System.String^ DocName
) 
```

#### Parameters

*DocName*
:   Name of the document (see **Remarks**)

#### Return Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

Only call this method for a document that has already been opened in its own window. If you call this method for a document that has not been opened in its own window, then methods on the returned object may not work as expected.

If you do not specify a file extension in the DocName argument, then the file extension of the document is ignored. This can cause problems if you have two different document types with the same name opened; for example, **12345.sldprt** and **12345.**sldasm.

If you do not specify the file extension in your call to this method, then you cannot be sure which document is retrieved. To avoid this problem, you can specify the filename extension in the DocName parameter or you can check the document type after it is activated using [IModelDoc2::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.md).

| If DocName is an empty string, and... | Then this method returns... |
| --- | --- |
| An assembly is opened | The first part of the assembly |
| Multiple assemblies are opened | The first part of the first assembly |
| Multile parts are opened | The first part |

Example

[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.md)  
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md)  
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.md)  
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.md)  
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.md)
