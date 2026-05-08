# RemoveFileSaveAsItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2`

Removes a file type from the File &gt; Save As dialog box that was added using ISldWorks::AddFileSaveAsItem2.
Removes a file type from the **File > Save As** dialog box that was added using [ISldWorks::AddFileSaveAsItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFileSaveAsItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String, _
   ByVal DocumentType As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim DocumentType As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveFileSaveAsItem2(Cookie, MethodName, Description, Extension, DocumentType)
```

```

System.bool RemoveFileSaveAsItem2( 
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension,
   System.int DocumentType
)
```

```

System.bool RemoveFileSaveAsItem2( 
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension,
   System.int DocumentType
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*MethodName*
:   Name of the application function used to save the file as specified in [ISldWorks::AddFileSaveAsItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.md)

*Description*
:   File description in the **Save as type** list

*Extension*
:   File name extension

*DocumentType*
:   Type of document to save as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

#### Return Value

True if the file type is removed from the **Save as type** list, false if not

Remarks

Call this method in your add-in's DisconnectFromSW method.

Example

[Add and Remove Items to File Save As and Open Menus (VB.NET)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_VBNET.htm)  
[Add and Remove Items to File Save As and Open Menus (C#)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddFileOpenItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3.md)  
[ISldWorks::RemoveFileOpenItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.md)
