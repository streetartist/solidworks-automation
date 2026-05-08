# Save3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3`

Saves the current document.
Saves the current document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Save3( _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.Save3(Options, Errors, Warnings)
```

```

System.bool Save3( 
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool Save3( 
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Options*
:   Mode in which to save the document as defined in [swSaveAsOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html)

*Errors*
:   Errors that caused the save operation to fail as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)

*Warnings*
:   Warnings or extra information generated during the save operation as defined in [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html)

#### Return Value

True if the save was successful, false if not

Remarks

| **If saving the file...** | **Then...** |
| --- | --- |
| Succeeds | - Return value is true - Errors argument is 0 |
| Fails | - Return value is false - Errors argument contains a bitwise OR of the error codes that were generated when saving the document |

You can find the masks to check against in the swFileSaveError\_e enumeration.

Even if the file is saved successfully, there might be warnings or information that occur during the save that might interest you. The Warnings argument contains a bitwise OR of the warning codes that were generated when saving the document. You can find the masks to check against in the swFileSaveWarning\_e enumeration.

| **If you do not want SOLIDWORKS to return...** | **Then pass in null or Nothing for...** |
| --- | --- |
| Error information | Errors argument |
| Warning information | Warnings argument |

This method results in FileSaveNotify being sent to any application listening.

See [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md) if this is new document, this document is to be saved to a file with a new name, or this document is to be saved to a version of a particular format.

Example

[Save File (VBA)](Save_File_Example_VB.htm)  
[Save File (VB.NET)](Save_File_Example_VBNET.htm)  
[Save File (C#)](Save_File_Example_CSharp.htm)  
[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)  
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)  
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)
