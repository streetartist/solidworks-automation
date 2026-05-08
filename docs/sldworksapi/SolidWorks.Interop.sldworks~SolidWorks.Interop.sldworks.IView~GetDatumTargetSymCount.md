# GetDatumTargetSymCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSymCount`

Gets the number of datum target symbols on this drawing view.
Gets the number of datum target symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumTargetSymCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetDatumTargetSymCount()
```

```

System.int GetDatumTargetSymCount()
```

```

System.int GetDatumTargetSymCount(); 
```

#### Return Value

Number of datum target symbols

Remarks

Call this method before calling [IView::IGetDatumTargetSyms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTargetSyms.md) to determine the size of the array for that method.

Example

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms.md)
