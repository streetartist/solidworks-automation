# IGetDatumTags Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTags`

Gets all the datum tags on this drawing view.
Gets all the datum tags on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDatumTags( _
   ByVal NumDatumTag As System.Integer _
) As DatumTag
```

```

Dim instance As IView
Dim NumDatumTag As System.Integer
Dim value As DatumTag
 
value = instance.IGetDatumTags(NumDatumTag)
```

```

DatumTag IGetDatumTags( 
   System.int NumDatumTag
)
```

```

DatumTag^ IGetDatumTags( 
   System.int NumDatumTag
) 
```

#### Parameters

*NumDatumTag*
:   Total number of datum tags on the drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum tags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of datum tags all at once instead of calling [IView::GetFirstDatumTag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.md) and then repeatedly calling [IDatumTag::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.md) to obtain the remaining datum tags on this drawing view.

Before calling this method, call [IView::GetDatumTagCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.md) to get the value for numDatumTag.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumTagCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.md)  
[IView::GetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags.md)
