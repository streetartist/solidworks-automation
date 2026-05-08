# IGetDatumOrigins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins`

Gets all of the datum origins on this drawing view.
Gets all of the datum origins on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDatumOrigins( _
   ByVal NumDatumOrigin As System.Integer _
) As DatumOrigin
```

```

Dim instance As IView
Dim NumDatumOrigin As System.Integer
Dim value As DatumOrigin
 
value = instance.IGetDatumOrigins(NumDatumOrigin)
```

```

DatumOrigin IGetDatumOrigins( 
   System.int NumDatumOrigin
)
```

```

DatumOrigin^ IGetDatumOrigins( 
   System.int NumDatumOrigin
) 
```

#### Parameters

*NumDatumOrigin*
:   Total number of datum origins on the drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum origins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of datum origins all at once instead of calling [IView::GetFirstDatumOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin.md) and then repeatedly calling [IDatumOrigin::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext.md) to obtain the remaining datum origins on this drawing view.

Before calling this method, call [IView::GetDatumOriginCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.md) to get the value for numDatumOrigin.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumOriginCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.md)  
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.md)
