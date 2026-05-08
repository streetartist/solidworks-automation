# GetDatumTargetSyms Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms`

Gets all of the datum target symbols on this drawing view.
Gets all of the datum target symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumTargetSyms() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDatumTargetSyms()
```

```

System.object GetDatumTargetSyms()
```

```

System.Object^ GetDatumTargetSyms(); 
```

#### Return Value

Array of [datum target symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)

Remarks

Use this method to obtain the array of datum target symbols all at once instead of calling [IView::GetFirstDatumTargetSym](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTargetSym.md) and then repeatedly calling [IDatumTargetSym::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetNext.md) to obtain the remaining datum target symbols on this drawing view.

Example

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumTargetSymCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSymCount.md)  
[IView::IGetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTargetSyms.md)
