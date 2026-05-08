# IsExploded Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded`

Obsolete. Superseded by IModelDocExtension::IsExploded.
Obsolete. Superseded by [IModelDocExtension::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsExploded() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.IsExploded()
```

```

System.bool IsExploded()
```

```

System.bool IsExploded(); 
```

#### Return Value

True if the model is currently exploded, false if the model is collapsed

Remarks

To take advantage of the explode mechanism, see [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md), [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md), [IAssemblyDoc::GetExplodedViewNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames.md), [IAssemblyDoc::IGetExplodedViewNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames.md), [IAssemblyDoc::GetExplodedViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.md), [IAssemblyDoc::AutoExplode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md), [IAssemblyDoc::ViewExplodeAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.md), [IAssemblyDoc::ViewCollapseAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.md), [IView::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.md), and [IView::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
