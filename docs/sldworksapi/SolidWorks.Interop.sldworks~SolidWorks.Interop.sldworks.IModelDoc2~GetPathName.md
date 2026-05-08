# GetPathName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName`

Gets the full path name for this document, including the file name.
Gets the full path name for this document, including the file name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPathName() As System.String
```

```

Dim instance As IModelDoc2
Dim value As System.String
 
value = instance.GetPathName()
```

```

System.string GetPathName()
```

```

System.String^ GetPathName(); 
```

#### Return Value

Full path name for this document including the file name; if the document has not yet been saved, then the string is empty

Example

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)  
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)  
[Get Active Document Dependents (VBA)](Get_Active_Document_Dependents_Example_VB.htm)  
[Get File Summary Information (VBA)](Get_File_Summary_Information_Example_VB.htm)  
[Get Unopened Document Dependents (VBA)](Get_Unopened_Document_Dependents_Example_VB.htm)  
[Get Paths of Open Documents (C#)](Get_Paths_of_Open_Documents_Example_CSharp.htm)  
[Get Paths of Open Documents (VB.NET)](Get_Paths_of_Open_Documents_Example_VBNET.htm)  
[Get Paths of Open Documents (VBA)](Get_Paths_of_Open_Documents_Example_VB.htm)  
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)  
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)  
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IComponent2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.md)  
[IComponent2::GetImportedPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetImportedPath.md)
