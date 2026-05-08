# GetFirstRevisionCloud2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud2`

Gets the first revision cloud annotation in this view.
Gets the first revision cloud annotation in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstRevisionCloud2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstRevisionCloud2()
```

```

System.object GetFirstRevisionCloud2()
```

```

System.Object^ GetFirstRevisionCloud2(); 
```

#### Return Value

[IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)

Remarks

This method obsoletes IView::GetFirstRevisionCloud by supporting inactive sheets.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetRevisionCloudCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.md)  
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.md)
