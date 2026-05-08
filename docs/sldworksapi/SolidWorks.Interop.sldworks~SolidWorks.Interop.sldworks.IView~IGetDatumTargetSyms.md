# IGetDatumTargetSyms Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTargetSyms`

Gets all of the datum target symbols on this drawing view.
Gets all of the datum target symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDatumTargetSyms( _
   ByVal NumDatumTargetSym As System.Integer _
) As DatumTargetSym
```

```

Dim instance As IView
Dim NumDatumTargetSym As System.Integer
Dim value As DatumTargetSym
 
value = instance.IGetDatumTargetSyms(NumDatumTargetSym)
```

```

DatumTargetSym IGetDatumTargetSyms( 
   System.int NumDatumTargetSym
)
```

```

DatumTargetSym^ IGetDatumTargetSyms( 
   System.int NumDatumTargetSym
) 
```

#### Parameters

*NumDatumTargetSym*
:   Total number of datum target symbols on the drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum target symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of datum target symbols all at once instead of calling [IView::GetFirstDatumTargetSym](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTargetSym.md) and then repeatedly calling [IDatumTargetSym::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetNext.md) to obtain the remaining datum target symbols on this drawing view.

Before calling this method, call [IView::GetDatumTargetSymCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSymCount.md) to get the value for numDatumTargetSym.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms.md)
