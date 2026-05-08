# AddFileOpenItem3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3`

Adds file types to the File &gt; Open dialog box.
Adds file types to the **File > Open** dialog box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFileOpenItem3( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String, _
   ByVal OptionLabel As System.String, _
   ByVal OptionMethodName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim OptionLabel As System.String
Dim OptionMethodName As System.String
Dim value As System.Boolean
 
value = instance.AddFileOpenItem3(Cookie, MethodName, Description, Extension, OptionLabel, OptionMethodName)
```

```

System.bool AddFileOpenItem3( 
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension,
   System.string OptionLabel,
   System.string OptionMethodName
)
```

```

System.bool AddFileOpenItem3( 
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension,
   System.String^ OptionLabel,
   System.String^ OptionMethodName
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*MethodName*
:   Name of the application function used to open the file (see **Remarks**)

*Description*
:   File description displayed in the **Save as type** list

*Extension*
:   File name extensions separated by semicolons

*OptionLabel*
:   Label for your options button or an empty string

*OptionMethodName*
:   Name of the callback method to display a dialog box, which appears when a user clicks your options button or an empty string

#### Return Value

True if the file types are added to the **Save as type** list, false if not

Remarks

Call this method in your add-in's ConnectToSW method.

Implement the function specified by MethodName with a string parameter that is the file name.

If your application is unloaded using an add-in, then you must remove any file types added with this method. See [ISldWorks::RemoveFileOpenItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.md).

The callback is called one time if the user:

- Presses the Shift or Ctrl key and selects multiple files to open in the **File > Open** Dialog.
- Drags-and-drops files into SOLIDWORKS from either File Explorer or the File Explorer tab in the TaskPane.

Example

[Add and Remove Items to File Save As and Open Menus (VB.NET)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_VBNET.htm)  
[Add and Remove Items to File Save As and Open Menus (C#)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RemoveFileOpenItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.md)  
[ISldWorks::RemoveFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2.md)  
[ISldWorks::AddFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.md)
