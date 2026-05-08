# EnumDocuments2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2`

Gets a list of documents currently open in the application.
Gets a list of documents currently open in the application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumDocuments2() As EnumDocuments2
```

```

Dim instance As ISldWorks
Dim value As EnumDocuments2
 
value = instance.EnumDocuments2()
```

```

EnumDocuments2 EnumDocuments2()
```

```

EnumDocuments2^ EnumDocuments2(); 
```

#### Return Value

[Documents enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.md)

Remarks

The list of [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) objects contained in the [IEnumDocuments2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.md) object contain any open IModelDoc2 pointer. This includes IModelDoc2 objects that may have been opened as file references, for example, from an assembly or drawing.

You might want to use the [IModelDoc::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md) property to determine if a particular document has its own window and is visible to the user.

Example

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks:GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks:GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks:CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md)  
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.md)  
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md)  
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md)
