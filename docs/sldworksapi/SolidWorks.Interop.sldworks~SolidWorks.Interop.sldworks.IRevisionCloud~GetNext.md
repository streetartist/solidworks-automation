# GetNext Method (IRevisionCloud)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetNext`

Gets the next revision cloud in a drawing view or sheet.
Gets the next revision cloud in a drawing view or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNext() As System.Object
```

```

Dim instance As IRevisionCloud
Dim value As System.Object
 
value = instance.GetNext()
```

```

System.object GetNext()
```

```

System.Object^ GetNext(); 
```

#### Return Value

[IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)

Remarks

You can traverse the revision cloud annotations in a drawing view as follows:

1. Call [IView::GetFirstRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.md) to get the first revision cloud.
2. Call this method [IView::GetRevisionCloudCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.md) times to access the other revision clouds.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)  
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.md)  
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.md)
