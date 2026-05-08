# ISwDMSheet3 Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3.html) on this topic. |
| ISwDMSheet3 Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3_members.md) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMSheet3 Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Accesses the drawing sheet.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMSheet3     Inherits ISwDMSheet, ISwDMSheet2  ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSheet3 ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMSheet3 : ISwDMSheet, ISwDMSheet2  ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMSheet3 : public ISwDMSheet, ISwDMSheet2  ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMSheet3](swdocumentmgr~SwDMSheet3.md).

# Remarks

- You can access an SwDMSheet3 object by calling QueryInterface on an [ISwDMSheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md) object in C++ or by direct assignment in Visual Basic.
- The SwDMSheet object can be assigned to a SwDMSheet3 variable, just like the SOLIDWORKS [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.md) object can be assigned to a SOLIDWORKS [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.md) variable.

# Accessors

[ISwDMDocument10::GetSheets](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetSheets.md)

[ISwDMTable5::Sheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet.md)

[ISwDMView::Sheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~Sheet.md)

# See Also

#### 

[ISwDMSheet3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md)
  
[ISwDMSheet2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2.md)
  
[ISwDMSheet4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.md)
