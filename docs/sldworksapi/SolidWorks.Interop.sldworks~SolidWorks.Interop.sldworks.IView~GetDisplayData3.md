# GetDisplayData3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData3`

Obsolete. Superseded by IView::GetDisplayData4.
Obsolete. Superseded by [IView::GetDisplayData4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayData3() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDisplayData3()
```

```

System.object GetDisplayData3()
```

```

System.Object^ GetDisplayData3(); 
```

#### Return Value

[IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) object

Remarks

The data kept with the [IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

This method supersedes the now obsolete [IView::GetDisplayData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData2.md) and should be used in its place. The previous version of this method returned model items that were not imported to the drawing view and, therefore, not visible in the drawing view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetDisplayData3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayData3.md)
