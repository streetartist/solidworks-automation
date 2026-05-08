# GetComponents Method (ISwDMConfiguration2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetComponents`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetComponents.html) on this topic. |
| GetComponents Method (ISwDMConfiguration2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md) : GetComponents Method (ISwDMConfiguration2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the components referenced by the configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetComponents() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration2 Dim value As System.Object   value = instance.GetComponents() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetComponents() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetComponents(); ``` | |

#### Return Value

Array of [ISwDMComponent](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.md) objects

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration2::GetComponents](swdocumentmgr~SwDMConfiguration2~GetComponents.md).

# Example

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
  
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
  
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
  
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

# Remarks

Do not use this method if a document component or reference is changed by [ISwDMDocument::ReplaceReference](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md) and the document is not subsequently opened and saved in SOLIDWORKS, because this method could return old and now nonexistent references. Instead, use [ISwDMDocument8::GetChangedReferences](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.md) or [ISwDMConfiguration11::GetReplacedComponents](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.md) until opening and saving the document in SOLIDWORKS.

This method only returns data for documents created using SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

# See Also

#### 

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md)
  
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP1
