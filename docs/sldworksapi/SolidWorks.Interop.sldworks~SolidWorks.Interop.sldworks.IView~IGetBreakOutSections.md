# IGetBreakOutSections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakOutSections`

Gets all of the broken-out sections in this view.
Gets all of the broken-out sections in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBreakOutSections( _
   ByVal Count As System.Integer _
) As Feature
```

```

Dim instance As IView
Dim Count As System.Integer
Dim value As Feature
 
value = instance.IGetBreakOutSections(Count)
```

```

Feature IGetBreakOutSections( 
   System.int Count
)
```

```

Feature^ IGetBreakOutSections( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of broken-out sections in this view

#### Return Value

- In-process, unmanaged C++: Pointer to an array of broken-out section [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetBreakOutSectionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSectionCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections.md)
