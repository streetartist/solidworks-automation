# IGetTemporaryAxes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTemporaryAxes`

Gets the information of the temporary axes displayed in this view.
Gets the information of the temporary axes displayed in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTemporaryAxes( _
   ByVal TempAxesCount As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim TempAxesCount As System.Integer
Dim value As System.Double
 
value = instance.IGetTemporaryAxes(TempAxesCount)
```

```

System.double IGetTemporaryAxes( 
   System.int TempAxesCount
)
```

```

System.double IGetTemporaryAxes( 
   System.int TempAxesCount
) 
```

#### Parameters

*TempAxesCount*
:   Number of temporary axes

    \

Remarks

Call [IView::GetTemporaryAxesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxesCount.md) before calling this method to get the value for TempAxesCount.

This array contains the start and end points, in that order, of temporary axes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetTemporaryAxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxes.md)
