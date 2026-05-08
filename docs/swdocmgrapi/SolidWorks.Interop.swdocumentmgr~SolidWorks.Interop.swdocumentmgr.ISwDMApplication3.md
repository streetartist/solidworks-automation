# ISwDMApplication3 Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3.html) on this topic. |
| ISwDMApplication3 Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3_members.md) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMApplication3 Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Manages part, assembly, or drawing documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMApplication3     Inherits ISwDMApplication, ISwDMApplication2  ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMApplication3 ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMApplication3 : ISwDMApplication, ISwDMApplication2  ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMApplication3 : public ISwDMApplication, ISwDMApplication2  ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMApplication3](swdocumentmgr~SwDMApplication3.md).

# Remarks

- You can access an SwDMApplication3 object by calling QueryInterface on an [ISwDMApplication](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md) object in C++ or by direct assignment in Visual Basic.
- The SwDMApplication object can be assigned to a SwDMApplication3 variable, just like the SOLIDWORKS [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.md) object can be assigned to a SOLIDWORKS [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.md) variable.

# Accessors

[ISwDMClassFactory::GetApplication](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.md)

[ISwDMConfiguration::Application](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~Application.md)

[ISwDMConfigurationMgr::Application](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.md)

# See Also

#### 

[ISwDMApplication3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.md)
  
[ISwDMApplication4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4.md)
  
[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.md)
  
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)
  
[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md)
  
[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.md)
