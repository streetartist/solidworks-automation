# GetOpenedFileInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo`

Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when it opened.
Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when it opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetOpenedFileInfo( _
   ByRef FileName As System.String, _
   ByRef Options As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim Options As System.Integer
 
instance.GetOpenedFileInfo(FileName, Options)
```

```

void GetOpenedFileInfo( 
   out System.string FileName,
   out System.int Options
)
```

```

void GetOpenedFileInfo( 
   [Out] System.String^ FileName,
   [Out] System.int Options
) 
```

#### Parameters

*FileName*
:   Full path and filename of the last model successfully opened by SOLIDWORKS

*Options*
:   Options in effect when FileName opened as defined in [swOpenDocOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOpenDocOptions_e.html)

Remarks

This method considers only models opened through the SOLIDWORKS user interface. This method does not consider models successfully opened through the API, unless the API opens an assembly. In that case, each assembly component is opened by SOLIDWORKS, and this method determines which of those assembly's components was successfully opened last.

Example

```

'VBA
```

```

Dim swApp As SldWorks.SldWorks  
Dim path As String  
Dim docspec As SldWorks.DocumentSpecification  
Dim opened As String  
Dim Options As Long  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
Option Explicit  
Sub main()
```

```

    Set swApp = Application.SldWorks  
    swApp.CloseAllDocuments True  
    path = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\tutorial\api\bagel.sldprt"  
    Set docspec = swApp.GetOpenDocSpec(path)  
    Set Part = swApp.OpenDoc7(docspec)  
    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\tutorial\api\coffeecup.sldprt", 1, 0, "", longstatus, longwarnings)  
    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\tutorial\api\toaster.sldprt", 1, 0, "", longstatus, longwarnings)  
      
    ' None of the above documents successfully opened through the API get returned by GetOpenedFileInfo  
    swApp.GetOpenedFileInfo opened, Options  
    Debug.Print "Last successfully opened file: " & opened  
    Debug.Print "Options as defined in swOpenDocOptions_e: " & Options  
      
End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.md)  
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md)  
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.md)
