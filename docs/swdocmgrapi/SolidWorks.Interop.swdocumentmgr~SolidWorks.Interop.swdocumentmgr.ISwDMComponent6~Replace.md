# Replace Method (ISwDMComponent6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~Replace`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~Replace.html) on this topic. |
| Replace Method (ISwDMComponent6) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6.md) : Replace Method (ISwDMComponent6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*fileName*
:   Path and file name of the component to replace this component

*ConfigurationName*
:   Configuration of the component to replace this component

*ReattachMates*
:   True to reattach mates to the component that replaced this component, false to not

Replace this component with the specified component.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Replace( _    ByVal fileName As System.String, _    ByVal ConfigurationName As System.String, _    ByVal ReattachMates As System.Boolean _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent6 Dim fileName As System.String Dim ConfigurationName As System.String Dim ReattachMates As System.Boolean Dim value As System.Boolean   value = instance.Replace(fileName, ConfigurationName, ReattachMates) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Replace(     System.string fileName,    System.string ConfigurationName,    System.bool ReattachMates ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool Replace(  &   System.String^ fileName, &   System.String^ ConfigurationName, &   System.bool ReattachMates ) ``` | |

#### Parameters

*fileName*
:   Path and file name of the component to replace this component

*ConfigurationName*
:   Configuration of the component to replace this component

*ReattachMates*
:   True to reattach mates to the component that replaced this component, false to not

#### Return Value

True if the operation succeeds, false if it fails

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent6::Replace](swdocumentmgr~SwDMComponent6~Replace.md).

# Example

[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
  
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

# Remarks

Call [ISwDMConfiguration11::GetReplacedComponents](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.md) to get information about replaced components in an assembly.

**NOTE:** If you call [ISwComponent6::PathName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.md) after calling ISwDMComponent6::Replace and before opening and saving an assembly, then the path to the original component is returned, not the path to the replaced component. References to replaced components are not updated until the assembly is opened and saved in SOLIDWORKS.

# See Also

#### 

[ISwDMComponent6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6.md)
  
[ISwDMComponent6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6_members.md)
  
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
