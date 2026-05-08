# GetExplodedViewNames Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames`

Obsolete. Superseded by IAssemblyDoc::GetExplodedViewNames2.
Obsolete. Superseded by [IAssemblyDoc::GetExplodedViewNames2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExplodedViewNames() As System.Object
```

```

Dim instance As IAssemblyDoc
Dim value As System.Object
 
value = instance.GetExplodedViewNames()
```

```

System.object GetExplodedViewNames()
```

```

System.Object^ GetExplodedViewNames(); 
```

#### Return Value

Array of strings of the names of the exploded views in the active configuration

Remarks

To take advantage of the explode mechanism, see [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md), [IAssemblyDoc::IGetExplodedViewNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames.md), [IAssemblyDoc::GetExplodedViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.md), [IAssemblyDoc::AutoExplode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md), [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md), [IAssemblyDoc::ViewExplodeAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.md), [IAssemblyDoc::ViewCollapseAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.md), [IView::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.md), [IView::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.md), and [IModelDoc2::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.md).

Example

[Create Exploded Views of an Assembly (VBA)](Create_Exploded_Views_Example_VB.htm)  
[Create Exploded Views of an Assembly (VB.NET)](Create_Exploded_Views_Example_VBNET.htm)  
[Create Exploded Views of an Assembly (C#)](Create_Exploded_Views_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
