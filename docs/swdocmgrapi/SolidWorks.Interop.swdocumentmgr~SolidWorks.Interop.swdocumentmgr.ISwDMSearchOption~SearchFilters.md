# SearchFilters Property (ISwDMSearchOption)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~SearchFilters`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~SearchFilters.html) on this topic. |
| SearchFilters Property (ISwDMSearchOption) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) : SearchFilters Property (ISwDMSearchOption) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets the search filters.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property SearchFilters As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSearchOption Dim value As System.Integer   instance.SearchFilters = value   value = instance.SearchFilters ``` | |

| C# |  |
| --- | --- |
| ``` System.int SearchFilters {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.int SearchFilters {    System.int get();    void set ( &   System.int value); } ``` | |

#### Property Value

Filter search as defined by [SwDMSearchFilters](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmSearchFilters.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMSearchOption::SearchFilters](swdocumentmgr~SwDMSearchOption~SearchFilters.md).

# Example

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
  
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

# See Also

#### 

[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)
  
[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
