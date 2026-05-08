# IGetDisplayData3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayData3`

Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view.
Gets the the [IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) object for this drawing view containing only those model items that are visible in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDisplayData3() As DisplayData
```

```

Dim instance As IView
Dim value As DisplayData
 
value = instance.IGetDisplayData3()
```

```

DisplayData IGetDisplayData3()
```

```

DisplayData^ IGetDisplayData3(); 
```

#### Return Value

[IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) object

Remarks

The data kept with the [IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

This method supersedes the now obsolete [IView::IGetDisplayData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayData2.md) and should be used in its place. The previous version of this method returned model items that were not imported to the drawing view and, therefore, not visible in the drawing view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayData3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData3.md)
