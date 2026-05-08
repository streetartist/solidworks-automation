# IGetFirstRevisionCloud Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud`

Gets the first revision cloud annotation in this view.
Gets the first revision cloud annotation in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstRevisionCloud() As RevisionCloud
```

```

Dim instance As IView
Dim value As RevisionCloud
 
value = instance.IGetFirstRevisionCloud()
```

```

RevisionCloud IGetFirstRevisionCloud()
```

```

RevisionCloud^ IGetFirstRevisionCloud(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an

  [IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.md)  
[IView::GetRevisionCloudCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.md)  
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.md)  
[IView::IGetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.md)
