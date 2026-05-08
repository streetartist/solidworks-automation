# GetApplication Method (ISwDMClassFactory)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html) on this topic. |
| GetApplication Method (ISwDMClassFactory) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.md) : GetApplication Method (ISwDMClassFactory) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*LicKey*
:   License key

Gets the application object for the SOLIDWORKS Document Manager API.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetApplication( _    ByVal LicKey As System.String _ ) As SwDMApplication ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMClassFactory Dim LicKey As System.String Dim value As SwDMApplication   value = instance.GetApplication(LicKey) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMApplication GetApplication(     System.string LicKey ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMApplication^ GetApplication(  &   System.String^ LicKey ) ``` | |

#### Parameters

*LicKey*
:   License key

#### Return Value

Pointer to the [ISwDMApplication](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMClassFactory::GetApplication](swdocumentmgr~SwDMClassFactory~GetApplication.md).

# Example

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)
  
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
  
[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)

# See Also

#### 

[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.md)
  
[ISwDMClassFactory Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
