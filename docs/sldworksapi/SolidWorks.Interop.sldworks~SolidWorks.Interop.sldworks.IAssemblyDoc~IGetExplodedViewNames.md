# IGetExplodedViewNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames`

Obsolete. Superseded by IAssemblyDoc::GetExplodedViewNames2.
Obsolete. Superseded by [IAssemblyDoc::GetExplodedViewNames2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetExplodedViewNames( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetExplodedViewNames(Count)
```

```

System.string IGetExplodedViewNames( 
   System.int Count
)
```

```

System.String^ IGetExplodedViewNames( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of exploded views in the active configuration (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the exploded views in the active configuration
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IAssemblyDoc::GetExplodedViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.md) to get the value of Count.

To take advantage of the explode mechanism, see [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md), [IAssemblyDoc::GetExplodedViewNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames.md), [IAssemblyDoc::GetExplodedViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.md), [IAssemblyDoc::AutoExplode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md), [IAssemblyDoc::ShowExploded2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md), [IAssemblyDoc::ViewExplodeAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.md), [IAssemblyDoc::ViewCollapseAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.md), [IView::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.md), [IView::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.md), and [IModelDoc2::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
