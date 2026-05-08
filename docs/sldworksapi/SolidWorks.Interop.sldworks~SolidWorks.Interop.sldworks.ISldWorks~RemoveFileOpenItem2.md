# RemoveFileOpenItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2`

Removes a file type from the File &gt; Open dialog box that was added using ISldWorks::AddFileOpenItem3.
Removes a file type from the File > Open dialog box that was added using [ISldWorks::AddFileOpenItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFileOpenItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim value As System.Boolean
 
value = instance.RemoveFileOpenItem2(Cookie, MethodName, Description, Extension)
```

```

System.bool RemoveFileOpenItem2( 
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension
)
```

```

System.bool RemoveFileOpenItem2( 
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*MethodName*
:   Name of the application function used to open the file as specified in [ISldWorks::AddFileOpenItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3.md)

*Description*
:   File description in the **Save as type** list

*Extension*
:   File name extension

#### Return Value

True if the file type is removed from the **Save as type** list, false if not

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
[ISldWorks::AddFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.md)  
[ISldWorks::RemoveFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2.md)
