# IGetRevisionClouds Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds`

Gets all of the revision cloud annotations in this view.
Gets all of the revision cloud annotations in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRevisionClouds( _
   ByVal NumRevClouds As System.Integer _
) As RevisionCloud
```

```

Dim instance As IView
Dim NumRevClouds As System.Integer
Dim value As RevisionCloud
 
value = instance.IGetRevisionClouds(NumRevClouds)
```

```

RevisionCloud IGetRevisionClouds( 
   System.int NumRevClouds
)
```

```

RevisionCloud^ IGetRevisionClouds( 
   System.int NumRevClouds
) 
```

#### Parameters

*NumRevClouds*
:   Number of revision cloud annotations in this view (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [revision cloud annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IView::GetRevisionCloudCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.md) to populate NumRevClouds.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.md)  
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.md)  
[IView::IGetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud.md)
