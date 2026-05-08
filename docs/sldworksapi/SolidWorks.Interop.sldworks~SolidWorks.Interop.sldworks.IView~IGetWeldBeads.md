# IGetWeldBeads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads`

Gets all of the weld beads on this drawing view.
Gets all of the weld beads on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetWeldBeads( _
   ByVal NumWeldBead As System.Integer _
) As WeldBead
```

```

Dim instance As IView
Dim NumWeldBead As System.Integer
Dim value As WeldBead
 
value = instance.IGetWeldBeads(NumWeldBead)
```

```

WeldBead IGetWeldBeads( 
   System.int NumWeldBead
)
```

```

WeldBead^ IGetWeldBeads( 
   System.int NumWeldBead
) 
```

#### Parameters

*NumWeldBead*
:   Total number of weld beads on this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [weld beads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of weld beads all at once instead of calling [IView::GetFirstWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.md) and then repeatedly calling [IWeldBead::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.md) to obtain the weld beads in the drawing view.

Before calling this method, call [IView::GetWeldBeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeadCount.md) to get the value for numWeldBead.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.md)
