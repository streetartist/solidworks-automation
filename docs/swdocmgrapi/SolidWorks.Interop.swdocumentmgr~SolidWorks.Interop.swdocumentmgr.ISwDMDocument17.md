# ISwDMDocument17 Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.html) on this topic. |
| ISwDMDocument17 Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17_members.md)   [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMDocument17 Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Accesses the document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMDocument17     Inherits ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8  ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument17 ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMDocument17 : ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8  ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMDocument17 : public ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8  ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument17](swdocumentmgr~SwDMDocument17.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

Before you can access this object, you must call [ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md).

NOTES:

- You can access an ISwDMDocument17 object by calling QueryInterface on an [ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) object in C++ or by direct assignment in Visual Basic.
- The SwDMDocument object can be assigned to an ISwDMDocument17 variable, just like the SOLIDWORKS [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.md) object can be assigned to a SOLIDWORKS [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.md) variable.

# Accessors

[ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md)

[ISwDMConfiguration::Document](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~Document.md)

[ISwDMConfigurationMgr::Document](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~Document.md)

# See Also

#### 

[ISwDMDocument17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.md)
  
[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.md)
  
[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.md)
  
[ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.md)
  
[ISwDMDocument7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument7.md)
  
[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.md)
  
[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.md)
  
[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.md)
  
[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.md)
  
[ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.md)
  
[ISwDMDocument18 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument18.md)
  
[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md)
  
[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.md)
  
[ISwDMDocument21 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21.md)
  
[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.md)
  
[ISwDMDocument23 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23.md)
  
[ISwDMDocument24 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument24.md)
  
[ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.md)
  
[ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.md)
  
[ISwDMDocument27 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27.md)
  
[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.md)
  
[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.md)
  
[ISwDMDocument30 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument30.md)
