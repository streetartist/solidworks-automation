# GetTitle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTitle`

Gets the title of the document that appears in the active window's title bar.
Gets the title of the document that appears in the active window's title bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTitle() As System.String
```

```

Dim instance As IModelDoc2
Dim value As System.String
 
value = instance.GetTitle()
```

```

System.string GetTitle()
```

```

System.String^ GetTitle(); 
```

#### Return Value

Title string, usually displayed on the window's title bar

Remarks

The document name that appears in the window header changes based on your File Explorer settings. If you chose to suppress known file extensions, then the title shown in the window, and returned by this method, varies (for example, Part1.sldprt vs. Part1)

Example

[Detecting In-context Edit (C++)](Get_Edit_In_Context_Example_CPlusPlus_COM.htm)  
[Close Document (VBA)](Close_Document_Example_VB.htm)  
[Get Document Information (VBA)](Get_Document_Information_Example_VB.htm)  
[Get Names of Components and Window Handle and DIBSECTION (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)  
[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)  
[Save Rollbacked Part As Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SetTitle2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTitle2.md)
