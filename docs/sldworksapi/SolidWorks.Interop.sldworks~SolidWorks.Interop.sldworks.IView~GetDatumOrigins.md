# GetDatumOrigins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins`

Gets all of the datum origins on this drawing view.
Gets all of the datum origins on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumOrigins() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDatumOrigins()
```

```

System.object GetDatumOrigins()
```

```

System.Object^ GetDatumOrigins(); 
```

#### Return Value

Array of [datum origins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)

Remarks

Use this method to obtain the array of datum origins all at once instead of calling [IView::GetFirstDatumOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin.md) and then repeatedly calling [IDatumOrigin::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext.md) to obtain the remaining datum origins on this drawing view.

Example

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumOriginCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.md)  
[IView::IGetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.md)
