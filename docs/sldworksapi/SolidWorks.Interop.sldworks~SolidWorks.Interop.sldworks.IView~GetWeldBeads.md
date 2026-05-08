# GetWeldBeads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads`

Gets all of the weld beads on this drawing view.
Gets all of the weld beads on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWeldBeads() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetWeldBeads()
```

```

System.object GetWeldBeads()
```

```

System.Object^ GetWeldBeads(); 
```

#### Return Value

Array of [weld beads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md)

Remarks

Use this method to obtain the array of weld beads all at once instead of calling [IView::GetFirstWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.md) and then repeatedly calling [IWeldBead::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.md) to obtain the weld beads.

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
[IView::GetWeldBeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeadCount.md)  
[IView::IGetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads.md)  
[IView::GetFirstWeldBead Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.md)  
[IWeldBead::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.md)
