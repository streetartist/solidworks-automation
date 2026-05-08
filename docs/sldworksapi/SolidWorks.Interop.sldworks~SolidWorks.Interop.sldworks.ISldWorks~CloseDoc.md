# CloseDoc Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc`

Closes the specified document.
Closes the specified document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CloseDoc( _
   ByVal Name As System.String _
) 
```

```

Dim instance As ISldWorks
Dim Name As System.String
 
instance.CloseDoc(Name)
```

```

void CloseDoc( 
   System.string Name
)
```

```

void CloseDoc( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of document (see **Remarks**)

Remarks

If Name is specified with:

- the name of a document that is not open, then this method does nothing.
- an empty string  (""), then the active document is closed without saving.
- the name of a document in the dirty state (modified, but not saved), then this method closes the document without saving it.

This method also closes any non-active hidden documents.

For documents referenced by other documents loaded in memory, call this method to release user-interface resources while keeping the model data loaded.

If you are closing the only document open in the SOLIDWORKS session and this SOLIDWORKS session is a background session, then calling this method, or calling [ISldWorks::QuitDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md), results in the SOLIDWORKS session being closed.

A background SOLIDWORKS session can be created when the SOLIDWORKS session is started by your application and the session is not controlled by the user; i.e., [ISldWorks::UserControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md) set to false.

To keep the SOLIDWORKS session open, set ISldWorks::UserControl to True, which makes the session visible, or you can close your documents at the end of your program execution.

Example

[Close Document (VBA)](Close_Document_Example_VB.htm)  
[Get Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)  
[Run or Attach to a SOLIDWORKS Session (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)  
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)  
[Get Names of Creators of Features (VBA)](Get_Names_of_Creators_of_Features_Example_VB.htm)  
[Get Names of Creators of Features (VB.NET)](Get_Names_of_Creators_of_Features_Example_VBNET.htm)  
[Get Names of Creators of Features (C#)](Get_Names_of_Creators_of_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)  
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md)  
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md)  
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md)  
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.md)  
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.md)  
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.md)  
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.md)  
[ISldWorks::CloseAndReopen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md)
