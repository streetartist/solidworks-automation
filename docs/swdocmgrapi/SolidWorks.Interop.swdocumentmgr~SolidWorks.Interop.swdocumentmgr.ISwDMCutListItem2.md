# ISwDMCutListItem2 Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html) on this topic. |
| ISwDMCutListItem2 Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)   [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMCutListItem2 Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Accesses cut-list items.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMCutListItem2     Inherits ISwDMCutListItem  ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMCutListItem2 : ISwDMCutListItem  ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMCutListItem2 : public ISwDMCutListItem  ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2](swdocumentmgr~SwDMCutListItem2.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# Remarks

- You can access an ISwCutListItem2 object by calling QueryInterface on an [ISwDMCutListItem](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md) object in C++ or by direct assignment in Visual Basic.
- The ISwDMCutListItem object can be assigned to an ISwDMCutListItem variable, just like the SOLIDWORKS [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.md) object can be assigned to a SOLIDWORKS [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.md) variable.

# Accessors

[ISwDMDocument10::GetCutListItems2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetCutListItems2.md)

# See Also

#### 

[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md)
  
[ISwDMCutListItem3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3.md)
  
[ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.md)
