# SearchOption Property (ISwDMExternalReferenceOption)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.html) on this topic. |
| SearchOption Property (ISwDMExternalReferenceOption) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md) : SearchOption Property (ISwDMExternalReferenceOption) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets and sets the search options for retrieving information about the external references in the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property SearchOption As SwDMSearchOption ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMExternalReferenceOption Dim value As SwDMSearchOption   instance.SearchOption = value   value = instance.SearchOption ``` | |

| C# |  |
| --- | --- |
| ``` SwDMSearchOption SearchOption {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDMSearchOption^ SearchOption {    SwDMSearchOption^ get();    void set ( &   SwDMSearchOption^ value); } ``` | |

#### Property Value

An [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMExternalReferenceOption::SearchOption](swdocumentmgr~SwDMExternalReferenceOption~SearchOption.md).

# Example

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
  
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
  
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

# Remarks

To set this property:

1. Call [ISwDMApplication::GetSearchOptionObject](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetSearchOptionObject.md).
2. Modify the returned ISwDMSearchOption object as needed.
3. Assign this property to the modified ISwDMSearchOption object.

# See Also

#### 

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md)
  
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.md)
  
[ISwDMDocument15::GetExternalFeatureReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.md)

# Availability

SOLIDWORKS Document Manager API 2011 SP0
